from unittest import TestCase
import dodoku.insert as insert 
from _overlapped import NULL
import dodoku

class InsertTest(TestCase):
    #valid board unit tests
    #Happy path analysis:
    #test100_101 valid board
    def test100_101ShouldReturnValidBoard(self):
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]

        expectedResult = [[0, -2, 0, 0, -1, 0, 0, -4, 0, None, None, None, None, None, None], [-8, 0, -1, -9, 0, 0, 0, 0, -5, None, None, None, None, None, None], [0, 0, 0, 0, -3, 0, 0, -1, 0, None, None, None, None, None, None], [0, -3, 0, 0, 0, 0, -4, 0, -6, None, None, None, None, None, None], [-5, 0, -9, 0, 0, 0, 0, 0, -7, None, None, None, None, None, None], [0, 0, 0, 0, 0, 0, -2, -8, 0, None, None, None, None, None, None], [-2, 0, 0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0], [0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9], [0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5], [None, None, None, None, None, None, 0, 0, -6, 0, 0, 0, 0, -9, 0], [None, None, None, None, None, None, -2, 0, 0, 0, 0, 0, -4, 0, -8], [None, None, None, None, None, None, -7, 0, -9, 0, 0, 0, 0, 0, 0], [None, None, None, None, None, None, 0, -5, 0, 0, -9, 0, 0, 0, 0], [None, None, None, None, None, None, -4, 0, 0, -6, 0, -3, -9, 0, 0], [None, None, None, None, None, None, 0, -6, 0, 0, -5, 0, 0, -3, -1]]
        actualResult = insert._create_board(grid)
        self.assertEqual(expectedResult, actualResult)  
     
    #valid grid from valid board unit tests
    #Happy path analysis:
    #test200_101 valid grid   
    def test200_101ShouldReturnValidGrid(self):
        board = [[0, -2, 0, 0, -1, 0, 0, -4, 0, None, None, None, None, None, None], [-8, 0, -1, -9, 0, 0, 0, 0, -5, None, None, None, None, None, None], [0, 0, 0, 0, -3, 0, 0, -1, 0, None, None, None, None, None, None], [0, -3, 0, 0, 0, 0, -4, 0, -6, None, None, None, None, None, None], [-5, 0, -9, 0, 0, 0, 0, 0, -7, None, None, None, None, None, None], [0, 0, 0, 0, 0, 0, -2, -8, 0, None, None, None, None, None, None], [-2, 0, 0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0], [0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9], [0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5], [None, None, None, None, None, None, 0, 0, -6, 0, 0, 0, 0, -9, 0], [None, None, None, None, None, None, -2, 0, 0, 0, 0, 0, -4, 0, -8], [None, None, None, None, None, None, -7, 0, -9, 0, 0, 0, 0, 0, 0], [None, None, None, None, None, None, 0, -5, 0, 0, -9, 0, 0, 0, 0], [None, None, None, None, None, None, -4, 0, 0, -6, 0, -3, -9, 0, 0], [None, None, None, None, None, None, 0, -6, 0, 0, -5, 0, 0, -3, -1]]
        
        expectedResult = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
        actualResult = insert._create_grid(board)
        self.assertEqual(expectedResult, actualResult)

    #valid grid unit tests
    #Happy path analysis:
    #test300_101 valid grid   
    def test300_101ShouldReturnValidFinalGrid(self):
        parms={'value':'3','cell':'r7c9','grid':'[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]' ,'integrity':'8e734231'}
        expectedResult = {'status': 'ok', 'grid': ['0', '-2', '0', '0', '-1', '0', '0', '-4', '0', '-8', '0', '-1', '-9', '0', '0', '0', '0', '-5', '0', '0', '0', '0', '-3', '0', '0', '-1', '0', '0', '-3', '0', '0', '0', '0', '-4', '0', '-6', '-5', '0', '-9', '0', '0', '0', '0', '0', '-7', '0', '0', '0', '0', '0', '0', '-2', '-8', '0', '-2', '0', '0', '-6', '0', '0', '0', '0', '3', '0', '-1', '-4', '0', '-6', '0', '0', '0', '-6', '0', '0', '-3', '0', '0', '0', '-2', '0', '0', '-1', '0', '-9', '0', '-4', '0', '-5', '-7', '0', '0', '0', '0', '0', '0', '-7', '0', '0', '-5', '0', '0', '-6', '0', '0', '0', '0', '-9', '0', '-2', '0', '0', '0', '0', '0', '-4', '0', '-8', '-7', '0', '-9', '0', '0', '0', '0', '0', '0', '0', '-5', '0', '0', '-9', '0', '0', '0', '0', '-4', '0', '0', '-6', '0', '-3', '-9', '0', '0', '0', '-6', '0', '0', '-5', '0', '0', '-3', '-1'], 'integrity': '8e734231'}
        actualResult = insert._insert(parms)
        
        self.assertEqual(expectedResult, actualResult)
