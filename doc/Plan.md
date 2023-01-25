# Software Development Plan

## Phase 0: Requirements Specification
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.

    *   The goal is to create a Tic-Tac-Toe computer game that uses machine learning so the computer will never lose. The AI should either win or tie, never lose. Modes to be created for this console-based game are AI v AI, AI v Human, Human v AI, and Human v Human. The game should be colorful and look nice for the player.

*   [ ] Explain the problem this program aims to solve.
 
    *   The human player(s) should be able to play as either 'X' or 'O'. The CPU should use AI at some point because the client wants to use the buzzwords Machine Learning for popularity. 

    *   Describe what a *good* solution looks like.

    *   A good solution is one where the AI always wins or ties, the interface is simple and attractive, and the game doesn't crash or glitch in any way.

    *   List what you already know how to do.

    *   I already know how to edit code and check for possible errors

    *   Point out any challenges that you can foresee.

    *   I do not know how to properly put code into partitions that make human readability easier and I will need to learn how to do so.

*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.

    *   The output will be a Tic-Tac-Toe game board most of the time with open cells showing their corresponding identifying number, and taken cells showing whether it is an 'X' or 'O'. The program will use data from a tuple of the board to see which cells are open and if the game has been won and by which player, with output showing which player won a game (when applicable), and if an input is not accepted a clear message will show what input(s) should/can be given.

*   [ ] List the algorithms that will be used (but don't write them yet).

    *   Already included ********************


## Phase 1: Design
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.


    [ ] Modules I plan to make:
    *   boardAiTeam
        open_cells and first_open_cell functions I think were from the AI team, and the following functions: get_human_move, make_board, place, horizontal_winner, vertical_winner, diagonal_winner, pos_to_rowcol, rowcol_to_pos, and full.
    *   boardUiTeam (same as boardAiTeam but with Ui functions for open and first open cells)
        open_cells and first_open_cell functions I think were from the UI team, and the following functions: get_human_move, make_board, place, horizontal_winner, vertical_winner, diagonal_winner, pos_to_rowcol, rowcol_to_pos, and full.
    *   strategy
    	The following functions: strategy_dumb, strategy_random, strategy_oracle
    *   model
	The entire MODEL tuple
    *   graphics
        The following functions: logo, show, black, red, green, yellow, blue, magenta, cyan, white, color, home, and clear.  
    *   ttt.py
	Contains the remaining functions. These should include all of and only the following functions: player_select, winner, human_turn, cpu_turn, keep_playing, cpu_vs_cpu, cpu_vs_human, human_vs_human, human_vs_cpu, game, and if __name__ == '__main__'.


## Phase 2: Implementation
*(15% of your effort)*

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 3: Testing and Debugging
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 4: Deployment
*(5% of your effort)*

Deliver:

*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
