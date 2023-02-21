class ClLP312:
  def __init__(self, fd, cg, et, rt):
    self.food = fd
    self.clothing = cg
    self.entertainment = et
    self.rent = rt
    self.budget = 0
    self.percents = [0]*4  # [0, 0, 0, 0]

  def _percent(self, number):
    return round((number / self.budget) * 100, 2)
  
  def calculate(self):
    self.budget = self.food + self.clothing + \
                  self.entertainment + self.rent
    self.percents[0] = self._percent(self.food)
    self.percents[1] = self._percent(self.clothing)
    self.percents[2] = self._percent(self.entertainment)
    self.percents[3] = self._percent(self.rent)

  def display(self):
    print("Category\t\tBudget")
    print(f"Food\t\t\t{self.percents[0]}%")
    print(f"Clothing\t\t{self.percents[1]}%")
    print(f"Entertainment\t{self.percents[2]}%")
    print(f"Rent\t\t\t{self.percents[3]}%")


def main():
  print("Enter the amount spent last month on the following items: \n")
  food = float(input("Food: $"))
  clothing = float(input("Clothing: $"))
  entertainment = float(input("Entertainment: $"))
  rent = float(input("Rent: $"))
  print()

  # Make a new "ClLP312" object, pass in the numbers to the constructor
  budget = ClLP312(food, clothing, entertainment, rent)
  budget.calculate()
  budget.display()


if __name__ == "__main__":
  main()