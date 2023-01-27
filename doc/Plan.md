# Software Development Plan

## Phase 0: Requirements Specification
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Re-write the instructions in your own words.

    *   The goal is to create a Tic-Tac-Toe computer game that uses machine learning so the computer will never lose. The AI should either win or tie, never lose. Modes to be created for this console-based game are AI v AI, AI v Human, Human v AI, and Human v Human. The game should be colorful and look nice for the player.

*   [X] Explain the problem this program aims to solve.
 
    *   The human player(s) should be able to play as either 'X' or 'O'. The CPU should use AI at some point because the client wants to use the buzzwords Machine Learning for popularity. 

    *   A good solution is one where the AI always wins or ties against a human player, and always ties when against itself. The interface would be simple and attractive, and the game doesn't crash or glitch in any way.

    *   I already know how to edit code and check for possible errors, and I know a bit about planning programs too.

    *   Challenges I can foresee are: I do not know how to properly put code into partitions that make human readability easier and I will need to learn how to do so. I am also not sure if simply trying each team's separate open-cells and first-open-cell functions will be enough to fix the program: if it doesn't, I will probably have a difficult time determining where and why the program is going wrong.

*   [X] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
	
    *	The input will be numbers inputted in the command line, with 0, 1, 2, and 3 being entered at the beginning to choose the game mode and 1-9 throughout to choose which cell to mark. 'q' will always be an available input and will exit a current game if in one and if on the menu it will close the program.	
    *   The output will be a Tic-Tac-Toe game board most of the time with open cells showing their corresponding identifying number, and taken cells showing whether it is an 'X' or 'O'. The program will use data from a tuple of the board to see which cells are open and if the game has been won and by which player, with output showing which player won a game (when applicable), and if an input is not accepted a clear message will show what input(s) should/can be given.

*   [X] List the algorithms that will be used (but don't write them yet).

    *   Algorithms included in source code


## Phase 1: Design
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [X] Function signatures that include:

    *   All functions included in source code

*   [X] Pseudocode that captures how each function works.
    
    *   Pseudocode and original code included in source code and in the AI Team's plan and the Engine Team's plan


    [X] Modules I plan to make:
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


    *   **In the end, the two board modules were integrated, with the Ui team's functions being used**


## Phase 2: Implementation
*(15% of your effort)*

Deliver:

*   [X] More or less working code.
*   [X] Note any relevant and interesting events that happened while you wrote the code.
    *   Many things didn't go according to plan. Once I'd separated the program into modules there were a miriad of problems with import statements not being in the right modules, with cyclical imports which I didn't even know existed, with a function trying to access a value in a tuple that didn't actually exist, and the open_cells function that kept returning None (more on that below).
    *   (IDK) An interesting thing I figured out was that the open-cells function (from the UI team, which I had decided on using) was returning None, so my thoughts were the Oracle strategy thought every space was blank and therefore did the default option of choosing a random cell. However, when I ran the code in a human vs human game I was not able to select a cell that had already been selected. I fixed this by creating nested for loops that appended each integer in the board to a tuple and returned that tuple as an identifier of all open cells.
    *   In the strategy-oracle function I found it would always choose a random open cell because it always thought there was no "X" on the board (It was checking tuples for "X" instead of the values inside the tuples) so I did the same thing I did for the open-cells function, creating a nested for loop to check every value in the two-dimensional tuple separately.
    *   Also in the strategy-oracle function I created a list where I appended each value on the board to using nested for-loops, and used a separate nested for-loop to check if the tupled version of that list was the same as the tuple in the model and returned the integer value of the first for loops iteration plus 1 so the 'AI' would know which move to make based on the BOARD tuple. 

## Phase 3: Testing and Debugging
*(30% of your effort)*

Deliver:

*   [X] A set of test cases that you have personally run on your computer.
    *   A bug I found was that the AI seemed to choose a random cell instead of the one outlined in the AI team's test cases (it turns out it was actually random). This was fixed by modifying the open-cells and strategy-oracle functions as stated above in Phase 2: Implementation by temporarily switching tuples between one and two dimensions
    *   The main test case I used was the easter egg, where it runs dozens of automated AI vs AI games quickly and did a keyword search for win I found there were none, meaning that each game was a draw just like it's supposed to be. This test can be done by typing without apostrophes 'joshua' into the prompt from the main screen of the game(the one with the tic-tac-toe logo)
    *   I used the set of test cases created by the AI team. For the sake of space I will only include the test cases I used:

    *  **A Human playing as 'X'**:

	1. Open with 1
	2. O plays 5
	3. Respond with 7
	4. O plays 4
	5. Respond with 6
	6. O plays 2
	7. Respond with 8
	8. O plays 9
	9. Respond with 3, drawing the game

    *  **A Human playing as 'X'**:

	1. Open with 2
	2. O plays 1
	3. Respond with 5
	4. O plays 8
	5. Respond with 7
	6. O plays 3
	7. Respond with 6
	8. O plays 4
	9. Respond with 9, drawing the game

    *  **A Human playing as 'X'**:

	1. Open with 3
	2. O plays 5
	3. Respond with 9
	4. O plays 6
	5. Respond with 4
	6. O plays 1
	7. Respond with 8
	8. O plays 7
	9. Respond with 2, drawing the game


    * **A Human playing as 'O'**:

	1. X opens with 1
	2. Respond with 3
	3. X plays 4
	4. Respond with 7
	5. X plays 5
	6. Respond with 6
	7. X plays 9, winning the game
	
    * **A Human playing as 'O'**:

	1. X opens with 2
	2. Respond with 8
	3. X plays 1
	4. Respond with 3
	5. X plays 7
	6. Respond with 4
	7. X plays 5
	8. Respond with 9
	9. X plays 6, drawing the game

    * **A Human playing as 'O'**:

	1. X opens with 3
	2. Respond with 4
	3. X plays 1
	4. Respond with 2
	5. X plays 5
	6. Respond with 7
	7. X plays 9, winning the game


## Phase 4: Deployment
*(5% of your effort)*

Deliver:

*   [X] Your repository is pushed to GitLab.
*   [X] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [X] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [X] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   I'm not entirely sure how the graphics of the program work and why
        *   If a bug is reported in a few months, how long would it take you to find the cause?
        *   Depending on the bug, anywhere between ten minutes to two hours
    *   Will your documentation make sense to...
        *   My documentation will make sense to most people
        *   My documentation will make sense to me in six months
    *   How easy will it be to add a new feature to this program in a year?
        *   It should be easy to add any new features to this program
    *   Will your program continue to work after upgrading...
        * This program will continue to work after upgrading because the program can work on all computer hardware, operating system, and most likely the next version of Python
*   [X] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [X] Respond to the **Assignment Reflection Survey** on Canvas.
