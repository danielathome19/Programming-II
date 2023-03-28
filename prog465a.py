import random
import numpy as np


def maxMatrices(mat1, mat2):
  rows = len(mat1)
  cols = len(mat1[0])
  mOut = np.empty((rows, cols), dtype='int')
  for r in range(rows):
    for c in range(cols):
      mOut[r][c] = max(mat1[r][c], mat2[r][c])
  return mOut


def printMatrix(mat):
  for row in mat:
    for num in row:
      print(f"{num:3d} ", end="")
    print()


def main():
  mat1 = []
  mat2 = []
  for r in range(5):
    row1 = []
    row2 = []
    for c in range(5):
      rnd1 = random.randint(-50, 99)
      rnd2 = random.randint(-50, 99)
      row1.append(rnd1)
      row2.append(rnd2)
    mat1.append(row1)
    mat2.append(row2)

  print("Matrix 1:")
  printMatrix(mat1)

  print("\nMatrix 2:")
  printMatrix(mat2)

  mLargest = maxMatrices(mat1, mat2)
  print("\nLargest Elements:")
  printMatrix(mLargest)


if __name__ == "__main__":
  main()  # Run "pip install numpy" first