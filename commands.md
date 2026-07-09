# Command Reference — Expense Tracker Project

A log of every terminal command used while building this project, for future reference.

## Checking Python & Git are installed

```bash
py --version
git --version
```

## Navigating folders

```bash
cd Documents              # move into Documents folder
cd expense_tracker         # move into project folder
cd                         # show current folder path
dir                        # list files/folders in current location
```

## Creating the project folder

```bash
mkdir expense_tracker
cd expense_tracker
code .                     # open this folder in VS Code
```

## Running the project

```bash
py main.py                 # run the command-line version
py app.py                  # run the Flask website version
```

## Installing packages

```bash
py -m pip install flask
```

## Git setup (one-time only)

```bash
git init
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Connecting to GitHub (one-time only)

```bash
git remote add origin https://github.com/naikpratham381/expense_tracker.git
git branch -M main
git push -u origin main
```

## The regular save routine (used after every feature)

```bash
git status                 # see what changed
git add .                  # stage all changes
git commit -m "describe what changed here"
git push                   # upload to GitHub
```