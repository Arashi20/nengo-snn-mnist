import os

# Basic helper script to push changes to GitHub
commit_msg = input("Enter commit message: ")
os.system("git add .")
os.system(f"git commit -m \"{commit_msg}\"")
os.system("git push origin main")
