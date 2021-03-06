from typing import Tuple
from typing import List

#helper function that determines if moves are valid
def validMoves(zeroInd, gameSize, move):
        if move == 'l':
            if zeroInd % gameSize == 0:
                return False
        elif move == 'r':
            if zeroInd % gameSize == gameSize - 1:
                return False
        elif move == 'u':
            if zeroInd < gameSize:
                return False
        elif move == 'd':
            if zeroInd >= gameSize * (gameSize - 1):
                return False

class game:
    def left(cls, position, zeroInd, gameSize):
        #checks if move is valid
        if validMoves(zeroInd,gameSize,'l') is False:
            return (position,zeroInd)

        #moves the 0 tile to the left
        position = cls.swap(position, zeroInd, zeroInd - 1)
        zeroInd = zeroInd - 1
        return (position, zeroInd)

    def right(cls, position, zeroInd: int, gameSize: int):
        #checks if move is valid
        if validMoves(zeroInd,gameSize,'r') is False:
            return (position,zeroInd)

        #moves the 0 tile to the right
        position = cls.swap(position, zeroInd, zeroInd + 1)
        zeroInd = zeroInd + 1
        return (position, zeroInd)
    
    def up(cls, position, zeroInd, gameSize: int):
        #checks if move is valid
        if validMoves(zeroInd,gameSize,'u') is False:
            return (position,zeroInd)
        
        #moves the 0 tile up
        position = cls.swap(position, zeroInd, zeroInd - gameSize)
        zeroInd = zeroInd - gameSize
        return (position, zeroInd)

    def down(cls, position, zeroInd, gameSize):
        #checks if move is valid
        if validMoves(zeroInd,gameSize,'d') is False:
            return (position,zeroInd)
        
        #moves the 0 tile down
        position = cls.swap(position, zeroInd, zeroInd +gameSize)
        zeroInd = zeroInd + gameSize
        return (position, zeroInd)

    #helper function that swaps 0 tile
    def swap(cls, state, x: int, y: int,):
        #swaps location of tiles
        temp = state[x]
        state[x] = state[y]
        state[y] = temp
        return state

    def doMoves(cls, state: str, moveList: str, size: int, zeroInd: int = -1) -> Tuple[List[str], int]:
        #function that calls other move functions
        #takes current state, list of moves, size, and index of 0 as arguments
        retState = list(state)

        if zeroInd < 0:
            zeroInd = retState.index('0')
        for move in moveList:
            if move == 'l':
                (retState, zeroInd) = cls.left(retState, zeroInd, size)
                
            elif move == 'r':
                (retState, zeroInd) = cls.right(retState, zeroInd, size)
                
            elif move == 'd':
                (retState, zeroInd) = cls.down(retState, zeroInd, size)
                
            elif move == 'u':
                (retState, zeroInd) = cls.up(retState, zeroInd, size)
        
        return (retState, zeroInd)