import algorithms
import math
from GameFrame import game
from aStar import a_star_search

def main():
    pee = "123456780"
    poo = "160273485"
    stupid = "123456708"

    test = game()

    #test.doMoves(poo, "dd", 3)
    #test.print_puzzle(poo, 3)

    #algorithms.breadth_first_search(poo, pee, 3)

    #print(algorithms.out_of_place(poo, pee))
    #print("{0}".format(algorithms.manhattan_distance(poo, math.sqrt(len(poo)))))

    a_star_search(stupid, pee, 3)
    


main()