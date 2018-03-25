import sys
from random import randint
from BaseAI_3 import BaseAI
import Minimax
import Minimaxab
from Grid import Grid
from Displayer import Displayer

class PlayerAI(BaseAI):
    def getMove(self, grid):
        moves = grid.getAvailableCells()

        #Initiate Alpha and Beta
        alpha = float('-inf')
        beta  = float('inf')

        newGrid = grid.clone()

        decision = alphaBeta(alpha, beta)
        decision.maximum()
        
        return


class alphaBeta(BaseAI):
    def __init__(self, alpha, beta):
        self.possibleNewTiles = [2, 4]
        self.score = 0
        self.alpha = alpha
        self.beta = beta
        self.depth = 5


    def cloneGrid(self, grid):
        return grid.clone()
    

    def getNewTileValue(self):
        if randint(0,99) < 100 * 0.9:
            return self.possibleNewTiles[0]
        else:
            return self.possibleNewTiles[1]


    def maximum(self, grid, alpha, beta, parent):
        
        if not grid.canMove():
            #Need to fill out
            return None
        
        currentNode = node(grid, move)
        moves = grid.getAvailableMoves()
        
        for x in moves:
            
            temp = cloneGrid(grid)
            temp.move(x)

            minValue = minimize(newGrid, a, b, x, )

    def minimize(self, grid, alpha, beta):
        print("In Minimize")
        cells = grid.getAvailableCells()
        
        for x in cells:
            potential = grid.clone()
            potential.insertTile(x, self.getNewTileValue())

            
            maxValue = maximize(potential, alpha, beta, parent)

            #Set Beta
            if self.beta > maxValue.score:
                self.beta = maxValue.score

            #Test for pruning
            elif self.beta <= self.alpha
                break
        return 
            


            


class node():
    def __init__(self, state, move, parent):
        self.state = state
        self.move = move
        self.point = points

class score():
    def __init(self, score, move):
        self.score = score
        self.move = move

