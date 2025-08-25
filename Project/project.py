from abc import ABC, abstractmethod

class Account(ABC):
    _account_counter = 1001

    def __init__(self, account_holder, initial_balance=0):
        self._account_number = Account._account_counter
        self._account_holder = account_holder
        self._balance = initial_balance
        Account._account_counter += 1

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print("Invalid withdraw amount or insufficient funds.")

    def get_balance(self):
        return self._balance

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self

    @abstractmethod
    def display_details(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_holder, initial_balance=0, interest_rate=2.5):
        super().__init__(account_holder, initial_balance)
        self._interest_rate = interest_rate

    def display_details(self):
        print("\n--- Savings Account Details ---")
        print(f"Account Number: {self._account_number}")
        print(f"Account Holder: {self._account_holder}")
        print(f"Balance: ${self._balance:.2f}")
        print(f"Interest Rate: {self._interest_rate}%")
        print("-----------------------------")

class CheckingAccount(Account):
    def __init__(self, account_holder, initial_balance=0, overdraft_limit=500):
        super().__init__(account_holder, initial_balance)
        self._overdraft_limit = overdraft_limit

    def display_details(self):
        print("\n--- Checking Account Details ---")
        print(f"Account Number: {self._account_number}")
        print(f"Account Holder: {self._account_holder}")
        print(f"Balance: ${self._balance:.2f}")
        print(f"Overdraft Limit: ${self._overdraft_limit:.2f}")
        print("------------------------------")

class Bank:
    def __init__(self):
        self._accounts = {}

    def create_account(self):
        print("\n--- Create a New Bank Account ---")
        account_holder = input("Enter account holder's name: ")
        try:
            initial_balance = float(input("Enter initial balance: $"))
        except ValueError:
            print("Invalid balance. Setting to $0.")
            initial_balance = 0
            
        print("Select account type:")
        print("  1. Savings Account")
        print("  2. Checking Account")
        choice = input("Enter choice (1 or 2): ")

        if choice == '1':
            new_account = SavingsAccount(account_holder, initial_balance)
        elif choice == '2':
            new_account = CheckingAccount(account_holder, initial_balance)
        else:
            print("Invalid choice. Account creation failed.")
            return

        self._accounts[new_account._account_number] = new_account
        print("\nAccount created successfully!")
        print(f"Your new account number is: {new_account._account_number}")

    def find_account(self, account_number):
        return self._accounts.get(account_number)

    def access_account(self):
        try:
            acc_num = int(input("\nEnter your account number to access: "))
        except ValueError:
            print("Invalid account number.")
            return

        account = self.find_account(acc_num)
        if not account:
            print("Account not found.")
            return

        while True:
            print(f"\n--- Account Menu for {account._account_holder} ({acc_num}) ---")
            print("1. Display Account Details")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Back to Main Menu")
            choice = input("Enter choice: ")

            if choice == '1':
                account.display_details()
            elif choice == '2':
                try:
                    amount = float(input("Enter amount to deposit: $"))
                    account + amount
                except ValueError:
                    print("Invalid amount.")
            elif choice == '3':
                try:
                    amount = float(input("Enter amount to withdraw: $"))
                    account - amount
                except ValueError:
                    print("Invalid amount.")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

my_bank = Bank()

while True:
    print("\n====== Welcome to OOP Bank ======")
    print("1. Create New Account")
    print("2. Access Existing Account")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        my_bank.create_account()
    elif choice == '2':
        my_bank.access_account()
    elif choice == '3':
        print("Thank you for using OOP Bank. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
