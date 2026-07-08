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