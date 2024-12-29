import os
import subprocess
from datetime import datetime, timedelta

# Configuration
repo_name = "Reask.com"
commit_message = "Automated commit"
days_to_commit = 100  # Number of days to make commits (past and future)
start_date = datetime.now() - timedelta(days=days_to_commit)  # Start from past

# Create or initialize a Git repository
if not os.path.exists(repo_name):
    os.makedirs(repo_name)
    os.chdir(repo_name)
    subprocess.run(["git", "init"])
else:
    os.chdir(repo_name)

# Function to set fake commit dates
def make_commit(date):
    with open("contribution.txt", "a") as file:
        file.write(f"Commit on {date}\n")
    subprocess.run(["git", "add", "contribution.txt"])
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date
    env["GIT_COMMITTER_DATE"] = date
    subprocess.run(["git", "commit", "-m", commit_message], env=env)

# Generate commits for the specified range
for i in range(days_to_commit):
    commit_date = (start_date + timedelta(days=i)).strftime("%Y-%m-%dT12:00:00")
    make_commit(commit_date)

# Push to GitHub
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "remote", "add", "origin", "https://github.com/maylo1yzx/Reask.com.git"]) 
subprocess.run(["git", "push", "-u", "origin", "main"])
