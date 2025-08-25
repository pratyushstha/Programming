from datetime import datetime

def load_customers(filename):
    customers = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                name, acc_num, balance = line.strip().split(",")
                customers[acc_num] = {"name": name, "balance": float(balance)}
    except FileNotFoundError:
        pass
    return customers

def save_customers(filename, customers):
    try:
        with open(filename, "w") as f:
            for acc_num, data in customers.items():
                f.write(f"{data['name']},{acc_num},{data['balance']}\n")
    except Exception as e:
        print(f"Error: {e}")

def log_transaction(filename, acc_num, type_, amount):
    try:
        with open(filename, "a") as f:
            f.write(f"{datetime.now()},{acc_num},{type_},{amount}\n")
    except Exception as e:
        print(f"Error: {e}")

def deposit(customers, acc_num, amount):
    if acc_num in customers:
        customers[acc_num]["balance"] += amount
        log_transaction("transactions.txt", acc_num, "Deposit", amount)
        print("Deposit successful.")
    else:
        print("Account not found.")

def withdraw(customers, acc_num, amount):
    if acc_num in customers:
        if customers[acc_num]["balance"] >= amount:
            customers[acc_num]["balance"] -= amount
            log_transaction("transactions.txt", acc_num, "Withdrawal", amount)
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

customers = load_customers("customers.txt")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. View Customers")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        acc = input("Enter account number: ")
        amt = float(input("Enter amount: "))
        deposit(customers, acc, amt)
        save_customers("customers.txt", customers)
    elif choice == "2":
        acc = input("Enter account number: ")
        amt = float(input("Enter amount: "))
        withdraw(customers, acc, amt)
        save_customers("customers.txt", customers)
    elif choice == "3":
        for acc_num, data in customers.items():
            print(f"{data['name']} ({acc_num}): {data['balance']}")
    elif choice == "4":
        break
    else:
        print("Invalid choice")
