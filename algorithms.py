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

def manhattan_distance(state: str, goal: str, size: int) -> int:
    totalManDist = 0

    return totalManDist