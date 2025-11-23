# Task Tracker: CLI TODO App

**Task tracker** is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

---

## ✨ Usage
```bash
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

## ⚡ Installation

You can install Task Tracker (CLI) directly from GitHub:

```bash
pip install git+https://github.com/US-Backend-Challenges/Task-Tracker.git
```

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it.