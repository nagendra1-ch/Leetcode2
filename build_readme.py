import os
import re
from datetime import datetime, timezone

# Path configuration
REPO_ROOT = "."
README_PATH = "README.md"

def get_problem_folders():
    folders = []
    # Matches folders named like '0001-two-sum' or '0001-Two-Sum'
    pattern = re.compile(r"^(\d{4})-(.+)$")
    
    for entry in os.listdir(REPO_ROOT):
        full_path = os.path.join(REPO_ROOT, entry)
        if os.path.isdir(full_path):
            match = pattern.match(entry)
            if match:
                num = match.group(1)
                slug = match.group(2)
                folders.append((num, slug, full_path, entry))
    return sorted(folders, key=lambda x: x[0])

def parse_problem_metadata(folder_path):
    # Default values
    difficulty = "Easy"
    language = "Python 3"
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Check for solution file extension
    for file in os.listdir(folder_path):
        if file.endswith(".py"):
            language = "Python 3"
        elif file.endswith(".cpp"):
            language = "C++"
        elif file.endswith(".java"):
            language = "Java"
        elif file.endswith(".sql"):
            language = "MySQL"

    # Inspect README or solution comments for difficulty if available
    readme_file = os.path.join(folder_path, "README.md")
    if os.path.exists(readme_file):
        with open(readme_file, "r", encoding="utf-8") as f:
            content = f.read()
            if "Medium" in content:
                difficulty = "Medium"
            elif "Hard" in content:
                difficulty = "Hard"
            elif "Easy" in content:
                difficulty = "Easy"

    return difficulty, language, date_str

def generate_dashboard():
    problems = get_problem_folders()
    
    stats = {"Easy": 0, "Medium": 0, "Hard": 0}
    table_rows = []
    
    for num, slug, folder_path, folder_name in problems:
        difficulty, language, date_str = parse_problem_metadata(folder_path)
        stats[difficulty] = stats.get(difficulty, 0) + 1
        
        problem_title = slug.replace("-", " ").title()
        problem_link = f"https://leetcode.com/problems/{slug.lower()}/"
        solution_link = f"./{folder_name}"
        
        row = f"| {num} | [{problem_title}]({problem_link}) | [{folder_name}]({solution_link}) | {difficulty} | {language} | {date_str} |"
        table_rows.append(row)
        
    total_solved = len(problems)
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    
    # Building Markdown UI matching your layout
    markdown = f"""# 🏆 LeetCode Solutions

<p align="center">
  <img src="https://img.shields.io/badge/TOTAL%20SOLVED-{total_solved}-blue?style=for-the-badge&logo=leetcode" />
  <img src="https://img.shields.io/badge/EASY-{stats['Easy']}-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/MEDIUM-{stats['Medium']}-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/HARD-{stats['Hard']}-red?style=for-the-badge" />
</p>

## 📊 Statistics

| Metric | Count |
| :--- | :--- |
| **Total Solved** | {total_solved} |
| **Easy** | {stats['Easy']} |
| **Medium** | {stats['Medium']} |
| **Hard** | {stats['Hard']} |
| **Languages** | Python 3, MySQL |
| **Last Updated** | {current_time} |

## 📁 Solutions

| # | Problem | Solution | Difficulty | Language | Date |
| :-: | :--- | :--- | :-: | :-: | :-: |
""" + "\n".join(table_rows) + "\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(markdown)

if __name__ == "__main__":
    generate_dashboard()
