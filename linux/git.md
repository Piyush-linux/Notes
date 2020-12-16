# History
---
+ __Application__
    - It is version control system
    - Usage for change in data file which can be track
    - Roll back to working
+ VSC-local
    - local VSC track file
    - If local HDD is destroyed then every file is gone
+ Centralized VSC
    - Which can be pull and push
    - If server is damage them every file is gone
+ Distributed VSC
    - Alike Centralized VSC
    - Complete history backup is available
    - Initialization of git
    - Hosted :: GitHub,GitLab,BitBucket

# Uses
---
- Snapshot th file ,not the difference
- Git repository is made of `file.git`
- Every operation is local
- Generally add data

# Git-bash
---
- For git commands
+ Configuration
    - git config --global user.name "name"
    - git config --global user.email "name@mail.com"
    - git config --list 
    - git config --global code.editor `-`

# Architecture
---
- _Commit_ : Snapshot the file
- _Working dir_:Git Initialized Folder
- _Staging area_:file to commit
- _git dir_:file eith .git & compress img

# Tracking
---
:: Save file.ext
- git init : To make repository
- git status : status of repository
- git add --a/./file : To stage all file/add
- git commit -m "String" : To commit with message
- git log : Return commit
- rm -rf .git : To delete the git-repository

# Cloning
---
- git clone <link to be clone> [name]

# File Status
---
addFile -> editFile -> stageFile.

# Ignore
---
- touch .gitignore : To Create Ignore folder for file
- Type file.ext inside .gitignore file
- dir/ : To ignore directory

# Difference
---
- git diff : Compare staging dir with working dir
- git diff --stage : compare staging dir with commit

# Stage
---
- git commit -a -m "String"
- To directly commit without staging it all

# Move Rename
---
- git rm _file.ext_ : To Remove file from Folder
- git rm --cached _file.ext_ : To Untrack file
- git mv _file.ext_ _reanme.ext_ : To Rename File

# Git Log
---
- git rm -rf .git : Git repo deleted
- git log -p / git log -np / 
- git log -stat : In short commit with details
- --pretty=short : all commit with detail
- --pretty=full :
- since=2.day : commit in two day's 
- --pretty=format : "%h --%an"
- git commit -amend : to make change

# UnStaging
---
- git restore --staged _file_ : To UnStage File
- git checkout --_file_ : To Restore file content
- git Checkout -f :

# Remote : Repository(GITHUB)
---
- git remote 
- git remote add origin username@github.com:url
- git remote -v :
- git push -v origin master : To push on site
+ SSH
    - run_mail / SSH_eval / tail 

# Alias
---
- git config --global alias.(short) [status]

# Branching 
---
- main : [master_Bramch]
- side : [side_Branch]
- git checkout -b _branch.name_ : To Create Branch
- git Checkout (master) : To switch master branch 
- git branch 


