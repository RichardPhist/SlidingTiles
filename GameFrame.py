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
            return (size, zeroInd)
        
        state = cls.swap(state, zeroInd, zeroInd + size)
        zeroInd = zeroInd + size
        return (state, zeroInd)

    def doMoves(cls, state: str, moveList: str, size: int, zeroInd: int = -1) -> Tuple[List[str], int]:
        #function that calls other move functions
        #takes current state, list of moves, size, and index of 0
        #as arguments
        state = list(state)

        if zeroInd < 0:
            zeroInd = state.index('0')
        for move in moveList:

            #cls.print_puzzle(state, size)
            #print()
            #print(move)

            if move == 'l':
                state, zeroInd = cls.left(state, zeroInd, size)
                
            elif move == 'r':
                state, zeroInd = cls.right(state, zeroInd, size)
                
            elif move == 'd':
                state, zeroInd = cls.down(state, zeroInd, size)
                
            elif move == 'u':
                state, zeroInd = cls.up(state, zeroInd, size)
                

        #cls.print_puzzle(state, size)
        
        return (state, zeroInd)

    def print_puzzle(cls, puzzle: List[str], size: int):
        #helper function prints out state of the game
        for i, tile in enumerate(puzzle):
            print(tile, end=' ')
            if (i - size + 1) % size == 0:
                print('')