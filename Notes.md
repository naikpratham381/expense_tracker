# My Learning Notes — Expense Tracker Project

## Feature 1: Menu Loop
- Learned: while True loop, if/elif/else, input(), break
- while True = keeps repeating until we say stop
- break = the magic word that stops the loop
- input() always gives back text (a string), even if user types a number

## Git & GitHub (basics)
- Git = takes "photos" (commits) of my code so I can go back if I break something
- GitHub = online photo album website to store my Git photos
- Deploy = making your program usable by other people (not needed yet).

--------------------------------------------------------------------------

## Git Basics (Feature 1 commit)
- git init = start tracking this folder with Git (like opening a new photo album)
- git status = check which files are tracked/untracked/staged
- git add . = stage ALL files (get them ready for a photo)
- git commit -m "message" = take the actual photo, with a note describing what changed
- Each commit gets a unique ID (like 1a704bf) so I can find it later
- So far this is only saved on MY computer — GitHub will back it up online.
Quick recap of what you just learned
ConceptWhat it means
git init :Start tracking a folder
git add . :  Stage files (get them ready)
git commit -m "..."  :  Take a permanent snapshot with a note
git remote add origin <url>  :  Link your project to an online GitHub repo
git push  :  Upload your commits to GitHub

-----------------------------------------------------------------------------------------

 Key concepts you just learned

ConceptMeaning
def function_name():Create a reusable block of instructionsCalling a function function_name() : Actually running those instructions
float() : Convert text into a decimal numberDictionary {...}Store labeled data (key-value pairs).
append()Add an item to the end of a list
## Feature 2: Add Expense
- Learned: functions (def), calling a function, float(), dictionaries, .append()
- def function_name(): = create a reusable block of code (like teaching a robot a command)
- Calling it (function_name()) = actually running that code
- float(input(...)) = convert typed text into a decimal number
- Dictionary {"key": value} = labeled storage, easier than remembering list positions
- expenses.append(expense) = add a new dictionary into our expenses list

-----------------------------------------------------------------------------------------

## Feature 3: View Expenses
- Learned: len(), return, enumerate(), f-strings, dictionary['key']
- len(expenses) = counts how many items are in the list
- return = exits a function early (like break, but for functions)
- enumerate(list, start=1) = loop through items WITH a running count attached
- f-strings f"{variable}" = insert variables directly into printed text, cleaner than concatenation
- expense['amount'] = grab a specific value out of a dictionary using its key/label

-------------------------------------------------------------------------------------------
## Feature 4: Total Spending
- Learned: accumulator pattern
- total = 0 → starts a "piggy bank" variable at zero
- total = total + expense['amount'] → adds each expense's amount into the running total, one loop at a time
- += is shorthand for "add to current value" (total += x same as total = total + x)
- This pattern (start at 0, add in a loop) is used everywhere in programming — counting, summing, etc.

-------------------------------------------------------------------------------------------

## Feature 5: Filter by Category
- Learned: flag variables, .lower(), not
- found_any = False → a "light switch" variable that starts off, flips on only if we find a match
- .lower() → converts text to lowercase so "Food" and "food" are treated as the same
- not found_any → checks if the flag is still False after the loop (nothing was found)
- Also updated the menu: added option 4 (Filter), shifted Exit to option 5

-------------------------------------------------------------------------------------------

## Feature 6: Delete Expense
- Learned: reusing functions, .isdigit(), input validation, zero-based indexing, .pop()
- Reused view_expenses() inside delete_expense() instead of rewriting the same display logic
- .isdigit() checks if user input is only numbers (protects against crashes from bad input)
- Python lists start counting at 0, so we subtract 1 from the human-friendly number shown on screen
- expenses.pop(index) removes an item from the list AND gives it back to us (unlike .append which only adds)
- Always validate user input before using it — never trust that the user typed what you expect

-----------------------------------------------------------------------------------------

## Feature 7: Save to File
- Learned: import, csv module, os module, open(), with statement, DictWriter
- import csv / import os = bring in built-in toolboxes for extra functionality
- os.makedirs("data", exist_ok=True) = create a folder safely, no crash if it already exists
- open(path, mode="w") = open/create a file for writing (overwrites existing content)
- with ... as file: = context manager, automatically closes the file safely when done
- csv.DictWriter = converts a list of dictionaries into CSV rows automatically
- writer.writeheader() = writes column titles
- writer.writerows(expenses) = writes every dictionary as a row
- Called save_expenses() after every add/delete so the file always matches memory
- Note: expenses.csv now has data, but restarting the program still starts with an empty list in memory — Feature 8 (Load from File) will fix that.

---------------------------------------------------------------------------------------
## Feature 8: Load from File (Phase 1 complete! 🎉)
- Learned: os.path.exists(), read mode, DictReader, top-level code execution
- os.path.exists(path) = check if a file exists before trying to open it (avoids crashes)
- mode="r" = open a file for READING (mode="w" was for writing)
- csv.DictReader = reads CSV rows and turns them back into dictionaries automatically
- Important: CSV always stores everything as TEXT, even numbers — had to convert amount back with float()
- load_expenses() called once at the top level (outside any function/loop) so it runs immediately when the program starts
- Now expenses truly persist between program runs — Phase 1 (command-line brain) is done!

--------------------------------------------------------------------------------------------

## Phase 2 Started: Flask Website
- Installed Flask using: py -m pip install flask
- Created app.py (separate from main.py) as the website version
- Learned: routes, decorators, render_template, templates folder
- @app.route("/") = decorator that connects a URL address to a Python function
- render_template("index.html") = tells Flask to find and display an HTML file from the templates folder
- if __name__ == "__main__": = only run this code if the file is run directly (not imported)
- app.run(debug=True) = starts the local web server, auto-restarts on save, shows helpful errors
- Ran locally at http://127.0.0.1:5000 — successfully saw the homepage! 

-------------------------------------------------------------------------

## Phase 2 - Feature: Add Expense (Web Form)
- Learned: HTML forms, GET vs POST, request.form, redirect + url_for
- GET request = "show me a page" (visiting a URL)
- POST request = "here's data, process it" (submitting a form)
- request.form["amount"] = grabs the value from an HTML input with name="amount"
- redirect(url_for("home")) = sends browser to another page after processing (prevents duplicate submission on refresh)
- Reused the same save_expenses()/expenses.append() logic from main.py — backend logic didn't need to change!
- HTML <input name="..."> must match exactly what request.form["..."] looks for

-----------------------------------------------------------------------

## Phase 2 - Feature: View Expenses (Web Page)
- Learned: Jinja2 templating basics
- render_template(file, expenses=expenses) = passes Python data into the HTML template
- {% if %} {% else %} {% endif %} = Jinja2's version of if/else, written inside HTML
- {% for %} {% endfor %} = Jinja2's version of a for loop, written inside HTML (needs explicit endfor, unlike Python's indentation)
- {{ variable }} = displays a value inside HTML (like print())
- expenses|length = Jinja2's version of len()
- loop.index = automatic counter Jinja2 provides inside a for-loop, starts at 1
- expense.amount (dot notation) = access dictionary values inside templates, instead of expense['amount']

-------------------------------------------------------------------------

## Phase 2 - Feature: Total Spending (Web Page)
- Reused the exact same accumulator pattern from main.py — no new concepts needed!
- Calculated total in Python (app.py), then passed it to the template with render_template("total_spending.html", total=total)
- Displayed with {{ total }} in HTML, same Jinja2 syntax as before
- Key lesson: once you learn a pattern well (accumulator, templating), it works everywhere — command-line or web

------------------------------------------------------------------

## Phase 2 - Feature: Filter by Category (Web Page)
- Learned: query parameters, request.args.get(), GET forms
- Query parameters = small data sent through the URL itself (e.g. ?category=Food)
- request.args.get("category", "") = reads a query parameter safely, with a default fallback
- method="GET" on a form = puts form data into the URL — good for searches/filters (shareable, bookmarkable)
- Passed both filtered results AND search_category to the template, so the input box remembers the last search
- Reused the same lowercase-comparison filtering logic from main.py

----------------------------------------------------------------

## Phase 2 - Feature: Delete Expense (Web Page)
- Learned: dynamic route parameters, function parameters, loop.index vs loop.index0
- <int:index> in a route = captures a changing number directly from the URL, auto-validates it's an integer
- The captured value becomes a parameter of the function: def delete_expense(index):
- loop.index = 1-based counter (for display), loop.index0 = 0-based counter (matches real list positions)
- Used loop.index0