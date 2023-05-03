import os

# Freeze requirements.txt
os.system("pip freeze > requirements.txt")

# Re-run the describe script on the updated requirements.txt
os.system("DescribePackagesAndReformat.py")

# Commit and push to GitHub
os.system('git add . && git commit -m "commit from deploy" && git push')