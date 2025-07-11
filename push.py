from git import Repo
import os

# === STEP 1: YOUR INFO HERE ===
USERNAME = "Helloworld23434"  # your GitHub username
TOKEN = "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"  # paste your token (starts with ghp_...)
REPO = "Python-projectz"  # example: mycode
BRANCH = "master"  # or 'master' if your repo uses that
LOCAL_PATH = "/storage/emulated/0/Python little projects"

# === STEP 2: SETUP REMOTE URL ===
remote_url = f"https://Helloworld23434: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@github.com/Helloworld23434/Python-projectz.git"

# === STEP 3: INIT GIT ===
repo = Repo.init(LOCAL_PATH)

# === STEP 4: ADD ALL FILES ===
repo.git.add(A=True)

# === STEP 5: COMMIT ===
repo.index.commit("Commit from Pydroid")

# === STEP 6: ADD OR UPDATE REMOTE ===
if "origin" not in [remote.name for remote in repo.remotes]:
    origin = repo.create_remote('origin', remote_url)
else:
    origin = repo.remotes.origin
    origin.set_url(remote_url)

# === STEP 7: PUSH TO GITHUB ===
origin.push(BRANCH)
print("File pushed to GitHub!")