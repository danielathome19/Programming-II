from calcfunctions import *


def doThing():
    print("Hello, world!")


def printNums() -> None:
    for i in range(10):
        print("i:", i)
    pass


def main():
    doThing()
    printNums()
    a = add(1, 2)
    q, r = divmod2(5, 10)
    print(q, r)
    pass


if __name__ == "__main__":
    main()
