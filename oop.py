class Account():

	def __init__(self, name, balance=0, interest=0.02):
		self.__months = 12
		self.name = name
		self.balance = balance 
		self.interest = interest

	def setBalance(self, balance):
		self.balance = balance

	def getBalance(self):
		return self.balance

	def getInterest(self):
		self.__calcInterest()
		return self.balance

	def __calcInterest(self):
		self.balance = self.balance*(1+self.interest)
		return self.balance


if __name__ == "__main__":
	account = Account("Carol", 5000, 0.03)
	BradleysAccount = Account("Bradley")

	print account.getInterest()
	print account.months
	account.months = 140000
	print account.months
	print account.getBalance()	
	print BradleysAccount.getBalance()
