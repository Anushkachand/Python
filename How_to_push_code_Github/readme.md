# 🚀 Push Code to GitHub (Step-by-Step Guide)

Follow these steps to upload your project to GitHub using VS Code.

---

## 📌 Step 1: Open Terminal in Project Folder

In VS Code:
- Right click on your project folder  
- Click **"Open in Terminal"**

---

## 📌 Step 2: Initialize Git (if not already done)

```
git init
```

## Step 3: Add Your GitHub Repository as Remote

- Goto your GitHub repository
- Click on the green Code button
- Copy the repository URL
- Then run:

```
git remote add origin https://github.com/Anushkachand/Python.git
```

### Step 4: Add Files
```
git add .
```
## Step 5: Commit Changes
```
     git commit -m "Added my Python code"
```
Step 6: Push to GitHub 
```
git branch -M main
git push -u origin main
```

-------------------------------------------------
# ❗ Common Errors & Fixes
Error:
```  
   error: src refspec main does not match any
```
✅ Solution:

Make sure you have committed at least once:
```
   git add .
   git commit -m "initial commit"
   git push -u origin main
```

------------------------------------------------------
Branch:


| Task          | Command                     |
| ------------- | --------------------------- |
| Show branches | `git branch`                |
| Switch branch | `git checkout branch-name`  |
| Delete branch | `git branch -d branch-name` |
|create branch  | `git branch new-branch-name`|
