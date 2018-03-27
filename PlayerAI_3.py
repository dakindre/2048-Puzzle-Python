import sys
import math
from random import randint
from BaseAI_3 import BaseAI
from Grid_3 import Grid
from Displayer_3 import Displayer



class PlayerAI(BaseAI):
    def getMove(self, grid):
        moves = grid.getAvailableCells()

        #Initiate Alpha and Beta
        alpha = float('-inf')
        beta  = float('inf')

        newGrid = grid.clone()

        decision = alphaBeta(newGrid)
        decision.maximize(newGrid, alpha, beta)
        
        return


class alphaBeta(BaseAI):
    def __init__(self, grid):
        self.grid = grid
        self.possibleNewTiles = [2, 4]
        self.direction = -5

        self.depth = 0


    def cloneGrid(self, grid):
        return grid.clone()
    

    def getNewTileValue(self):
        if randint(0,99) < 100 * 0.9:
            return self.possibleNewTiles[0]
        else:
            return self.possibleNewTiles[1]

    def getScore(self):
        return self.score

    def maxDepth(self):
        if self.depth >= 5: return True
        else: return False

    def maximize(self, state, alpha, beta):
        if self.maxDepth():
            return (self.getHeuristicScore(state, 0))
                    
        self.depth += 1
        
        if not state.canMove():
            return None
        
        moves = state.getAvailableMoves()
        
        for x in moves:
            
            temp = self.cloneGrid(state)
            temp.move(x)
            
            displayer = Displayer()
            print('PARENT: ', x, ' depth ',self.depth, displayer.display(temp), )

            minValue = self.minimize(temp, alpha, beta)


            if minValue.getAB > alpha:
                alpha = minValue.getAB
                self.direction = m
                
            if not beta is float('inf'):
                if alpha >= beta:
                    break

        return returnSequence(direction, alpha)
            

    def minimize(self, grid, alpha, beta):
        self.depth += 1
        cells = grid.getAvailableCells()
        
        for x in cells:
            potential = grid.clone()
            potential.insertTile(x, self.getNewTileValue())

            displayer = Displayer()
            print('CHILD: ', displayer.display(potential))
            
            
            maxValue = self.maximize(potential, alpha, beta, grid)
            

            if beta > maxValue.getAB:
                beta  = maxValue.getAB

            if beta <= alpha:
                break
        print('Reached')
        return returnSequence(direction, beta)




    def getHeuristicScore(self, newGrid, oldScore):
        score = 0
        
        emptyWeight = 1
        closeWeight = 0
        orderWeight = 1
        scoreWeight = 1
        nearWeight = 0.6
        cornerWeight = 2
        
        debug = False
        # (1): actual score
        addScore = 5 - oldScore
        # print "scc " + str(addScore)
        if addScore > 0:
                addScore = math.log(addScore) / math.log(2)
                
        
        # (2): empty fields
        # the higher the score, the more important the empty fields
        # highest score * available fields
        fields = len(newGrid.getAvailableCells())
        
        #emptyFields = math.log(fields * newGrid.getHighestValue()) / math.log(2)
        # (3): how close are our numbers?
        # closescore = self.getCloseNumberScore(newGrid) 
        # score += closescore * 0.5
        # close = self.smoothness(newGrid) * math.log(newGrid.getHighestValue()) / math.log(2)
        # closescore = close
        
        # (4): are we close to a great corner order?
        # order = self.getOrderScore(newGrid)
                
# 		if corner == 0:
# 			nearWeight *= 2
# 			scoreWeight *= 2
# # 		
        
                
        score = addScore
        # print directionVectors
        
        if debug:
                ''''print "SCORE " + str(scoreWeight * addScore)
                print "EMPTY " + str(emptyFields * emptyWeight)
                # print emptyFields * emptyWeight
                # score += emptyfields
                #print "CLOSE " + str(closescore * closeWeight)
                
                print "ORDER " + str(order * orderWeight)
                print "NEAR " + str(near * nearWeight)
                print "CORNER " + str(corner)
                print "last score " + str(score)
        '''
        #
        return score



class returnSequence:
    def __init__(self, direction, ab):
        self.direction = direction
        self.ab = ab

    def getDir(self):
        return self.direction

    def getAB(self):
        return self.ab





























	            



