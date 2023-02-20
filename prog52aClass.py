class Shape:
  # Constructor: set up class data
  def __init__(self, length, width):
    self.length = length
    self.width = width
    self._area = 0   # _ prefix basically means 'private' so
    self._perim = 0  # it should only be called in the class

  # Mutator/Setter: modifies class data
  def calculate(self):
    self._area = self.length * self.width
    self._perim = 2 * self.length + 2 * self.width

  def setLength(self, length):
    self.length = length

  # Accessor/Getters: return class data
  def getArea(self):
    return self._area

  def getPerimeter(self):
    return self._perim


def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter width: "))
  shape = Shape(len, wid)  # Call "Shape" constructor
  # shape.setLength(5)
  shape.calculate()
  print("Area:", shape.getArea())
  print("Perimeter:", shape.getPerimeter())

if __name__ == "__main__":
  main()