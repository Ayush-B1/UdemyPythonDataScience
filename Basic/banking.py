class Account:

    def __init__(self, balance, accNo):
        self.balance = balance
        self.__accountNo = accNo

    def debit(self, amount):
        self.balance -= amount
        if self.balance == 0:
            print("There is nothing to debit")
        else:
            print(f'{amount} was debited from your account current balance = {self.balance}')

    def credit(self, amount):
        self.balance += amount
        print(f'{amount} was credited new balance = {self.balance}')

    def checkbalance(self):
        return self.balance


Acc1 = Account(10000, 443221)
Acc1.credit(2000)
