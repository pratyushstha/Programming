#include <stdio.h>

#define MAX_CUSTOMERS 100

struct Customer {
    int account_no;
    float balance;
};

void deposit(struct Customer *c, float amount) {
    c->balance += amount;
    printf("Deposited %.2f. New balance: %.2f\n", amount, c->balance);
}

void withdraw(struct Customer *c, float amount) {
    if (amount <= c->balance) {
        c->balance -= amount;
        printf("Withdrew %.2f. New balance: %.2f\n", amount, c->balance);
    } else {
        printf("Insufficient balance!\n");
    }
}

void show(struct Customer *c) {
    printf("Account No: %d\n", c->account_no);
    printf("Balance: %.2f\n", c->balance);
}

int findCustomer(struct Customer customers[], int total, int account_no) {
    for (int i = 0; i < total; i++) {
        if (customers[i].account_no == account_no)
            return i;
    }
    return -1;
}

int main() {
    struct Customer customers[MAX_CUSTOMERS];
    int total = 0;
    int choice, acc_no, index;
    float amount;

    while (1) {
        printf("\n1. Add Customer\n2. Deposit\n3. Withdraw\n4. Show Account\n5. Exit\nEnter choice: ");
        scanf("%d", &choice);

        if (choice == 1) {
            if (total >= MAX_CUSTOMERS) {
                printf("Bank is full!\n");
                continue;
            }
            printf("Enter new account number: ");
            scanf("%d", &customers[total].account_no);
            printf("Enter initial balance: ");
            scanf("%f", &customers[total].balance);
            total++;
            printf("Customer added.\n");
        } else if (choice >= 2 && choice <= 4) {
            printf("Enter account number: ");
            scanf("%d", &acc_no);
            index = findCustomer(customers, total, acc_no);

            if (index == -1) {
                printf("Customer not found!\n");
                continue;
            }

            if (choice == 2) {
                printf("Enter amount to deposit: ");
                scanf("%f", &amount);
                deposit(&customers[index], amount);
            } else if (choice == 3) {
                printf("Enter amount to withdraw: ");
                scanf("%f", &amount);
                withdraw(&customers[index], amount);
            } else if (choice == 4) {
                show(&customers[index]);
            }
        } else if (choice == 5) {
            printf("Goodbye!\n");
            break;
        } else {
            printf("Invalid choice.\n");
        }
    }

    return 0;
}
