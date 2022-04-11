import algorithms
import math
from GameFrame import game

def main():
    pee = "1234567890"
    poo = "160273485"

    test = game()

    test.doMoves(poo, "dd", 3, -1)

    print(algorithms.out_of_place(poo, pee))



if __name__ == '__main__':
    main()