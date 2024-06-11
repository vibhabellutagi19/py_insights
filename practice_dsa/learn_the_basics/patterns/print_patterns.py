def print_square(n: int):
    for i in range(0, n):
        for j in range(0, n):
            if j < n:
                print("*", end=" ")
        print()


def print_triangle_stars(n: int):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


def print_triangle_numbers(n: int):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(j + 1, end=" ")
        print()


def print_triangle_num_same(n: int):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(i + 1, end=" ")
        print()


def print_triangle_ulta_star(n: int):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()


def print_triangle_ulta_num(n: int):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print(j + 1, end=" ")
        print()


def print_triangle_equi_star(n: int):
    for i in range(0, n):
        stars = i * 2 + 1
        spaces = n - 1 - i

        for st in range(0, spaces):
            print(" ", end=" ")

        for sp in range(0, stars):
            print("*", end=" ")

        for st in range(0, spaces):
            print(" ", end=" ")
        print()


def print_triangle_equi_ulta(n: int):
    for i in range(0, n):
        stars = 2 * n - (i * 2 + 1)

        for st in range(0, i):
            print(" ", end=" ")

        for sp in range(0, stars):
            print("*", end=" ")

        for st in range(0, i):
            print(" ", end=" ")
        print()
