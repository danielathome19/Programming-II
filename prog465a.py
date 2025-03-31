from random import randint
# import numpy as np (have to do `pip install numpy` in the terminal)


def print_matrix(mat):
    for row in mat:
        for num in row:
            print(f"{num:3d} ", end="")
        print()


def max_matrices(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    mat_out = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            mat_out[r][c] = max(mat1[r][c], mat2[r][c])
    return mat_out


def main():
    mat1 = []
    mat2 = []
    for r in range(5):
        row1 = []
        row2 = []
        for c in range(5):
            row1.append(randint(-50, 99))
            row2.append(randint(-50, 99))
        mat1.append(row1)
        mat2.append(row2)

    print("Matrix 1:")
    print_matrix(mat1)

    print("\nMatrix 2:")
    print_matrix(mat2)

    mat_max = max_matrices(mat1, mat2)
    print("\nLargest Elements:")
    print_matrix(mat_max)


if __name__ == "__main__":
    main()
