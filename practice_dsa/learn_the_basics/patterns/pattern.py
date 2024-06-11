
from print_patterns import print_square, print_triangle


def print_pattern(n: int, fun: str ):
    if fun == 'square':
        print_square(n)
    elif fun == 'triangle':
        print_triangle(n)

if __name__ == '__main__':
    # read the input file
    with open('practice_dsa/learn_the_basics/input.txt', 'r') as file:
        n = int(file.readline().strip())
    
    # call the pattern function
    #print_pattern(n, "square")
    print_pattern(n, "triangle")


    
