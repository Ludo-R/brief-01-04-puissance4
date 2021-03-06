
"""
Vous devez développer un jeu de “puissance 4” similaire au jeu
 “4 in a row”. Dans ce jeu, deux joueurs s’affrontent. 
 Ils doivent à tour de rôle poser un jeton dans une grille. 
 Les jetons viennent se déposer dans l’emplacement libre le plus bas 
 de la colonne choisie. Le joueur qui réussit à aligner 4 de ses jetons, 
 dans n’importe quelle direction, gagne la partie. 
 Le jeu doit être jouable dans les modes suivants : humain contre humain 
 sur la même machine, humain contre IA et IA contre IA. 
 L’IA doit proposer plusieurs niveaux de difficulté. 
 La taille de la grille doit être paramétrable. 
 Le programme doit être développé suivant les trois grandes 
 parties suivantes : le moteur de jeu, la partie graphique et 
 l’IA (Intelligence Artificielle).
"""

import random
from itertools import groupby

EMPTY = '-'
R = 'O'
Y = 'X'
PLAYERS = [R, Y]
FLAG = True

class Puissance4:
    def __init__(self, rows=6, cols=7, turn=random.choice(PLAYERS), colplayed=None):
        self.rows = rows
        self.cols = cols
        self.board = [[EMPTY] * rows for i in range(cols)]
        self.colplayed = colplayed
        self.turn = turn

    def refresh(self):
        print("\n")
        for r in range(self.rows):
            print(' '.join(str(self.board[c][r]) for c in range(self.cols)))

    def checkwin(self):
        for i in self.board:
            checklist = ''.join(i)
            for value, group in groupby(checklist):
                if len(list(group)) >=4 and value != EMPTY:
                    print('\nWinner is player : %s\n'%self.turn)
                    exit()
            
    def dropcoin(self):
        try: 
            col = self.board[int(self.colplayed)]
            i = -1
            while col[i] != EMPTY:
                i -= 1
            col[i] = self.turn
        except IndexError:
            print('\nBad entry, columns between (0 and 6) and verify columns not full')

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