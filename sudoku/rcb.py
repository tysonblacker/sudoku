import numpy as np


def get_column(position, board):
    """
    Gets a column from the sudoku board, from whatever position is given
    """
    values = []
    offset = position % 9
    for i in range(9):
        value = board[i * 9 + offset]
        if value != 0:
            values.append(value)
    return values


def get_row(position, board):
    """
    Gets a row from the sudoku board, from whatever position is given.
    """
    values = []
    offset = position // 9
    for i in range(9):
        value = board[offset * 9 + i]
        if value != 0:
            values.append(value)
    return values


def get_box(position, board):
    """
    Gets a square from the sudoku board, from whatever position is given.
    """
    values = []
    boxr = (position // 9) // 3
    boxc = (position % 9) // 3

    for i in range(3):
        for j in range(3):
            # terrible equation to get the box out
            value = board[((boxr * 3 + i) * 9) + (3 * boxc) + j]
            if value != 0:
                values.append(value)
    return values


def valid_row(position, board):
    """
    Validates the row, makes sure there are no duplicates.
    """
    row = get_row(position, board)
    return len(row) == len(set(row))


def valid_column(position, board):
    """
    Validates the column, makes sure there are no duplicates.
    """
    column = get_column(position, board)
    return len(column) == len(set(column))


def valid_box(position, board):
    """
    Validates the box, makes sure there are no duplicates.
    """
    box = get_box(position, board)
    return len(box) == len(set(box))


def valid_position(position, board):
    """
    Validates the position, makes sure there are no duplicates.
    """
    if not valid_row(position, board):
        return False
    if not valid_column(position, board):
        return False
    if not valid_box(position, board):
        return False
    return True


def get_nots(position, board):
    """
    Get all the values already used for a position
    """
    row = get_row(position, board)
    column = get_column(position, board)
    box = get_box(position, board)
    nots = row + column + box
    return nots


def get_possibles(position, board):
    """
    Inverse of the nots with the position value added
    """
    possibles = []
    if board[position] != 0:
        possibles.append(board[position])
    else:
        nots = get_nots(position, board)
        npnots = np.unique(nots)
        for i in range(1, 10):
            if i not in npnots:
                possibles.append(i)
    return possibles


def update_possible(position, board):
    """
    Updates a position in the board if there is only one valid option
    When solved, the position and value are printed.
    """
    possible = get_possibles(position, board)
    if len(possible) == 1:
        board[position] = possible[0]
        print "Simple - Position: ", position, " Value: ", possible[0]
        return True
    else:
        return False


def get_possibles_board(board):
    """
    Creates a board of possible values for every position in the board
    This is like the pencil marks in some Sudoku applications.
    """
    possibles_board = []
    for position in range(81):
        possibles_board.append(get_possibles(position, board))

    return possibles_board


# A small utility to flatten a list
def plus(a, b): return a + b


def get_solos(rcb):
    """
    Returns a list of positions and values that can only be one value from
    from a collection of possibles.
    """
    flat = reduce(plus, rcb)
    solos = []
    positions = {}

    for j in range(1, 10):
        # if there is only one value for j in a row, column and block for a
        # position then it must that value.
        if flat.count(j) == 1:
            solos.append(j)

    for solo in solos:
        # finds the position for the solo values
        for position in range(9):
            if rcb[position].count(solo) == 1 and len(rcb[position]) > 1:
                positions[position] = solo
    return positions


# Prints the board in a nice shape used for debugging purposes
def rcb_print_board(board):
    m = np.array(board)
    m9x9 = m.reshape((9, 9))
    print m9x9


def solos9(board):
    """
    If there is only one value left for a position it is set.
    eg. If there are already 2 columns in a box that can't be used for a value
    and if there 2 positions already filled in the remaining column then we
    know that it can be filled in.

    ...|...|...
    2..|...|...
    3..|...|...
    ---+---+---
    .1.|...|...
    ...|...|...
    ...|...|...
    ---+---+---
    ...|...|...
    ..1|...|...
    ...|...|...

    Position 0 could be [1,4,5,6,7,8,9]
    but the only position that can contain 1 is 0 in the first 3x3 box

    """
    for row_start in range(0, 81, 9):
        solos_rcb = get_solos(
                get_row(row_start, get_possibles_board(board)))
        update_solos9(row_start, solos_rcb, "is_row", board)

    for column_start in range(9):
        solos_rcb = get_solos(
                get_column(column_start, get_possibles_board(board)))
        update_solos9(column_start, solos_rcb, "is_column", board)

    for box_startr in range(0, 9, 27):
        for box_startc in range(0, 9, 3):
            position = box_startr + box_startc
            solos_rcb = get_solos(
                get_box(position, get_possibles_board(board)))
            update_solos9(position, solos_rcb, "is_box", board)


def update_solos9(position, solos_rcb, nine_type, board):
    """
    Updates the metrix from the values retrieved from solos.
    """
    col = position % 9
    row = position / 9

    for solo_rcb in solos_rcb:
        if nine_type == "is_row":
            solo_position = row * 9 + solo_rcb
        if nine_type == "is_column":
            solo_position = solo_rcb * 9 + col
        if nine_type == "is_box":
            boxr = (position / 9) / 3
            boxc = (position % 9) / 3
            solo_position = ((boxr * 3 + solo_rcb / 3) * 9) + \
                    (3 * boxc) + solo_rcb % 3

        print "Solo - Postition: ", solo_position, " Value: ", \
                    solos_rcb[solo_rcb]
        board[solo_position] = solos_rcb[solo_rcb]
