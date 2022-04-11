from ctypes import sizeof
import algorithms
import math
from GameFrame import game

def main():
    pee = "1234567890"
    poo = [1,2,3,4,0,5,6,7,8]

    #find 0 position in list
    zIndex = poo.index(0)
    print(zIndex)

    #after finding the position of 0, we can use these formulas to move U,D,L,R
    #up
    print(zIndex - math.sqrt(len(poo)))
    #down
    print(zIndex + math.sqrt(len(poo)))
    #left
    print(zIndex - 1)
    #right
    print(zIndex + 1)

    #need to add bounary conditions so we don't go outside the board

        

   # test = game()

   # test.doMoves(poo, "dd", 3, -1)




if __name__ == '__main__':
    main()