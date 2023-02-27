
class ClLP37:
	def __init__(self, num1, num2):
		self.n1 = num1
		self.n2 = num2
		self.div = 0
		self.mod = 0
	
	def calc(self):
		self.div = self.n1 / self.n2
		self.mod = self.n1 % self.n2
	
	def getDiv(self):
		return self.div
	
	def getMod(self):
		return self.mod
	
	def getDivMod(self):
		return self.div, self.mod
