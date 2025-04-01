import sys
sys.setrecursionlimit(5000)


def fact_loop(n):
    product = 1
    for num in range(n, 0, -1):  # n * n-1 * n-2 * ... * 1
        product *= num
    return product


def fact(n):
    if n <= 1: return 1   # Base/Ending Case
    return n * fact(n-1)  # Recursive Case


def main():
    num = int(input("Enter a number: "))
    while num != 0:
        num_fact = fact(num)
        print(f"{num}! = {num_fact}")
        num = int(input("Enter a number: "))


if __name__ == '__main__':
    main()
