def calcArea(len, wid):
  return len * wid

def calcPerim(len, wid):
  return 2 * len + 2 * wid

def areaPerim(len, wid):
  area = calcArea(len, wid)
  perim = calcPerim(len, wid)
  return area, perim

def main():
  length = int(input("Enter length: "))
  width = int(input("Enter width: "))
  a, p = areaPerim(length, width)
  print(f"Area: {a}\nPerimeter: {p}")

if __name__ == "__main__":
  main()