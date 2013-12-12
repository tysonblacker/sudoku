Sudoku Solver
=============

A simple Sudoku Solver that takes a puzzle and attempts to solve it. 

The first stage is to try and solve it with some logic. 
It attempts to:
- Find the answer to squares by finding if there is only one available solution. 
- Find if there is only one valid available answer to a row or column.
- Perform a brute force counter that will find the solultion or declare the the puzzle is unsolvable. Inspiration for the brute force solver come from a MatLab alogrithm that is now lost.

## Requirements

The required python modules are:
- numpy
- sys
- getop
- nosetest is used for testing

PYTHONPATH also needs configuring

    export PYTHONPATH=$PYTHONPATH:.

## Usage

    bin/sksolver.py -i <filename>

eg.

    bin/skolver.py -i bin/test_file

### File format
A file is used as the input, it is an a 9x9 array. Number 1-9 represent the 
sudoku starting points and 0s are for the blank squares.

    $ cat test_file
    250147096
    400050002
    100209005
    002070600
    500413007
    000000000
    620000079
    900080004
    007000500


## TO-DO List
There are a few things that could be updated to make the code work better:
- Generally make the code work more efficiently; "solos" and "simple_solver" are almost the same.
- The interface for passing the sudoku board
- Update some the names used; solos and solos9 are not great function names.
- Use a 2D array instead of a 1D array
- Add some debug logging
- Display the board with lines
  
