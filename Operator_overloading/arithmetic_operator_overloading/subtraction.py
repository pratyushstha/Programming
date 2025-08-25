class BankAccount : 
    def __init__(self, balance) : 
        self.balance = balance
    def __sub__(self, Amount) : 
        if self.balance>=Amount : 
            return BankAccount(self.balance - Amount)
        else : 
            print("Insufficient funds!")
    def __str__(self) : 
        return f"You have {self.balance}"
b1 = BankAccount(1000)
print(b1-10000)