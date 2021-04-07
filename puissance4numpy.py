import random
from itertools import groupby
import numpy as np

R = '-1'
Y = '1'
PLAYERS = [R, Y]
FLAG = True

class Puissance4:
    def __init__(self, rows=6, cols=7, turn=random.choice(PLAYERS), colplayed=None):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros(shape=(rows,cols))
        self.board = self.board.T
        self.colplayed = colplayed
        self.turn = turn
    
    def refresh(self):
        self.board = self.board.T
        print(self.board)
        self.board = self.board.T

    def dropcoin(self):
        i = -1
        col = self.board[int(self.colplayed)]
        while col[i] != 0:
            i -= 1
        col[i] = self.turn

    def checkwin(self):
        group1 = "1. 1. 1. 1."
        group2 = "-1. -1. -1. -1."
        #check vertical
        for i in self.board:
            checklist = ''.join(str(i))
            if group1 in checklist:
                print("Winner is 1")
                exit()
            if group2 in checklist:
                print("Winner is -1")
                exit()
        
        #check horizontal
        self.board = self.board.T
        for i in self.board:
            checklist = ''.join(str(i))
            if group1 in checklist:
                print("Winner is 1")
                exit()
            if group2 in checklist:
                print("Winner is -1")
                exit()
        self.board = self.board.T

        #check diagonales


    def game(self):
        while FLAG == True:
            self.refresh()
            self.checkwin()
            if self.turn == R:
                self.turn = Y
            else:
                self.turn = R
            self.colplayed = input('\nPlay any col : (0-6)\n')
            self.dropcoin()

test = Puissance4()
test.game()