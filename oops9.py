class account:
    def __init__(self,acc,bal):
        self.balance=bal
        self.account_no=acc
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("debited", amount, "successfully")
            print("the total balance is:", self.display())
        else:
            print("Insufficient Funds")
    def credit(self,amount):
        self.balance+=amount   
        print("credited", amount, "successfully")
        print("the total balance is:", self.display())   
    def display(self):
        return self.balance  
    
acc=account(10000,12345)
acc.debit(1200)
acc.credit(3000)
    

