from asyncio import queues
import math
from queue import PriorityQueue
from typing import List
from typing import Tuple
from GameFrame import game

EXPAND_LIMIT = 2000000
gameinstance = game()

def IterativeDeepeningDepthFirstSearch(state: str, goal: str, size: int) -> Tuple[str, int]:
    numOfExpands = 0
    expanded = {}
    StartState = list(state)
    Solution = list(goal)
    indexO = StartState.index('0')
    limit = 4
    stack = [[indexO, "", StartState, 0]]

    while len(stack) > 0:
        if numOfExpands > EXPAND_LIMIT:
            return("Is too thicc:" + numOfExpands)

        Odex, moves, position, d = stack.pop()

        if ''.join(position) in expanded:
            continue
        expanded[''.join(position)] = 1

        if position == Solution:
            return(moves, numOfExpands)

        for nextState in expand((position, Odex,moves)):
            if d + 1 < limit:
                nextState = [d + 1] + list(nextState)
                stack = stack + [nextState]

        numOfExpands = numOfExpands + 1
        
    
    
    

def breadth_first_search(state: str, goal: str, gameSize: int) -> Tuple[str, int]:
    numOfExpands = 0
    initState = state
    zeroInd = state.index('0')

    queue = [(initState, zeroInd, "")]
    visited = {}

    while len(queue) > 0:
        
        if numOfExpands > EXPAND_LIMIT:
            return ("Exceeded expansion limit:", numOfExpands)

        currState = queue.pop(0) #makes the current state of the game the state of the game that pops off the queue
        (currStringOfGame, indOfZero, moves) = currState 
        #unpacks and assigns values to new tuple

        if currStringOfGame == goal:
            #once goal state is found return the moves and num of expands to get there
            return(moves, numOfExpands)

        numOfExpands += 1

        for (currStringOfGame, indOfZero, moves) in expand(currState, gameSize):
            if not visited.get(str(currStringOfGame)):
                #if the state is not visited already explore
                visited[str(currStringOfGame)] = True
                queue.append((''.join(currStringOfGame), indOfZero, moves))
                #inserts to back of queue with tuple of string of game, index of 0, and moves taken

    return ('FAILURE', numOfExpands)

def depth_first_search(state: str, goal: str, gameSize: int) -> Tuple[str, int]:
    numOfExpands = 0
    initState = state
    zeroInd = state.index('0')

    queue = [(initState, zeroInd, "")]
    visited = {}

    while len(queue) > 0:
        
        if numOfExpands > EXPAND_LIMIT:
            return ("Exceeded expansion limit:", numOfExpands)

        currState = queue.pop(-1) #makes the current state of the game the state of the game that pops off the stack
        (currStringOfGame, indOfZero, moves) = currState 
        #unpacks and assigns values to new tuple

        if currStringOfGame == goal:
            #once goal state is found return the moves and num of expands to get there
            return(moves, numOfExpands)

        numOfExpands += 1

        for (currStringOfGame, indOfZero, moves) in expand(currState, gameSize):
            if not visited.get(str(currStringOfGame)):
                #if the state is not visited already explore
                visited[str(currStringOfGame)] = 2
                queue.append((''.join(currStringOfGame), indOfZero, moves))
                #inserts to back of queue with tuple of string of game, index of 0, and moves taken

    return ('FAILURE', numOfExpands)


def iter_deepening_A(state: str, goal: str, gameSize: int) -> Tuple[str, int]: 
    levelLimit = 5
    numOfExpands = 0
    currLevel = 0
    initState = state
    zeroInd = state.index('0')
    queue = PriorityQueue()
    tempQueue = PriorityQueue()
    visited = {} 
    queue.put([0, 0, currLevel, initState, zeroInd, ""])

    while not queue.empty():
        if numOfExpands > EXPAND_LIMIT:
            return ("Exceeded expansion limit:", numOfExpands)
        currState = queue.get()
        (estCost, currCost, currLevel, currStringOfGame, indOfZero, moves) = currState 
        if currStringOfGame == goal:
            return(moves, numOfExpands)
        #zero goes u,d,l,r = children
        for child in expand((currStringOfGame, indOfZero, moves), gameSize):
            if not visited.get(str(currStringOfGame)) and currLevel+1 < levelLimit:
                visited[''.join(currStringOfGame)] = 2
                childString, childIndOfZero, childMoves = child
                heuristic = out_of_place(childString, goal)
                #heuristic = manhattan_distance(childString, goal)
                queue.put([(currCost+1+heuristic), currCost+1, currLevel+1,
                    childString, childIndOfZero, childMoves])
            else:
                tempQueue.put([(currCost+1+out_of_place(currStringOfGame, goal)), currCost+1, 0,
                    childString, childIndOfZero, childMoves])
        if tempQueue.empty():
            queue = tempQueue  
            tempQueue = PriorityQueue()  

        numOfExpands +=1
    return ('FAILURE', numOfExpands)
        

def expand(stateOfGame: Tuple[str, int, str], gameSize: int) -> List[Tuple[str, int, str]]:
    """
    Function that takes state of the game (stringOfGame, index of 0, moves to be done) and
    game size (sqrt(len(stringOfGame))) as arugments
    Performs each move and updates the moves done after each move
    """
    #unpack and assign values of new tuple
    (currState, newZeroInd, listOfMoves) = stateOfGame
    possMoves = ['u', 'd', 'l', 'r']
    retArray = []

    for move in possMoves:
        (tempState, tempZeroInd) = gameinstance.doMoves(currState, [move], gameSize)
        retArray.append((tempState, tempZeroInd, listOfMoves + move))
        #print(tempState, tempZeroInd, move)

    return retArray

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
    """
    helper function for manhattan distance used to
    get goal index of a tile
    """
    #dictionary for characters and their indexes in 4x4 game
    webster = {"A": 9, "B": 10, "C": 11,"D": 12, "E": 13, "F": 14}
    retValue = webster.get(tile)
    if not retValue:
        #goal indexes of numbered tiles are their values-1
        return int(tile) - 1
    else:
        return retValue