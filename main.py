from asyncio.windows_events import NULL
import algorithms
import os
import math
from GameFrame import game
from algorithms import a_star_search

def main():

    algos = [
        algorithms.breadth_first_search, #BFS
        algorithms.depth_first_search, #DFS
        algorithms.IterativeDeepeningDepthFirstSearch, #Iterative Deep
         algorithms.a_star_search, #A star
        algorithms.iter_deepening_A #Iterative Deep A Star
        ]

    algorithm_names = { #hashtable to get algorithm names
        algorithms.breadth_first_search: "BFS",
        algorithms.depth_first_search: "DFS",
        algorithms.IterativeDeepeningDepthFirstSearch: "IDDFS",
        algorithms.a_star_search: "A Star",
        algorithms.iter_deepening_A: "Iter_Deep_A",
    }

    f = NULL
    game_to_solve = game()

    for func in algos:
        print("Running")#to make sure it started
        for file_name in os.listdir("./"):
            if file_name.endswith(".txt"):
                f = open(file_name, 'r')
                f_lines = f.readlines()
                goal = f_lines[0].strip("\n")
                for line in f_lines[1:]:
                    #calls the algorithm to solve the game
                    (moves_to_solve, num_expands)= func(line.strip("\n"), goal, int(math.sqrt(len(line.strip("\n")))))
                    #calls doMoves to perform the solution found by the algorithm
                    (result_of_moves, zero_index) = game_to_solve.doMoves(line, moves_to_solve, int(math.sqrt(len(line.strip("\n")))))

                    #prints to terminal
                    print(f"Algorithm: ", algorithm_names[func])
                    print(f"Initial state: ", line[:-1]) 
                    print(f"Goal state: ", goal)
                    print(f"Solution: ", moves_to_solve)
                    print(f"Expands: ", num_expands)
                    print(f"Result: ", ''.join(result_of_moves[:-1]))
                    print("Now writing into csv files\n")
                    
                    #creates and writes to an output file
                    outfile_name = file_name.strip(".txt")
                    output_file = f"{algorithm_names[func]}{outfile_name}.csv"
                    true_output = ""
                    true_output += make_write_string(algorithm_names[func], line[:-1], goal, moves_to_solve, num_expands, result_of_moves)
                    write_to_output(output_file, true_output)
                f.close()
                
#helper function creates string to write to output file
def make_write_string(algo_name, init_state, goal_state, solution, expands, result) -> str:
    output_string = ""
    output_string += algo_name + ","
    output_string += init_state + ","
    output_string += goal_state + ","
    output_string += solution + ","
    output_string += str(expands) + ","
    output_string += ''.join(result[:-1])
    output_string += "\n"
    return output_string

#helper function that writes to output file
def write_to_output(output_file ,output_string):
    with open(output_file, 'a') as csvfile:
        csvfile.writelines(output_string)
        csvfile.close()

main()