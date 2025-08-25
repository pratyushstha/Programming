class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance +=amount
    def withdraw(self, amount):
        if(amount>self.balance):
            print("You can't withdraw what you don't have")
        else:
            self.balance-=amount
    def show_balance(self):
        print(self.balance)
c1 = BankAccount("ram", 1, 99)
c1.deposit(100)
c1.show_balance()
c1.withdraw(50)
c1.show_balance()
c1.withdraw(500)
c1.show_balance()