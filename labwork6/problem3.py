class BankAccount  :
    def __init__(self, __account_number, __balance) : 
        self.__account_number = __account_number
        self.__balance = __balance
    def deposit(self, Amount) :
        self.__balance += Amount
        print(self.__balance)
    def withdraw(self, Amount) : 
        if self.__balance >= Amount : 
            self.__balance -= Amount
            print(self.__balance)
        else : 
            print("You don't have that much money in your account")
    def __str__(self) : 
        return f"{self.__account_number, self.__balance}"
c1 = BankAccount(1, 10000)
print(c1)
c1.deposit(1000)
c1.withdraw(20000)
c1.withdraw(1000)

