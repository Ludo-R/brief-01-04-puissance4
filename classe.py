
import random
from itertools import groupby
import numpy as np
import unittest

R = '-1'
Y = '1'
PLAYERS = [R, Y]
FLAG = True

class Players:
    def realPlayerPlay(self):
        self.colplayed = input('\nPlay any col : (0-6)\n')
        return self.colplayed
    
    def botPlayerPlay(self):
        self.colplayed = random.randint(0,6)
        return self.colplayed


class Rules:
    def refresh(self):
        self.board = self.board.T
        print("\n")
        print(self.board)
        self.board = self.board.T

    def dropcoin(self):
        i = -1
        col = self.board[int(self.colplayed)-1]
        while col[i] != 0:
            i -= 1
        col[i] = self.turn
        return col[i]

    def checkwin(self):
        group1 = "1. 1. 1. 1."
        group2 = "-1. -1. -1. -1."
        #check vertical
        for i in self.board:
            checklist = ''.join(str(i))
            if group1 in checklist:
                print("Winner is Player 1")
                exit()
            if group2 in checklist:
                print("Winner is Player 2")
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


        #check diag
        group1 = "1.0, 1.0, 1.0, 1.0"
        group2 = "-1.0, -1.0, -1.0, -1.0"

        diags = [self.board[::-1,:].diagonal(i) for i in range(-self.board.shape[0]+1,self.board.shape[1])]
        diags.extend(self.board.diagonal(i) for i in range(self.board.shape[1]-1,-self.board.shape[0],-1))
        checklistdiag = [n.tolist() for n in diags]

class Game(Rules, Players):
    def __init__(self, rows=6, cols=7, turn=random.choice(PLAYERS), colplayed=None):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros(shape=(rows,cols))
        self.board = self.board.T
        self.colplayed = colplayed
        self.turn = turn
        
    def game(self):
        nbplayer = input('\nSelect Number of Players : 1 or 2 \n')
        if nbplayer == "2":         
            while FLAG == True:
                self.refresh()
                self.checkwin()
                if self.turn == R:
                    self.turn = Y
                else:
                    self.turn = R
                self.colplayed = self.realPlayerPlay()
                self.dropcoin()
        elif nbplayer == "1":
            difficulty = input('\nSelect bot difficulty : 1, 2, 3\n')
            while FLAG == True:
                self.refresh()
                self.checkwin()
                if self.turn == R:
                    self.turn = Y
                    self.colplayed = input('\nPlay any col : (0-6)\n')
                else:
                    self.turn = R
                    self.colplayed = self.botPlayerPlay()
                self.dropcoin()
        else:
            print("Invalid option")
            self.game()

test = Game()
test.game()