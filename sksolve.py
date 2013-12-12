#!/usr/bin/python

import sys, getopt

#import sudoku 
from sudoku.sudoku import *

fname="test_file"


def build_board(file_name, board):
    """
    Read a 9x9 file with sudoku values, 0 is a blank field
    Any extra lines or characters beyond the 9 are ignored.
    if the any of the charaters are not 0-9 then an exception
    is made when casting to an integer.
    """
    try:
        f = open(file_name, 'r')
        for i in range(9):
            line = f.readline()
            for j in range(9):
                board.append(int(line[j]))
    except (IOError, ValueError):
        print file_name, "is an invalid file"
        exit()
   
def main(argv):
    inputfile = ''
    board = []
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
       print 'sksolve.py -i <inputfile>'
       sys.exit(2)
    
    if len(opts) != 1 or len(args) != 0:
       print 'sksolve.py -i <inputfile>'
       sys.exit(2)
    opt, arg = opts[0]
    if opt in ("-i"):
        inputfile = arg
    else:
        print 'sksolve.py -i <inputfile>'
        sys.exit(2)
             
    build_board(inputfile, board)
    solve(board)
     

if __name__ == "__main__":
   main(sys.argv[1:])

