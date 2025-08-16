import os

# ==== CONFIG ====
REPO_USERNAME = "HardikLovesTech"
REPO_NAME = "LeetCodeSolutions"
SOLUTIONS_DIR = "solutions"  # relative to README.md
README_FILE = "README.md"
# ===============

def generate_index():
    files = sorted(os.listdir(SOLUTIONS_DIR))
    index_lines = []
    count = 1

    for file in files:
        if file.endswith((".py", ".java", ".cpp")):
            problem_name = file.replace("_", " ").replace("-", " ").split(".")[0].title()
            github_link = f"https://github.com/{REPO_USERNAME}/{REPO_NAME}/blob/main/{SOLUTIONS_DIR}/{file}"
            index_lines.append(f"| {count} | {problem_name} | [View Code]({github_link}) |")
            count += 1

    index_table = (
        "| # | Problem Name | Solution Link |\n"
        "|---|--------------|---------------|\n" +
        "\n".join(index_lines)
    )

    return index_table

def update_readme():
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace the existing table (between markers) with the new one
    start_marker = "<!-- INDEX_START -->"
    end_marker = "<!-- INDEX_END -->"

    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = f"{before}{start_marker}\n{generate_index()}\n{end_marker}{after}"
    else:
        # If no markers exist, append at the end
        new_content = content + f"\n\n{start_marker}\n{generate_index()}\n{end_marker}"

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ README.md updated with the latest index.")

if __name__ == "__main__":
    update_readme()
