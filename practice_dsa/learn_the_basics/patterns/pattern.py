from print_patterns import (
    print_square,
    print_triangle_stars,
    print_triangle_numbers,
    print_triangle_num_same,
    print_triangle_ulta_star,
    print_triangle_ulta_num,
    print_triangle_equi_star,
    print_triangle_equi_ulta
)

def print_pattern(n: int, fun: str):
    patterns = {
        "square": print_square,
        "triangle": print_triangle_stars,
        "triangle_num": print_triangle_numbers,
        "triangle_num_same": print_triangle_num_same,
        "tri_utla_star": print_triangle_ulta_star,
        "tri_ulta_num": print_triangle_ulta_num,
        "equi_star": print_triangle_equi_star,
        "equi_ulta": print_triangle_equi_ulta
    }

    if fun in patterns:
        patterns[fun](n)
    else:
        print(f"Invalid pattern function: {fun}")

if __name__ == "__main__":
    # read the input file
    with open("practice_dsa/learn_the_basics/input.txt", "r") as file:
        n = int(file.readline().strip())

    # call the pattern function
    print_pattern(n, "equi_ulta")