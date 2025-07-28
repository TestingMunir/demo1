### 🔧 Git Basics

- `git init <directory>`  
  Create empty Git repo in specified directory. Run with no arguments to initialize the current directory as a git repository.  
  **Example:** `git init my-project`

- `git clone <repo>`  
  Clone repo located at `<repo>` onto local machine. Original repo can be located on the local filesystem or on a remote machine via HTTP or SSH.  
  **Example:** `git clone https://github.com/user/repo.git`

- `git add <directory>`  
  Stage all changes in `<directory>` for the next commit. Replace `<directory>` with a `<file>` to change a specific file.  
  **Example:** `git add .` or `git add index.html`

- `git commit -m "<message>"`  
  Commit the staged snapshot, but instead of launching a text editor, use `<message>` as the commit message.  
  **Example:** `git commit -m "Initial commit"`

- `git status`  
  List which files are staged, unstaged, and untracked.  
  **Example:** `git status`

- `git log`  
  Display the entire commit history using the default format.  
  **Example:** `git log`

### 🌿 Git Branches

- `git branch`  
  List all of the branches in your repo. Add a `<branch>` argument to create a new branch with the name `<branch>`.  
  **Example:** `git branch feature-login`

- `git checkout -b <branch>`  
  Create and check out a new branch named `<branch>`. Drop the `-b` flag to checkout an existing branch.  
  **Example:** `git checkout -b develop`

- `git merge <branch>`  
  Merge `<branch>` into the current branch.  
  **Example:** `git merge feature-login`

### ♻️ Undoing Changes

- `git diff`  
  Show unstaged changes between your index and working directory.  
  **Example:** `git diff`

- `git reset <file>`  
  Remove `<file>` from the staging area, but leave the working directory unchanged.  
  **Example:** `git reset index.html`

- `git checkout -- <file>`  
  Discard changes in working directory. Use with care!  
  **Example:** `git checkout -- index.html`

- `git revert <commit>`  
  Create new commit that undoes all of the changes made in `<commit>`, then apply it to the current branch.  
  **Example:** `git revert abc1234`

- `git reset`  
  Reset staging area to match most recent commit, but leave the working directory unchanged.  
  **Example:** `git reset`

- `git reset --hard`  
  Reset staging area and working directory to match most recent commit and overwrite all changes in the working directory.  
  **Example:** `git reset --hard`

### 🌐 Remote Repositories

- `git remote add <name> <url>`  
  Create a new connection to a remote repo. After adding a remote, you can use `<name>` as a shortcut for `<url>` in other commands.  
  **Example:** `git remote add origin https://github.com/user/repo.git`

- `git fetch <remote> <branch>`  
  Fetches a specific `<branch>` from the repo. Leave off `<branch>` to fetch all remote refs.  
  **Example:** `git fetch origin main`

- `git pull <remote>`  
  Fetch the specified remote’s copy of current branch and immediately merge it into the local copy.  
  **Example:** `git pull origin main`

- `git push <remote> <branch>`  
  Push the branch to `<remote>`, along with necessary commits and objects. Creates named branch in the remote repo if it doesn’t exist.  
  **Example:** `git push origin main`

### ⚒️ Configuration

- `git config --global user.name <name>`  
  Define the author name to be used for all commits by the current user.  
  **Example:** `git config --global user.name "Alice"`

- `git config --global user.email <email>`  
  Define the author email to be used for all commits by the current user.  
  **Example:** `git config --global user.email "alice@example.com"`

- `git config --global alias.<alias-name> <git-command>`  
  Create shortcut for a Git command. E.g. `alias.glog log --graph --oneline` will set `git glog` equivalent to `git log --graph --oneline`.  
  **Example:** `git config --global alias.co checkout`

- `git config --global --edit`  
  Open the global configuration file in a text editor for manual editing.  
  **Example:** `git config --global --edit`

- `git config --system core.editor <editor>`  
  Set text editor used by commands for all users on the machine. `<editor>` should be the command that launches the desired editor (e.g., vi).  
  **Example:** `git config --system core.editor nano`

### 📋 Rewriting Git History

- `git commit --amend`  
  Replace the last commit with the staged changes and last commit combined. Use with nothing staged to edit the last commit’s message.  
  **Example:** `git commit --amend -m "Updated commit message"`

- `git rebase <base>`  
  Rebase the current branch onto `<base>`.  
  **Example:** `git rebase main`

- `git rebase -i <base>`  
  Interactively rebase current branch onto `<base>`.  
  **Example:** `git rebase -i HEAD~3`

- `git reflog`  
  Show a log of changes to the local repository’s HEAD.  
  **Example:** `git reflog`

### 📊 Git Log Options

- `git log -<limit>`  
  Limit number of commits by `<limit>`.  
  **Example:** `git log -5`

- `git log --oneline`  
  Condense each commit to a single line.  
  **Example:** `git log --oneline`

- `git log --stat`  
  Include which files were altered and the relative number of lines added or deleted from each of them.  
  **Example:** `git log --stat`

- `git log -p`  
  Display the full diff of each commit.  
  **Example:** `git log -p`

- `git log --author="<pattern>"`  
  Search for commits by a particular author.  
  **Example:** `git log --author="Alice"`

- `git log --grep="<pattern>"`  
  Search for commits with a message that matches `<pattern>`.  
  **Example:** `git log --grep="bug fix"`

- `git log <since>..<until>`  
  Show commits that occur between `<since>` and `<until>`.  
  **Example:** `git log v1.0..v2.0`

- `git log -- <file>`  
  Only display commits that have the specified file.  
  **Example:** `git log -- README.md`

- `git log --graph --decorate`  
  Draw a text-based graph of commits.  
  **Example:** `git log --graph --decorate`

### 🔍 Git Diff Options

- `git diff HEAD`  
  Show difference between working directory and last commit.  
  **Example:** `git diff HEAD`

- `git diff --cached`  
  Show difference between staged changes and last commit.  
  **Example:** `git diff --cached`

### 🪑 Cleaning

- `git clean -n`  
  Shows which files would be removed from working directory.  
  **Example:** `git clean -n`

- `git clean -f`  
  Actually remove those files.  
  **Example:** `git clean -f`

### 📤 Git Push Variants

- `git push <remote> --all`  
  Push all of your local branches to the specified remote.  
  **Example:** `git push origin --all`

- `git push <remote> --tags`  
  Push all local tags.  
  **Example:** `git push origin --tags`

- `git push <remote> --force`  
  Force push — **use with caution**!  
  **Example:** `git push origin main --force`

- `git pull --rebase <remote>`  
  Fetch and rebase from remote branch instead of merging.  
  **Example:** `git pull --rebase origin main`

