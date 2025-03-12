class ElectricBill:
    def __init__(self, kwh):
        self.kwh = kwh
        self.cost = 0.0

    def calc(self):
        # TODO
        ...

    def __str__(self):
        return f"The cost of {self.kwh} is ${self.cost:.2f}"
