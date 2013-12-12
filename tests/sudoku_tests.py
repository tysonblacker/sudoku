import nose.tools as nose
import sudoku.rcb as rcb
import sudoku.sudoku as suku


long_board = [0,6,0,3,0,0,8,0,4,
               5,3,7,0,9,0,0,0,0,
               0,4,0,0,0,6,3,0,7,
               0,9,0,0,5,1,2,3,8,
               0,0,0,0,0,0,0,0,0,
               7,1,3,6,2,0,0,4,0,
               3,0,6,4,0,0,0,1,0,
               0,0,0,0,6,0,5,2,3,
               1,0,2,0,0,9,0,8,0,0]

short_board = [6,0,3,0,0,8,0,4,
               5,3,7,0,9,0,0,0,0,
               0,4,0,0,0,6,3,0,7,
               0,9,0,0,5,1,2,3,8,
               0,0,0,0,0,0,0,0,0,
               7,1,3,6,2,0,0,4,0,
               3,0,6,4,0,0,0,1,0,
               0,0,0,0,6,0,5,2,3,
               1,0,2,0,0,9,0,8,0]

easy_board = [0,6,0,3,0,0,8,0,4,
               5,3,7,0,9,0,0,0,0,
               0,4,0,0,0,6,3,0,7,
               0,9,0,0,5,1,2,3,8,
               0,0,0,0,0,0,0,0,0,
               7,1,3,6,2,0,0,4,0,
               3,0,6,4,0,0,0,1,0,
               0,0,0,0,6,0,5,2,3,
               1,0,2,0,0,9,0,8,0]

medium_board = [2,5,0,1,4,7,0,9,6,
                4,0,0,0,5,0,0,0,2,
                1,0,0,2,0,9,0,0,5,
                0,0,2,0,7,0,6,0,0,
                5,0,0,4,1,3,0,0,7,
                0,0,0,0,0,0,0,0,0,
                6,2,0,0,0,0,0,7,9,
                9,0,0,0,8,0,0,0,4,
                0,0,7,0,0,0,5,0,0]


difficult_board=  [8,0,5,0,0,0,0,0,6,
               0,1,0,0,0,0,0,0,2,
               0,2,6,0,1,0,5,0,0,
               0,6,0,4,0,1,0,0,0,
               0,0,8,0,0,0,7,0,0,
               0,0,0,5,0,8,0,6,0,
               0,0,2,0,4,0,1,3,0,
               5,0,0,0,0,0,0,8,0,
               9,0,0,0,0,0,2,0,7]

# Error in the last row, there are two 7s
error_board=  [8,0,5,0,0,0,0,0,6,
               0,1,0,0,0,0,0,0,2,
               0,2,6,0,1,0,5,0,0,
               0,6,0,4,0,1,0,0,0,
               0,0,8,0,0,0,7,0,0,
               0,0,0,5,0,8,0,6,0,
               0,0,2,0,4,0,1,3,0,
               5,0,0,0,0,0,0,8,0,
               9,0,0,0,0,0,2,7,7]



def test_get_solved_positions():
    nose.assert_equals ([1,3,6,8,
                    9,10,11,13,
                    19,23,24,26,
                    28,31,32,33,34,35,
                    45,46,47,48,49,52,
                    54,56,57,61,
                    67,69,70,71,
                    72,74,77,79], suku.get_solved_positions(easy_board))
    nose.assert_equals ([0,2,8,
                    10,17,
                    19,20,22,24,
                    28,30,32,
                    38,42,
                    48,50,52,
                    56,58,60,61,
                    63,70,
                    72,78,80] , suku.get_solved_positions(difficult_board))

finish_difficult_board = \
       [8,9,5,3,2,7,4,1,6,
        4,1,7,8,5,6,3,9,2,
        3,2,6,9,1,4,5,7,8,
        7,6,9,4,3,1,8,2,5,
        1,5,8,2,6,9,7,4,3,
        2,3,4,5,7,8,9,6,1,
        6,8,2,7,4,5,1,3,9,
        5,7,3,1,9,2,6,8,4,
        9,4,1,6,8,3,2,5,7]

finish_easy_board = \
       [2,6,1,3,7,5,8,9,4,
        5,3,7,8,9,4,1,6,2,
        9,4,8,2,1,6,3,5,7,
        6,9,4,7,5,1,2,3,8,
        8,2,5,9,4,3,6,7,1,
        7,1,3,6,2,8,9,4,5,
        3,5,6,4,8,2,7,1,9,
        4,8,9,1,6,7,5,2,3,
        1,7,2,5,3,9,4,8,6]

finish_medium_board = \
       [2,5,8,1,4,7,3,9,6,
        4,6,9,3,5,8,7,1,2,
        1,7,3,2,6,9,4,8,5,
        3,1,2,9,7,5,6,4,8,
        5,8,6,4,1,3,9,2,7,
        7,9,4,8,2,6,1,5,3,
        6,2,1,5,3,4,8,7,9,
        9,3,5,7,8,1,2,6,4,
        8,4,7,6,9,2,5,3,1]

def test_check_valid_board():
    nose.assert_false(suku.check_valid_board(long_board))
    nose.assert_false(suku.check_valid_board(short_board))
    nose.assert_true(suku.check_valid_board(easy_board))
    nose.assert_true(suku.check_valid_board(medium_board))
    nose.assert_true(suku.check_valid_board(difficult_board))
    nose.assert_false(suku.check_valid_board(error_board))

def test_solve():

    nose.assert_true(suku.solve(easy_board))
    nose.assert_equals(finish_easy_board, easy_board)
    
    nose.assert_true(suku.solve(medium_board))
    nose.assert_equals(finish_medium_board, medium_board)
    
    nose.assert_true(suku.solve(difficult_board))
    nose.assert_equals(finish_difficult_board, difficult_board)

    nose.assert_false(suku.solve(error_board)) 

