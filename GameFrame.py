from typing import Tuple
from typing import List

class game:
    def left(cls, posistion, zeroInd, gameSize):
        #moves the 0 tile to the left
        if zeroInd % gameSize == 0:
            return (posistion, zeroInd)
        
        posistion = cls.swap(posistion, zeroInd, zeroInd - 1)
        zeroInd = zeroInd - 1
        return (posistion, zeroInd)

    def right(cls, posistion, zeroInd: int, gameSize: int):
        #moves the 0 tile to the right
        if zeroInd % gameSize == gameSize - 1:
            return (posistion, zeroInd)

        posistion = cls.swap(posistion, zeroInd, zeroInd + 1)
        zeroInd = zeroInd + 1
        return (posistion, zeroInd)
    
    def up(cls, posistion, zeroInd, gameSize: int):
        #moves the 0 tile up
        if zeroInd < gameSize:
            return (posistion, zeroInd)
        
        posistion = cls.swap(posistion, zeroInd, zeroInd - gameSize)
        zeroInd = zeroInd - gameSize
        return (posistion, zeroInd)

    def down(cls, posistion, zeroInd, gameSize):
        #moves the 0 tile down
        if zeroInd >= gameSize * (gameSize - 1):
            return (posistion, zeroInd)
        
        posistion = cls.swap(posistion, zeroInd, zeroInd +gameSize)
        zeroInd = zeroInd + gameSize
        return (posistion, zeroInd)

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