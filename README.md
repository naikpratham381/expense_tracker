# Personal Expense Tracker

A Python-based expense tracker built as a learning project — first as a command-line application, then expanded into a full Flask website.

## Features

- Add expenses with amount, category, and description
- View all expenses
- Calculate total spending
- Filter expenses by category
- Delete expenses
- Persistent storage using CSV files
- Available as both a command-line app and a web app

## Tech Stack

- **Language:** Python 3
- **Web Framework:** Flask
- **Templating:** Jinja2
- **Storage:** CSV file
- **Frontend:** HTML, CSS

## Project Structure
    expense_tracker/
│
├── main.py              # Command-line version of the tracker
├── app.py                # Flask web version of the tracker
├── templates/             # HTML pages (Flask/Jinja2)
│   ├── index.html
│   ├── add_expense.html
│   ├── view_expenses.html
│   ├── total_spending.html
│   └── filter.html
├── static/
│   └── style.css          # Website styling
├── data/
│   └── expenses.csv       # Saved expense data
└── README.md

## How to Run

### Command-line version

```bash
py main.py
```

### Web version

```bash
py app.py
```

Then open your browser to `http://127.0.0.1:5000`

## What I Learned

This project was built step-by-step to practice core Python concepts:
- Loops, conditionals, and functions
- Lists and dictionaries
- File handling (reading/writing CSV)
- Web development basics with Flask (routes, forms, templating)
- Version control with Git and GitHub

## Author

Built by [Pratham D Naik] as a beginner Python learning project.