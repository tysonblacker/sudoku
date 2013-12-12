import nose.tools as nose
import sudoku.rcb as rcb
import numpy as np


test_board = [0,6,0,3,0,0,8,0,4,
               5,3,7,0,9,0,0,0,0,
               0,4,0,0,0,6,3,0,7,
               0,9,0,0,5,1,2,3,8,
               0,0,0,0,0,0,0,0,0,
               7,1,3,6,2,0,0,4,0,
               3,0,6,4,0,0,0,1,0,
               0,0,0,0,6,0,5,2,3,
               1,0,2,0,0,9,0,8,0]
               
tst1_board = [0,6,0,3,0,0,8,0,4,
               5,3,7,0,9,0,0,0,0,
               0,4,0,0,0,6,3,0,7,
               0,9,0,0,5,1,2,3,8,
               0,0,0,0,0,0,0,0,0,
               7,1,3,6,2,0,0,4,0,
               3,0,6,4,0,0,0,1,0,
               0,0,0,0,6,0,5,2,3,
               1,0,2,0,0,9,0,8,6]

empty_board = [0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0]

empty_possibles =  \
            [
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],

             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]

         ]

empty_rcb_possibles = \
            [
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],
             [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]
           ]  

test_rcb_possibles = \
            [
             [1,2,3,4], [2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9],
             [2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9],
             [2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9]
           ]  

test_rcb_possibles89 = \
            [
             [1,2,3,4], [1, 2,3,4,5,6,7,8], [1, 2,3,4,5,6,7,8],
             [2,3,4,5,6,7,8], [2,3,4,5,6,7,8], [2,3,4,5,6,7,8],
             [2,3,4,5,6,7,8], [2,3,4,5,6,7,8], [2,3,4,5,6,7,8,9]
           ]  

test_rcb_possibles_none = \
            [
             [1,2,3,4,9], [1, 2,3,4,5,6,7,8,9], [1, 2,3,4,5,6,7,8],
             [2,3,4,5,6,7,8], [2,3,4,5,6,7,8], [2,3,4,5,6,7,8],
             [2,3,4,5,6,7,8], [2,3,4,5,6,7,8], [2,3,4,5,6,7,8,9]
           ]  


               
def test_rcb_get_column():

    nose.assert_equals([5,7,3,1], rcb.get_column(0, test_board))
    nose.assert_equals([5,7,3,1], rcb.get_column(9, test_board))
    nose.assert_equals([3,6,4], rcb.get_column(3, test_board))
    nose.assert_equals([4,7,8,3], rcb.get_column(8, test_board))
    nose.assert_equals(empty_rcb_possibles, 
                  rcb.get_column(8, empty_possibles))

def test_rcb_get_row():
    nose.assert_equals([6,3,8,4], rcb.get_row(0, test_board))
    nose.assert_equals([6,3,8,4], rcb.get_row(8, test_board))
    nose.assert_equals([5,3,7,9], rcb.get_row(9, test_board))
    nose.assert_equals([5,3,7,9], rcb.get_row(10, test_board))
    nose.assert_equals(empty_rcb_possibles, 
                  rcb.get_row(8, empty_possibles))

def test_rcb_get_box():
    nose.assert_equals([6,5,3,7,4], rcb.get_box(0, test_board))
    nose.assert_equals([1,5,2,3,8], rcb.get_box(80, test_board))
    nose.assert_equals([8,4,3,7], rcb.get_box(17, test_board))
    nose.assert_equals([5,1,6,2], rcb.get_box(30, test_board))
    nose.assert_equals(empty_rcb_possibles, 
                  rcb.get_box(8, empty_possibles))

wrong_board = [6,6,0,3,0,0,8,0,4,
                5,3,7,0,9,0,0,0,0,
                0,4,0,0,0,6,3,0,7,
                0,9,0,9,5,1,2,3,8,
                0,0,0,0,0,0,0,0,0,
                7,1,3,6,2,0,0,4,0,
                3,0,6,4,0,6,0,1,0,
                6,0,0,0,6,0,5,2,3,
                1,0,2,0,0,9,0,8,0]
               

def test_rcb_valid_row():
    nose.assert_false(rcb.valid_row(0, wrong_board))
    nose.assert_true(rcb.valid_row(0, test_board))
    nose.assert_false(rcb.valid_column(63, wrong_board))
    nose.assert_true(rcb.valid_column(63, test_board))
    nose.assert_false(rcb.valid_box(68, wrong_board))
    nose.assert_true(rcb.valid_box(68, test_board))

def test_rcb_valid_position():
    nose.assert_false(rcb.valid_position(0, wrong_board))
    nose.assert_true(rcb.valid_position(0, test_board))
    nose.assert_false(rcb.valid_position(63, wrong_board))
    nose.assert_true(rcb.valid_position(63, test_board))
    nose.assert_false(rcb.valid_position(68, wrong_board))
    nose.assert_true(rcb.valid_position(68, test_board))

def test_rcb_get_nots():
    nose.assert_equal([6,3,8,4,5,7,3,1,6,5,3,7,4],
                         rcb.get_nots(0,test_board)) 
    nose.assert_equal([9,5,2,6,5,1,6,2], rcb.get_nots(40, test_board))
    
def test_rcb_get_possibles():
    nose.assert_equal([2,9], rcb.get_possibles(0,test_board))
    nose.assert_equal([3,4,7,8], rcb.get_possibles(40,test_board))
    nose.assert_equal([6], rcb.get_possibles(80, test_board))
    nose.assert_equal([6], rcb.get_possibles(1, test_board))


def test_rcb_possible():
    rcb.update_possible(80, test_board)
    nose.assert_equal(tst1_board, test_board) 
    

def test_get_possibles_board():
     nose.assert_equals(empty_possibles, rcb.get_possibles_board(empty_board))


def test_get_solos():
    nose.assert_equals( {0: 1}, rcb.get_solos(test_rcb_possibles))     
    nose.assert_equals( {8: 9}, rcb.get_solos(test_rcb_possibles89))     
    nose.assert_equals( {}, rcb.get_solos(test_rcb_possibles_none))     
