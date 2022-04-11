from queue import PriorityQueue
from typing import List
from typing import Tuple
from GameFrame import game

EXPAND_LIMIT = 2000000

def breadthFirstSearch(start: str, goal: str, size: int) -> Tuple[str, int]:
    numExpands = 0
    zeroInd = start.index('0')
    start = list(start)
    goal = list(goal)

    queue = [start, zeroInd, ""]
    visited = {}

    while len(queue) > 0:
        if numExpands > EXPAND_LIMIT:
            return (f'exceeded limit of {EXPAND_LIMIT} expansions', numExpands)

        

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
