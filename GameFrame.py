from typing import Tuple
from typing import List

class game:
    def swap(cls, state: List[str], x: int, y: int,) -> List[int]:
        #swaps location of tiles
        temp = state[x]
        state[x] = state[y]
        state[y] = temp
        return state

    def left(cls, state: List[str], zeroInd: int, size: int) -> Tuple[List[str], int]:
        #moves the 0 tile to the left
        if zeroInd % size == 0:
            return (state, zeroInd)
        
        state = cls.swap(state, zeroInd, zeroInd - 1)
        zeroInd = zeroInd - 1
        return (state, zeroInd)

    def right(cls, state: List[str], zeroInd: int, size: int) -> Tuple[List[str], int]:
        #moves the 0 tile to the right
        if zeroInd % size == size - 1:
            return (state, zeroInd)

        state = cls.swap(state, zeroInd, zeroInd + 1)
        zeroInd = zeroInd + 1
        return (state, zeroInd)
    
    def up(cls, state: List[str], zeroInd: int, size: int) -> Tuple[List[str], int]:
        #moves the 0 tile up
        if zeroInd < size:
            return (state, zeroInd)
        
        state = cls.swap(state, zeroInd, zeroInd - size)
        zeroInd = zeroInd - size
        return (state, zeroInd)

    def down(cls, state: List[str], zeroInd: int, size: int) -> Tuple[List[str], int]:
        #moves the 0 tile down
        if zeroInd >= size * (size - 1):
            return (state, zeroInd)
        
        state = cls.swap(state, zeroInd, zeroInd + size)
        zeroInd = zeroInd + size
        return (state, zeroInd)

    def doMoves(cls, state: str, moveList: str, size: int, zeroInd: int = -1) -> Tuple[List[str], int]:
        #function that calls other move functions
        #takes current state, list of moves, size, and index of 0 as arguments
        retState = list(state)

        if zeroInd < 0:
            zeroInd = retState.index('0')
        for move in moveList:
            if move == 'l':
                retState, zeroInd = cls.left(retState, zeroInd, size)
                
            elif move == 'r':
                retState, zeroInd = cls.right(retState, zeroInd, size)
                
            elif move == 'd':
                retState, zeroInd = cls.down(retState, zeroInd, size)
                
            elif move == 'u':
                retState, zeroInd = cls.up(retState, zeroInd, size)
        
        return (retState, zeroInd)