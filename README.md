# Rock, Paper, Scissors, LEARN!

## Goals

This project is designed to be a gentle, and kid friendly, introduction to Python programming. Getting a working program happening quickly is important, so this project creates a working Rock, Paper, Scissors game in the very first lesson! From there, we improve our game by adding features one at a time. This allows us to add features along the way.

I recommend using Pycharm when working through these lessons, or any IDE of your choice really. You can start each lesson by downloading that lesson's template and replacing all instances of "your_code" with the code you wrote to solve each problem presented in the comments. A more engaging way is to start with the 1_basic_template.py and look for what is new in each template, then add it to your 1 file that grows and changes as you work through the lessons.

## Audience

These lessons assume that some basic coding fundmentals are known. Not many fundmentals are required, but a basic knowledge of what coding is and familiarity with concepts like variables, loops, and conditionals.

## Lessons

### 1. Basic Rock Paper Scissors
This is the starting lesson. It covers a lot of ground without a lot of detail. The skeleton of the game is laid out for you, but you have to get each piece working. This introduces the most concepts in a single lesson of any lesson.

Lesson: 1_basic_template.py

Answer Key: 1_basic.py

Covers:
- Coding fundamentals!
- `print` statements, and sending information to the console.
- Getting user `input` from the console.
- Assigning values to variables.
- Creating conditionals in the form of if statements.
- Writing and calling functions.
- `return` values from functions.

### 2. Add Quit
This adds a way for the user to exit the program. After the size and complexity of the first lesson, this is a "quick win" that modifies existing code to improve our game. This is an introduction to modifying existing code bases and learning how to improve something without breaking it.

Lesson: 2_add_quit_template.py

Answer Key: 2_add_quit.py

Covers:
- Modify existing code.
- Modifying conditionals in the form of if elif else statements.
- using elif for program flow.

### 3. Add Score
Keeping score is a common acitivity in games, let's add some score tracking to our game, and make sure it is communicated to the human player.

Lesson: 3_add_score_template.py

Answer Key: 3_score_quit.py

Covers:
- Write a function that accepts arguments, and uses those arguments.
- Ordering of arguments is important!
- f-strings (Format Strings) and printing variable values out to the console.
- Incrementing integer values within the code.

### 4. Add Dictionary
Introduces dictionaries and uses them to simplify some of the code we wrote previously. This introduces the concept of using data structures to make coding tasks easier.

Lesson: 4_add_dictionary_template.py

Answer Key: 4_add_dictionary.py

Covers:
- Creating a dictionary and assigning that dictionary to a variable.
- Getting a value out of a dictionary using a key.
- Storing a value from a dictionary into a separate variable.
- Refactoring parts of code that following sections rely on, preferably without breaking anything!

### 5. Simpler Winner Logic
Continuing our work on refactoring our game to make it easier to read, write, and maintain, we are going to take the extensive winner logic and use our newfound skill with dictionaries to make the code smaller and more powerful.

Lesson: 5_simpler_winner_logic_template.py

Answer Key: 5_simpler_winner_logic.py

Covers:
- Creating a dictionary as a complex data structure (a dictionary that has lists for values).
- Planning for the future in your code.
- Writing conditionals that directly access dictionary values.
- The mighty power of the Python `in` comparator.
- More practice refactoring code.
