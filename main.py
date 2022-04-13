import algorithms
import math
from GameFrame import game

def main():
    goal = "123456780"
    problem1 = "160273485"
    problem2 = "123456708"
    problem3 = "130426758"

    

    test = game()

    #test.doMoves(poo, "dd", 3)
    #test.print_puzzle(poo, 3)

   # algorithms.breadth_first_search(problem1, goal, 3)

   # print(algorithms.out_of_place(problem1, goal))
    (path, expanded) = algorithms.iter_deepening_A(problem1, goal, 3, 1)
    print(path, expanded)

    #print("{0}".format(algorithms.manhattan_distance(poo, math.sqrt(len(poo)))))

  #  algorithms.breadth_first_search(problem2 , goal, 3)
   # algorithms.depth_first_search(problem2, goal, 3)
    


main()