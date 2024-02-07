import voidfunctions

def calcArea(len, wid) -> int:
  return len * wid

def calcPerim(len: int, wid: int) -> int:
  return 2 * len + 2 * wid

def areaPerim(len, wid):  # -> tuple[int, int]
  area = calcArea(len, wid)
  perim = calcPerim(len, wid)
  return area, perim

def main():
  voidfunctions.doSomething()
  length = int(input("Enter length: "))
  width = int(input("Enter width: "))
  a, p = areaPerim(length, width)
  print(f"Area: {a}\nPerimeter: {p}")
  pass


if __name__ == "__main__":
  main()
