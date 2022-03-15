
import random
from itertools import groupby
import numpy as np
import unittest
from classe import *

#------------------------------------------------------
#
# Unit TEST for Puissance 4 game
#
#------------------------------------------------------

class TestUnit(unittest.TestCase):

    #----------> Players Class

    def test_realPlayerPlay(self):
        """
        Testing realPlayerPlay() fonction from Players()
            - Testing issue is not None
        """
        test = Game()
        self.assertIsNotNone(test.realPlayerPlay())

    def test_BotPlayerPlay(self):
        """
        Testing refresh() fonction from Players()
            -Testing issue is not None
        """
        test2 = Game()
        self.assertIsNotNone(test2.botPlayerPlay())

    #----------> Rules Class

    def test_refresh(self):
        """
        Testing refresh() fonction from Rules()
            - Testing print is not None
            - Testing Transposing Matrice
            - Testing the print change after dropcoin() fonction
        """
        test3 = Game()
        test3.refresh()
        self.assertIsNotNone(test3.board)
        self.assertIsNot(test3.board, test3.board.T)
        test3.colplayed=4
        test3.dropcoin()
        beforetest = test3.board
        test3.refresh()
        self.assertIsNot(beforetest, test3.board)
    
    def test_dropcoin(self):
        """
        Testing dropcoin() fonction from Rules()
            - Testing issue is not None
            - Testing return is equal to player turn
        """
        test4 = Game()
        test4.colplayed = 4
        self.assertIsNotNone(test4.dropcoin())
        #Need to convert float to test turn with numpy array
        self.assertEqual(test4.dropcoin(), float(test4.turn))




if __name__ == '__main__':
    unittest.main()