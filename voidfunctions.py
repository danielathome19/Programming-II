from calcfunctions import *


def doSomething():
  print("Hello, world!")


def printNums():
  x = 0
  while x < 10:
    print("x:", x)
    x += 1


def main():
  doSomething()
  printNums()
  a = add(1, 2)
  q, r = divmod2(5, 10)
  print(q, r)
  pass


if __name__ == "__main__":
  main()
