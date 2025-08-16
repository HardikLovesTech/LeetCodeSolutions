import os
import subprocess
import openai
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

# Initialize OpenAI client with API key from env
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_commit_message(diff_content):
    """Generate commit message from git diff using OpenAI."""
    prompt = f"""
    You are an assistant that writes concise, clear git commit messages.
    Given this diff, write a short commit message in present tense:
    {diff_content}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # fast + cheap
        messages=[
            {"role": "system", "content": "You write concise git commit messages."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50
    )
    return response.choices[0].message.content.strip()

def git_auto_commit_push():
    """Stage all changes, generate commit message, and push."""
    # Stage all changes
    subprocess.run(["git", "add", "-A"], check=True)

    # Get diff for commit message generation
    diff_result = subprocess.run(
        ["git", "diff", "--cached"],
        stdout=subprocess.PIPE,
        text=True,
        check=True
    )
    diff_content = diff_result.stdout.strip()

    if not diff_content:
        print("No changes to commit.")
        return

    # Generate commit message
    commit_message = generate_commit_message(diff_content)
    print(f"Generated commit message: {commit_message}")

    # Commit and push
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    git_auto_commit_push()
