# Bank Account Management System

class BankAccount:

    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be greater than 0")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
            else:
                print("Insufficient balance")
        else:
            print("Withdrawal amount must be greater than 0")

    def check_balance(self):
        print(f"Current balance: {self.balance:.2f}")
        return self.balance


if __name__ == "__main__":

    account = BankAccount("123456789", 1000)

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account.check_balance()

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "4":
            print("Thank you for using the Bank Account System")
            break

        else:
            print("Invalid choice")
