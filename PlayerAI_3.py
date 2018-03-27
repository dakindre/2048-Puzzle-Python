import sys
import math
from random import randint
from BaseAI_3 import BaseAI
from Grid_3 import Grid
from Displayer_3 import Displayer
from copy import deepcopy
import queue

finalDepth = 2

class PlayerAI(BaseAI):
    
    def getMove(self, grid):
        alpha = scoreObject(float('-inf'), None)
        beta = scoreObject(float('inf'), None)

        #print('alpha ', alpha.value)
        #print('beta ', beta.value)

        #newGrid = grid.clone()
        #maxScore = self.alphaBeta(grid, alpha, beta, 0, None, 'max', grid)
        maxScore = self.maximize(grid, alpha, beta, 0, None, grid)
        
        return maxScore.getChild()
        
        
        

    def alphaBeta(self, grid, depth):
        
        if depth > finalDepth: return True

        #No moves to make exit with game over
        if not grid.canMove(): return True

        else: return False
        
        
    
    def maximize(self, grid, alpha, beta, depth, move, parent):
        if self.alphaBeta(grid, depth):
            heuristic = self.eval(grid)
            return maxMinObjects(move, heuristic)
        
        moves = grid.getAvailableMoves()
        ma = maxMinObjects(None, float('-inf'))
        
        for x in moves:
                           
            newGrid = grid.clone()
            newGrid.move(x)

            #print('Maximize ')
            #print('alpha [', alpha.value, '] beta [', beta.value, '] depth [', depth, ']')
            #Displayer().display(newGrid)
            
            mi = self.minimize(newGrid, alpha, beta, depth+1, x, grid)

            if mi.getUtility() > ma.getUtility():
                ma.child = mi.getChild()
                ma.utility = mi.getUtility()

            if ma.getUtility() >= beta.getValue():
                break

            if ma.getUtility() > alpha.getValue():
                alpha.value = ma.getUtility()
                alpha.move = ma.getChild

        return ma
                               
                
    def minimize(self, grid, alpha, beta, depth, move, parent):
        if self.alphaBeta(grid, depth):
            heuristic = self.eval(grid)
            return maxMinObjects(move, heuristic)
        
        mi = maxMinObjects(None, float('inf'))
        #print('In Min')
        cells = grid.getAvailableCells()
        for xy in cells:
            
            newGrid = grid.clone()
            newGrid.insertTile(xy, 2)

            #print('Minimize ')
            #print('alpha [', alpha.value, '] beta [', beta.value, '] depth [', depth, ']')
            #Displayer().display(newGrid)
            ma = self.maximize(newGrid, alpha, beta, depth+1, move, grid)

            if ma.getUtility() < mi.getUtility():
                mi.child = ma.getChild()
                mi.utility = ma.getUtility()

            if mi.getUtility() <= alpha.getValue():
                break

            if mi.getUtility() < beta.getValue():
                beta.value = mi.getUtility()
                beta.value = mi.getChild()
            
        return mi


    def eval(self, grid):
        heuristic = 0
        availableTiles = len(grid.getAvailableCells())
        #print('available tiles', availableTiles)
        return availableTiles
        
        


class scoreObject:
    def __init__(self, value, move):
        self.value = value
        self.move = move

    def getValue(self):
        return self.value

    def getMove(self):
        return self.move

class maxMinObjects:
    def __init__(self, child, utility):
        self.child = child
        self.utility = utility

    def getChild(self):
        return self.child

    def getUtility(self):
        return self.utility























	            



