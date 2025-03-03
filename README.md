# Sudoku Solver 
## Project Overview
This project implements a Sudoku solver using the backtracking algorithm. The program solves a 9x9 Sudoku puzzle by filling in the empty cells while ensuring that the rules of Sudoku are respected. The solver works recursively, trying different numbers in empty cells and backtracking when a number does not lead to a valid solution.

## Features
Solves a Sudoku puzzle by filling missing values.

Uses recursion and backtracking algorithm to find solutions.

Checks for validity in rows, columns, and 3x3 sub-grids.


## Input 
the Sudoku puzzle in the console (a 9x9 grid where empty cells are represented by 0).

### Input Format
The program expects a 9x9 grid input, where 0 represents an empty cell. Here's an example:


Copy

5 3 0 0 7 0 0 0 0

6 0 0 1 9 5 0 0 0

0 9 8 0 0 0 0 6 0

8 0 0 0 6 0 0 0 3

4 0 0 8 0 3 0 0 1

7 0 0 0 2 0 0 0 6

0 6 0 0 0 0 2 8 0

0 0 0 4 1 9 0 0 5

0 0 0 0 8 0 0 7 9

## Output
Once the puzzle is solved, the solution will be printed on the console.

## Code Explanation
display(int[][] board): Prints the current state of the Sudoku board.

solveSudoku(int[][] board, int i, int j): Recursively solves the Sudoku puzzle.

isValid(int[][] board, int x, int y, int val): Checks if a number can be placed at a given position without violating the Sudoku rules.

## Time and Space Complexity
Time Complexity: O(9^(n*n)), where n is the size of the grid (9x9). This arises from the recursive nature of the algorithm, where we try different numbers for each empty cell.

Space Complexity: O(n*n), due to the storage of the Sudoku grid.
