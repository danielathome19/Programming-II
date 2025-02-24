class Budget:
    def __init__(self, food, clothing, entertainment, rent):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        self.rent = rent
        self._budget = 0
        self._percents = [0]*4  # [0,0,0,0]

    def _get_percent(self, number):
        return round((number/self._budget) * 100, 2)

    def calculate(self):
        self._budget = self.food + self.clothing + self.entertainment + self.rent
        self._percents[0] = self._get_percent(self.food)
        self._percents[1] = self._get_percent(self.clothing)
        self._percents[2] = self._get_percent(self.entertainment)
        self._percents[3] = self._get_percent(self.rent)

    def display(self):
        print("Category\t\tBudget")
        print(f"Food:\t\t\t{self._percents[0]}%")
        print(f"Clothing:\t\t{self._percents[1]}%")
        print(f"Entertainment:\t{self._percents[2]}%")
        print(f"Rent:\t\t\t{self._percents[3]}%")
        print(f"Total amount spent: ${self._budget:.2f}")


def main():
    print("Enter the amount spent last month on the following items:\n")
    food = float(input("Food: $"))
    clothing = float(input("Clothing: $"))
    entertainment = float(input("Entertainment: $"))
    rent = float(input("Rent: $"))
    print()

    # Make a new 'Budget' object, pass in the numbers to the constructor
    spending = Budget(food, clothing, entertainment, rent)
    spending.calculate()
    spending.display()
    pass


if __name__ == "__main__":
    main()
