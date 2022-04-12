import algorithms
import math
from GameFrame import game

def main():
    pee = "123456780"
    poo = "160273485"
    stupid = "123456708"

    test = game()

    test.doMoves(poo, "dd", 3, -1)

    #print(algorithms.out_of_place(poo, pee))
    print("{0}".format(algorithms.manhattan_distance(poo, math.sqrt(len(poo)))))


main()