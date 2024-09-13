class account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    def debit(self,amount):
        self.balance-=amount
        print(amount,"debited from the account")
        print("total balance after debiting",acc.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print(amount,"credited to the account")
        print("total balance after crediting",acc.get_balance())
    def get_balance(self):
        return self.balance
acc=account(10000,234256)
acc.debit(1900)
acc.credit(2000)
acc.get_balance()
