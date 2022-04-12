import math
from queue import PriorityQueue
from typing import List
from typing import Tuple
from GameFrame import game

EXPAND_LIMIT = 2000000

def expand(stateTuple: Tuple[str, int, str], size: int) -> List[Tuple[str, int, str]]:
    state, zeroInd, moves = stateTuple

    possMoves = ['l', 'u', 'r', 'd']

    invMoves = {
        'l': 'r',
        'r': 'l',
        'u': 'd',
        'd': 'u'
    }

    # don't expand on inverse of last move as it will
    # immediately be rejected as a prior state
    if moves:
        possMoves.remove(invMoves[moves[-1]])

    newStateTuples = []
    expPuzzle = game()

    for move in possMoves:
        newState, newZeroInd = expPuzzle.doMoves(state=state,
                                                moveList=move,
                                                zeroInd=zeroInd,
                                                size=size)
        if newState != state:
            newStateTuples.append((newState, newZeroInd, moves + move))

    return newStateTuples

def out_of_place(state: str, goal: str) -> int:
    """
    Out of place heuristic
    Iterates through both strings comparing each character
    for each character not at the correct index
    increment the number of characters out of place
    """
    numOutOfPlace = 0
    for i in range(len(state)):
        if state[i] != goal[i]:
            numOutOfPlace += 1
    return numOutOfPlace

def manhattan_distance(state: str, gameSize: int) -> int:
    """
    Manhattan distance heuristic
    finds the total manhattan distanc of the game
    """
    totalManDist = 0
    for char in state:
        if char != '0':
            totalManDist += totalOffset(char, state.index(char), gameSize)
    return int(totalManDist)

def totalOffset(tile, tileIndex, gameSize) -> int:
    #calculates the total offset of a tile
    return rowOffset(tile, tileIndex, gameSize) + colOffset(tile, tileIndex, gameSize)

def rowOffset(tile, tileIndex, gameSize) -> int:
    #calculates the row offset of a tile
    return abs(conversion(tile) // gameSize - tileIndex // gameSize)

def colOffset(tile, tileIndex, gameSize) -> int:
    #calculates the column offset of a tile
    return abs(conversion(tile) % gameSize - tileIndex % gameSize)

def conversion(tile) -> int:
    webster = {"A": 9, "B": 10, "C": 11,"D": 12, "E": 13, "F": 14}
    retValue = webster.get(tile)
    if not retValue:
        return int(tile) - 1
    else:
        return retValue