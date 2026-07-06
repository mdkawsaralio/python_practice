class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if not amount<=self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.__balance}")
    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number
    

accounts = BankAccount(12345, 1000)  # Example account
print(f"Account Number: {accounts.get_account_number()}")
print(f"Current Balance: {accounts.get_balance()}")
accounts.deposit(500) #depositing 500
accounts.withdraw(200)  #withdrawing 200
print(f"Current Balance after transactions: {accounts.get_balance()}")