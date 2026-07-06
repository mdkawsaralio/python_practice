class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance = {self.balance}")
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have enough balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance = {self.balance}")

    def get_balance(self):
        return self.balance


accounts = {}

while True:
    print("\n===== BANK MENU =====")
    print("1. Add Account")
    print("2. View Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input.")
        continue

    if choice == 1:
        try:
            account_number = int(input("Enter account number: "))

            if account_number in accounts:
                print("Account already exists.")
            else:
                initial_balance = float(input("Enter initial balance: "))
                accounts[account_number] = BankAccount(account_number, initial_balance)
                print("Account created successfully.")

        except ValueError:
            print("Invalid input.")

    elif choice == 2:
        try:
            account_number = int(input("Enter account number: "))

            if account_number not in accounts:
                print("Account not found.")
            else:
                account = accounts[account_number]
                print("Account Number:", account.account_number)
                print("Balance:", account.balance)

        except ValueError:
            print("Invalid input.")

    elif choice == 3:
        try:
            account_number = int(input("Enter account number: "))

            if account_number not in accounts:
                print("Account not found.")
            else:
                amount = float(input("Enter deposit amount: "))
                accounts[account_number].deposit(amount)

        except ValueError:
            print("Invalid input.")

    elif choice == 4:
        try:
            account_number = int(input("Enter account number: "))

            if account_number not in accounts:
                print("Account not found.")
            else:
                amount = float(input("Enter withdrawal amount: "))
                accounts[account_number].withdraw(amount)

        except ValueError:
            print("Invalid input.")

    elif choice == 5:
        try:
            account_number = int(input("Enter account number: "))

            if account_number not in accounts:
                print("Account not found.")
            else:
                print("Current Balance:", accounts[account_number].get_balance())

        except ValueError:
            print("Invalid input.")

    elif choice == 6:
        print("Thank you for visiting.")
        break

    else:
        print("Invalid choice.")