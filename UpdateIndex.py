import os
import re

# ==== CONFIG ====
REPO_USERNAME = "HardikLovesTech"
REPO_NAME = "LeetCodeSolutions"
SOLUTIONS_DIR = "solutions"  # relative to README.md
README_FILE = "README.md"
# ===============

def clean_name(name: str) -> str:
    """Turn raw filename/folder name into readable title."""
    return name.replace("_", " ").replace("-", " ").title()

def parse_question_id(name: str) -> str:
    """Extract numeric prefix (LeetCode ID) if present."""
    match = re.match(r"^(\d+)", name)
    return match.group(1) if match else "-"

def generate_index():
    index_lines = []
    count = 1

    for entry in sorted(os.listdir(SOLUTIONS_DIR)):
        entry_path = os.path.join(SOLUTIONS_DIR, entry)

        # Case 1: Direct solution file (e.g., 1_TwoSum.py)
        if os.path.isfile(entry_path) and entry.endswith((".py", ".java", ".cpp")):
            qid = parse_question_id(entry)
            qname = clean_name(entry.split(".")[0])
            github_link = f"https://github.com/{REPO_USERNAME}/{REPO_NAME}/blob/main/{SOLUTIONS_DIR}/{entry}"
            index_lines.append(f"| {count} | {qid} | {qname} | - | [View Code]({github_link}) |")
            count += 1

        # Case 2: Folder (e.g., 7-reverse-integer/)
        elif os.path.isdir(entry_path):
            qid = parse_question_id(entry)
            qname = clean_name(entry)

            problem_link = "-"
            solution_links = []

            # Problem README
            readme_path = os.path.join(entry_path, "README.md")
            if os.path.exists(readme_path):
                problem_link = f"[Problem](https://github.com/{REPO_USERNAME}/{REPO_NAME}/blob/main/{entry_path}/README.md)"

            # Solution files
            for file in sorted(os.listdir(entry_path)):
                if file.endswith((".py", ".java", ".cpp")):
                    github_link = f"https://github.com/{REPO_USERNAME}/{REPO_NAME}/blob/main/{entry_path}/{file}"
                    solution_links.append(f"[{file}]({github_link})")

            solutions = "<br>".join(solution_links) if solution_links else "-"

            index_lines.append(f"| {count} | {qid} | {qname} | {problem_link} | {solutions} |")
            count += 1

    index_table = (
        "| # | Question ID | Question Name | Problem | Solution |\n"
        "|---|-------------|---------------|---------|----------|\n" +
        "\n".join(index_lines)
    )

    return index_table


def update_readme():
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- INDEX_START -->"
    end_marker = "<!-- INDEX_END -->"

    new_table = generate_index()

    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = f"{before}{start_marker}\n{new_table}\n{end_marker}{after}"
    else:
        new_content = content + f"\n\n{start_marker}\n{new_table}\n{end_marker}"

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ README.md updated with new index format.")


if __name__ == "__main__":
    update_readme()
