## 📓 Progress Diary (CLI App)

This is a simple command-line diary application that allows users to log their daily programming progress, store entries in a database, and retrieve them at any time. It’s a minimalistic productivity tool built in Python with a focus on usability and structured data storage.

---

### 🧠 Features

- 📝 **Add new diary entries**
  - Prompts users to enter what they’ve learned and the date
  - Saves entries into a database table for persistence

- 📂 **View saved entries**
  - Displays all previously added diary entries, formatted by date

- 🔁 **Menu loop**
  - After each action, the app returns the user to the main menu (excluding the welcome message after the first time)

- ❌ **Exit cleanly**
  - Allows the user to quit at any time with the exit option

---

### 🧪 Sample Flow

```text
Welcome to the programming diary!

Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: 1

What have you learned today? Today I learned how to start coding with Python and SQL.
Enter the date: 01-01-2020

Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: 2

01-01-2020
Today I learned how to start coding with Python and SQL.

Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: 3
```

### 📦 Tech Stack
 - Python – Application logic and user interaction
 - SQLite (or another database) – Data persistence layer

### 🎯 Key Learnings
 - Building simple CLI applications that interact with users via menus
 - Capturing and validating user input
 - Persisting data using a database
 - Implementing clean control flow and app structure

This project is ideal as a foundational exercise for learning how to combine Python, user input handling, and basic database operations.

