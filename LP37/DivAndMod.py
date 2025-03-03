class DivAndMod:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self._div = 0
        self._mod = 0
    
    def calc(self):
        self._div = self.n1 / self.n2
        self._mod = self.n1 % self.n2
    
    def get_div(self):
        return self._div
    
    def get_mod(self):
        return self._mod
    
    def get_divmod(self):
        return self._div, self._mod
