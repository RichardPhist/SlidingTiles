from typing import Tuple
from typing import List

class game:
    #helper function that swaps 0 tile
    def swap(cls, state, x: int, y: int,):
        #swaps location of tiles
        temp = state[x]
        state[x] = state[y]
        state[y] = temp
        return state

    def valid_moves(cls, zeroInd, gameSize, move):
        if move == 'l':
            if zeroInd % gameSize == 0:
                return False
        elif move == 'r':
            if zeroInd % gameSize == gameSize - 1:
                return False
        elif move == 'u':
            if zeroInd % gameSize == gameSize - 1:
                return False
        elif move == 'd':
            if zeroInd >= gameSize * (gameSize - 1):
                return False
    def left(cls, posistion, zeroInd, gameSize):
        #moves the 0 tile to the left
        if game.valid_moves(cls, zeroInd, gameSize, 'l') == False:
            return (posistion, zeroInd)
        
        posistion = cls.swap(posistion, zeroInd, zeroInd - 1)
        zeroInd = zeroInd - 1
        return (posistion, zeroInd)

    def right(cls, posistion, zeroInd: int, gameSize: int):
        #moves the 0 tile to the right
        if game.valid_moves(cls, zeroInd, gameSize, 'r') == False:
            return (posistion, zeroInd)

        posistion = cls.swap(posistion, zeroInd, zeroInd + 1)
        zeroInd = zeroInd + 1
        return (posistion, zeroInd)
    
    def up(cls, posistion, zeroInd, gameSize: int):
        #moves the 0 tile up
        if game.valid_moves(cls, zeroInd, gameSize, 'u') == False:
            return (posistion, zeroInd)
        
        posistion = cls.swap(posistion, zeroInd, zeroInd - gameSize)
        zeroInd = zeroInd - gameSize
        return (posistion, zeroInd)

    def down(cls, posistion, zeroInd, gameSize):
        #moves the 0 tile down
        if game.valid_moves(cls, zeroInd, gameSize, 'd') == False:
            return (posistion, zeroInd)
        
        posistion = cls.swap(posistion, zeroInd, zeroInd +gameSize)
        zeroInd = zeroInd + gameSize
        return (posistion, zeroInd)

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