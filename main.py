from asyncio.windows_events import NULL
import algorithms
import os
import math
from GameFrame import game

def main():

    algos = [algorithms.breadth_first_search, algorithms.depth_first_search]
    algorithm_names = {
        algorithms.breadth_first_search: "BFS",
        algorithms.depth_first_search: "DFS"
    }

    f = NULL
    game_to_solve = game()

    for func in algos:
        for file_name in os.listdir("./"):
            if file_name.endswith(".txt"):
                f = open(file_name, 'r')
                f_lines = f.readlines()
                goal = f_lines[0].strip("\n")
                for line in f_lines[1:]:
                    (moves_to_solve, num_expands)= func(line.strip("\n"), goal, int(math.sqrt(len(line.strip("\n")))))

                    (result_of_moves, zero_index) = game_to_solve.doMoves(line, moves_to_solve, int(math.sqrt(len(line.strip("\n")))))
                    #print("Now inserting into csv files\n")
                    outfile_name = file_name.strip(".txt")
                    output_file = f"{algorithm_names[func]}{outfile_name}.csv"
                    with open(output_file, 'w', newline='') as csvfile:
                        print(f"Initial state: ", line[:-1])
                        print(f"Goal state: ", goal)
                        print(f"Solution: ", moves_to_solve)
                        print(f"Expands: ", num_expands)
                        print(f"Result: ", result_of_moves[:-1])
                    #csvfile.writelines
                f.close()

    #test.doMoves(poo, "dd", 3)
    #test.print_puzzle(poo, 3)

    #algorithms.breadth_first_search(poo, pee, 3)

    #print(algorithms.out_of_place(poo, pee))
    #print("{0}".format(algorithms.manhattan_distance(poo, math.sqrt(len(poo)))))

    #print(algorithms.breadth_first_search("035684712", pee, 3))
    #print(algorithms.depth_first_search(poo, pee, 3))
    #(path, expanded) = algorithms.depth_first_search(poo, pee, 3)
    #print(path, expanded)



main()