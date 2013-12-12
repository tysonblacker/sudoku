import rcb as rcb
import numpy as np


def get_solved_positions(board):
    """
    Creates a list of solved positions from the sudoku board.
    It is used initially so that the positions are are ready solved are
    skipped. This happens twice, on start up and between the simple
    solve and the brute force.
    """
    solved_positions = []
    for i in range(81):
        if board[i] != 0:
            solved_positions.append(i)
    return solved_positions


def check_valid_board(board):
    """
    Performs a simple check to see if at least on the face of it the sudoku
    can be solved or at there are no simple errors.
    """
    if len(board) != 81:
        return False
    for position in range(81):
        if not rcb.valid_position(position, board):
            return False
    return True


def simple_solve(board):
    """
    Gets all the positions and values where there only one option left for a
    value in a rcb (row, column, box)

      .23|...|...
      456|...|...
      789|...|...
      ---+---+---
      ...|...|..6
      ...|...|..3
      ...|...|..2
      ---+---+-----
      ...|...|7..
      ...|...|.8.
      564|9..|...

    In the example position [0] can only be 1
    also, position 80 can only be 1

    """

    for position in range(81):
        if board[position] == 0:
            rcb.update_possible(position, board)


def brute_solve(board):
    """
    This is a basic counter algorithm to solve the sudoku. It is basically a
    counter that set a position value and tests it. If the current position
    gets to nine it is reset to 0 and the position pointer is decremented.
    If the pointer gets to 81 then the sudoku is solved, if it get to 0 then
    the sudoku has no solution.
    """
    orginal_positions = get_solved_positions(board)
    position = 0

    while position < 81 and position >= 0:
        if position in orginal_positions:
            # if the position has already been solved, skip it
            position = position + 1
            continue
        # increment the value at the current position
        value = board[position] + 1
        while value < 10:   # Test from 1 to 9
            board[position] = value
            if rcb.valid_position(position, board):
                position = position + 1
                # if the position is valid, increment the position and
                # break the while loop
                break
            else:
                if value == 9:
                    while position in orginal_positions or \
                          board[position] == 9:
                        # decrement the position pointer while the position
                        # value is "9" if the value was not already determined
                        # then set it to "0"
                        if (position) not in orginal_positions:
                            board[position] = 0
                        position = position - 1
                    # make sure that we break out the the value while loop
                    # by setting value to 20. Not sure is this is required
                    # with the break.
                    value = 20
                    break
                else:
                    value = value + 1
                    break
    if position == -1:
        return False
    else:
        return True


def print_board(board):
    """
        Uses numpy as a quick print out method
    """
    m = np.array(board)
    m9x9 = m.reshape((9, 9))
    print m9x9


def solve(board):
    solved = False
    if not check_valid_board(board):
        print "This board has errors."

    start_board = []
    while start_board != board:
        start_board = list(board)
        simple_solve(board)
        rcb.solos9(board)

    if board.count(0) > 0:
        print "Now using brute solver starting from ..."
        print_board(board)
        solved = brute_solve(board)
    else:
        solved = True

    if not solved:
        print "No solution found, invalid sudoku!"
    else:
        print "The solution is ..."
        print_board(board)
    return solved
