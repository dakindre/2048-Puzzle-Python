import sys
import math
from random import randint
from BaseAI_3 import BaseAI
from Grid_3 import Grid
from Displayer_3 import Displayer
from copy import deepcopy
import queue

finalDepth = 4

class PlayerAI(BaseAI):
    
    def getMove(self, grid):
        alpha = maxMinObjects('alpha', float('-inf'), None)
        beta = maxMinObjects('beta', float('inf'), None)

        #print('alpha ', alpha.value)
        #print('beta ', beta.value)

        #newGrid = grid.clone()
        #maxScore = self.alphaBeta(grid, alpha, beta, 0, None, 'max', grid)
        maxScore = self.maximize(grid, alpha, beta, 0, None, grid)
        #print('Return Type ', maxScore.getType(), ' Max Score ', maxScore.getScore(), 'Move ', maxScore.getMove())

        return maxScore.getMove()
        
        
        

    def alphaBeta(self, grid, depth):
        
        if depth == finalDepth: return True

        #No moves to make exit with game over
        if not grid.canMove(): return True

        else: return False
        
        
    
    def maximize(self, grid, alpha, beta, depth, move, parent):
        #print('Current Move ', move)
        if self.alphaBeta(grid, depth):
            heuristic = self.eval(grid)
            return maxMinObjects('max-heur', heuristic, move)
        
        moves = grid.getAvailableMoves()
        ma = maxMinObjects('ma', float('-inf'), None)
        
        for x in moves:
                           
            newGrid = grid.clone()
            newGrid.move(x)
            #print('Maximize ')
            #print('maxScore [', ma.score, '] depth [', depth, ']', ' move [', move, ']')
            #print('alpha [', alpha.score, '] beta [', beta.score, '] depth [', depth, ']', ' move [', move, ']')
            #Displayer().display(newGrid)
            
            mi = self.minimize(newGrid, alpha, beta, depth+1, x, grid)

            if mi.getScore() > ma.getScore():
                #print('INMAX---Max Returned Score ', mi.getScore(), ' Min Score ',ma.getScore())
                ma.score = mi.getScore()
                ma.move = x
            
        return ma
                               
                
    def minimize(self, grid, alpha, beta, depth, move, parent):
        #print('Current Move ', move)
        if self.alphaBeta(grid, depth):
            heuristic = self.eval(grid)
            return maxMinObjects('min-heur', heuristic, move)
        
        mi = maxMinObjects('mi', float('inf'), None)

        cells = grid.getAvailableCells()
        for xy in cells:
            
            newGrid = grid.clone()
            newGrid.insertTile(xy, 2)
            #print('Minimize ')
            #print('minScore [', mi.score, '] depth [', depth, ']', ' move [', move, ']')
            #print('alpha [', alpha.score, '] beta [', beta.score, '] depth [', depth, ']', ' move [', move, ']')
            #Displayer().display(newGrid)

            ma = self.maximize(newGrid, alpha, beta, depth+1, move, grid)
            

            if ma.getScore() < mi.getScore():
                #print('INMIN---Min Returned Score ', ma.getScore(), ' Max Score ',mi.getScore())
                mi.score = ma.getScore()
                mi.move = move


        return mi


    def eval(self, grid):
        heuristic = 0
        availableTiles = len(grid.getAvailableCells())
        #print('available tiles', availableTiles)
        return availableTiles
        
        


class maxMinObjects:
    def __init__(self, typeAB, score, move):
        self.typeAB = typeAB
        self.score = score
        self.move = move

    def getType(self):
        return self.typeAB

    def getScore(self):
        return self.score

    def getMove(self):
        return self.move




'''if mi.getScore() > ma.getScore():

    ma.score = mi.getScore()
    ma.move = x

if ma.getScore() > alpha.getScore():
    alpha.score = ma.getScore()
    alpha.move = ma.move

if not beta.getScore() ==  float('inf'):
    if ma.getScore() >= beta.getScore():
        break'''


                               

'''if alpha.getScore() < mi.getScore():
    alpha.score = mi.getScore()
    alpha.move = x

print(beta.getScore())
if not beta.getScore() == float('inf'):
    print(beta.getScore())
    if beta.getScore() <= alpha.getScore():
        print('Max End Reached')
        break

if mi.getUtility() > ma.getUtility():
    ma.child = mi.getChild()
    ma.utility = mi.getUtility()

if ma.getUtility() >= beta.getValue():
    break

if ma.getUtility() > alpha.getValue():
    alpha.value = ma.getUtility()
    alpha.move = ma.getChild'''




'''if ma.getScore() < mi.getScore():
    
    mi.score = ma.getScore()
    mi.move = move

if mi.getScore() <beta.getScore():
    beta.score = mi.getScore()
    #print('Beta Score ', beta.getScore())

if mi.getScore() <= alpha.getScore():
    break'''

'''if beta.getScore() > ma.getScore():
    print('Should Update')
    beta.score = ma.getScore()

if beta.getScore() <= alpha.getScore():
    print('Min End Reached')
    break'''

'''#print('Max Utility ', ma.getUtility(), ' Min Utility ', mi.getUtility())
if ma.getUtility() < mi.getUtility():
    #print('ma.getUtility() < mi.getUtility()')
    mi.utility = ma.getUtility()
    print('Max Utility ', ma.getUtility(), ' Min Utility ', mi.getUtility())
    mi.child = ma.getChild()

if mi.getUtility() <= alpha.getValue():
    #print('mi.getUtility() <= alpha.getValue()')
    break

if mi.getUtility() < beta.getValue():
    #print('mi.getUtility() < beta.getValue()')
    beta.value = mi.getUtility()
    beta.move = mi.getChild()'''


















	            



