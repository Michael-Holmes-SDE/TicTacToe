# CS 1440 Assignment 1: Tic-Tac-Toe - Instructions

*   [How to Do This Assignment](#how-to-do-this-assignment)
    *   [Phase 0: Requirements Specification](#phase-0-requirements-specification)
    *   [Phase 1: Design](#phase-1-design)
    *   [Phase 2: Implementation](#phase-2-implementation)
    *   [Phase 3: Testing and Debugging](#phase-3-testing-and-debugging)
    *   [Phase 4: Deployment](#phase-4-deployment)
    *   [Phase 5: Maintenance](#phase-5-maintenance)
*   [What We Look for When Grading](#what we look for when grading)
*   [Important Things to Watch Out For](#important-things-to-watch-out-for)

## Previous Semester Statistics

**N/A**


## How to Do This Assignment

The flaw in this program is that the AI player can lose.  It is your job to find out why.  You will uncover the causes as you study the code.  If you think anything else looks wrong, **just leave it alone**.  I will make a public announcement if another serious issue is discovered.  Apart from the AI bug, I am confident this program works as intended.


### Phase 0: Requirements Specification
*(20% of your effort)*

**Important - do not change any code in this phase**

0.  Read the [Project Requirements](./Requirements.md) to orient yourself with the project.
1.  Read the *Software Development Plans* written by the previous teams to learn what they accomplished.
    *   [AI team's SDP](./AI_Team_Plan.md)
    *   [Game Engine team's SDP](./Engine_Team_Plan.md)
    *   You should understand these documents well enough to find your way around the source code.
    *   Pay special attention to the test cases they wrote.
2.  Run the program several times and try to identify which functions perform what actions.
3.  **Do not change the source code in this phase of the project!**
    *   You will edit code in **Phase 2: Implementation**.
    *   In this phase your task is to *draft* the plan that you will follow when you get there.
4.  Identify functions that were written under *faulty assumptions* and produce *incorrect results*.
    *   **Do not rewrite these functions now!**
    *   You will need to re-design these functions to fix the bug in the program.
    *   In this phase you need only to make a note about them.
5.  This project starts with **one** Python module that contains all of the code.
    *   At the end of the project you will have reorganized the code into **five** modules.
    *   The **five** modules will have these names and contents:
        1.  `ttt.py` - the main entry point of the program; ties everything together.
            *   Will consist of a few import statements and a `__name__ == '__main__'` block
            *   This module will not contain any function definitions (i.e. the `def` keyword does not appear in this module)
        2.  `interface.py` - code that prints pretty output and takes user input.
            *   This is the only module in the project where the `input()` function is called.
            *   Most (but not all) of the functions that call `print()` belong in this module.
        3.  `engine.py` - this module is for functions that drive the main game loop.
            *   There are four different game loops, each corresponding to a player selection mode (i.e. CPU vs. CPU, human vs. CPU, CPU vs. human, human vs. human)
            *   This code controls how players take turns.
            *   Functions in this module *may* output messages with the help of other functions defined in `interface.py`.
        4.  `ai.py` - holds the strategy functions which power the CPU opponent, and data they use.
        5.  `util.py` - miscellaneous, low-level utility functions.
            *   Functions belonging to this module are so simple that they don't require other imports (i.e. this module needs no `import` statements).
            *   These functions may need to be modified if the representation of the game board changes.
            *   These functions do not print anything, nor take input directly from the user.
6.  Take the **Starter Code Quiz** on Canvas.
    *   Do not worry if you can't answer all of the questions yet
    *   You can re-take the quiz as many times as you want before the assignment is due
7.  Fill out **Phase 0** in your own Plan.md; explain in your *own words* what program does, how it does it, and what changes you expect to make.
8.  Track your time in Signature.md.


### Phase 1: Design
*(30% of your effort)*

**Important - do not change any code in this phase**

0.  Locate functions that are redundant or serve no purpose in the program; these will be deleted in the next phase.  There are a few exceptions to this:
    *   Unused AI strategy functions *may* be kept for testing
    *   Unused color functions *may* be kept for future development
1.  Redesign faulty functions on paper; **don't rewrite the Python code yet**.
    *   In this phase sketch out improved versions in *pseudocode*.
    *   Walk through the pseudocode in your head, with a pad of paper or a whiteboard to convince yourself that your changes will work.
2.  Record the signatures and pseudocode of functions that you redesign in Plan.md.
    *   Do not paste Python code into Plan.md; when we want to see your code we will read the `.py` files.
3.  You may write *some* runnable Python code to test out your ideas.
    *   This is called *prototyping*, and is a normal part of the design process.
    *   Do not become too attached to your prototype!
    *   Be prepared to delete prototype code after this phase.
    *   It helps to *not* write prototype code in the same files as *real* code.
4.  Consider if any new test cases could be devised that ensure the new program will perform correctly.
5.  You should be able to get 100% on the **Starter Code Quiz** by now.
6.  Fill out **Phase 1** in Plan.md.
    *   This will be the longest portion of the document.
7.  Track your time in Signature.md.


### Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

0.  Reorganize the program's functions into the **five** modules described above.
    *   Now is the time to create four *new* Python modules in  `src/`
    *   Give the files these names (mind the capitalization!):
        1.  `interface.py`
        2.  `engine.py`
        3.  `ai.py`
        4.  `util.py`
1.  **Rewrite** faulty, incorrect functions so they perform correctly.
2.  **Delete** functions that do not have a use (subject to the exceptions outlined above).
3.  By the end of this phase the program is runnable.
    *   **Do not** move on if your program crashes regularly!
4.  Fill out **Phase 2** in Plan.md.
    *   As you work in this phase you may choose to deviate from the design you settled upon in the previous phase.  This is normal!
    *   Briefly explain what changed.
    *   Do not paste long passages of Python code in Plan.md.
    *   Your write-up for this phase may be very short.
5.  Track your time in Signature.md.


### Phase 3: Testing and Debugging
*(30% of your effort)*

0.  Run through the test cases suggested by the previous teams.
1.  Run through any new test cases that you devised.
2.  Fill out **Phase 3** in Plan.md.
    *   Describe the tests cases you ran.
    *   Make note of the commands that you ran and what happened in the program.
3.  If you found bugs in this phase, explain what was wrong and how you fixed it.
4.  Track your time in Signature.md.


### Phase 4: Deployment
*(5% of your effort)*

It is your responsibility to ensure that your program will work on your grader's computer.

*   Code that crashes and *cannot* be quickly fixed by the grader will receive **0 points** on the relevant portions of the rubric.
*   Code that crashes but *can* be quickly fixed by the grader (or crashes only *some* of the time) will receive, at most, **half-credit** on the relevant portions of the rubric.

The following procedure is the best way for you to know what it will be like when the grader runs your code:

0.  Review [How to Submit this Assignment](./How_To_Submit.md) and make sure that your submission is correct.
1.  Push your code to GitLab, then check that all of your files and commits appear there.
2.  Clone your project into a *different directory*, and re-run your test cases.


### Phase 5: Maintenance

0.  Review your Plan.md and Signature.md one last time.
1.  Fill out **Phase 5** in Plan.md by answering the questions.
2.  Make one final commit and push your **completed** Software Development Plan and Signature to GitLab.
3.  Make sure that you are happy with your **Starter Code Quiz** score.
4.  Respond to the **Assignment Reflection Survey** on Canvas.


## What We Look for When Grading

*   Quality documentation (35 points)
    *   Plan.md
        *   Each section filled out with a convincing level of detail
        *   No code is pasted from the source files
    *   Signature.md
        *   All development activities are accounted for
        *   Placeholder entries and TODO notes removed
*   Program behavior (15 points)
    *   AI opponent is unbeatable
        *   CPU vs. CPU matches always end in a draw
        *   Human vs. CPU matches end either in a draw or CPU victory
    *   Existing good behavior of program is preserved
        *   The user interface and appearance is unchanged from the starter code
        *   The Easter Egg is still accessible just as it was in the original program
    *   No new bugs are introduced
        *   Program doesn't crash
        *   Illegal user input is detected by the program and an appropriate error message is displayed
    *   All of your test cases work as expected
*   Code quality (20 points)
    *   Representation of the game board (1D or 2D) is consistent throughout the program
    *   Functions are organized into the correct modules
    *   Useless functions are removed
        *   Exceptions
            *   Unused AI strategy functions *may* be kept for testing
            *   Unused color functions *may* be kept for future development
        *   No duplicated or redundant code remains; each function is present in only one module
    *   No useless import statements, variables or constants
    *   Doc strings and comments match the code they describe


## Important Things to Watch Out For

0.  **100% penalty** your program imports any modules **except**:
    *   `random`
    *   `time`
    *   `typing`
    *   modules you wrote yourself
1.  **10 point penalty** an import statement fails due to misspelling or incorrect capitalization.
    *   **Windows users** make sure that the capitalization of your file names on GitLab matches your `import` statements!
2.  **10 point penalty** the program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration
3.  **10 point penalty** repository's URL on GitLab does not follow the naming convention
4.  **10 point penalty** repository is not a clone of the starter code
5.  **10 point penalty** required files or directories are missing, renamed or not in their expected locations
6.  **10 point penalty** `.gitignore` is missing or corrupt; forbidden files or directories are present in repository
