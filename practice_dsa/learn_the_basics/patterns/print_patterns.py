def print_square(n: int):
    for i in range(0, n):
        for j in range(0, n):
            if j < n:
                print("*", end = " ")
        print()

def print_triangle(n: int):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()