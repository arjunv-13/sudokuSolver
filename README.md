# Sudoku Solver

## Overview
This project intends to demonstrate how recursive backtracking works via the example of a sudoku solver. 

It fetches a valid sudoku puzzle, solves it without delay, and then does it slowly with visual aids in order to show a user how a recursive backtracking algorithm works.

This project helped me learn more about recursion and the importance of optimizing algorithms when that function is repeatedly called called a high number of times.

## Usage

To use this program, run game.py. A pygame window will appear with a valid Sudoku puzzle. 

Then hit the spacebar to begin the solving visualization

## Components

### generate

This function fetches a valid sudoku puzzle. It makes use of a free API online and allows various difficulties.

### game

This implements the Pygame window and the slow solve.

First, a sudoku is fetched.

Then that sudoku is solved without delay using recursive backtracking to be stored as a comparison later.

Next, a sudoku outline board is generated with the input board as well.

Then when the spacebar is hit, the Sudoku is solved with a delay of 0.5s between each number updating. Green numbers that are correct guesses, red numbers are for incorrect guesses, and black numbers are input, static numbers.

However, the visualizer algorithm does not have access to the correct guesses besides to generate their color. Thus, it is solving it in the same way that it was originally solved

### solver

This contains the recursive backtracking algorithm to solve a Sudoku puzzle.

It starts from the top left and works its way across to the bottom right by successively guessing integers and seeing whether they lead to a viable trail. If a number fails, that search ends and it works backward to the last point where valid guesses are still possible.

This continues until we reach the bottom right of the board where the puzzle is complete.

## Future Work

In the future, I hope to add interactivity by allowing the user to input guesses and check their guesse. Additionally, a hint feature along with the "give up" full solve that currently exists are also features I am looking to add.

## Thank You

Thank you for reading this! I hope this was interesting and informative.