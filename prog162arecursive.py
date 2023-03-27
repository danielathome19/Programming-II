def fact(n):
  if n == 1: return n   # Base/ending Case
  return n * fact(n-1)  # Recursive Case

def factLoop(n):
  sum = 0
  for i in range(n, 0, -1):
    sum += i
  return sum

def main():
  num = int(input("Enter a number: "))
  while num != 0:
    factn = fact(num)
    print(f"{num}! = {factn}")
    num = int(input("Enter a number: "))

if __name__ == "__main__":
  main()