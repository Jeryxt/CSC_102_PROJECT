class Account:
    def __init__(self, account_number, account_user, balance=0):
        self.account_number = account_number
        self.account_user = account_user
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("You have deposited ₦" + str(amount) + "and your new balance is ₦" + str(self.balance))
        else:
            print("Deposit amount cannot be negative.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("You have withdrawn ₦" + str(amount) + "and your new balance is ₦" + str(self.balance))
        else:
            print("Insufficient withdrawal")

    def get_balance(self):
        return self.balance

    def display(self):
        print("Account Number: " + str(self.account_number))
        print("Account user: " + str(self.account_user))
        print("Balance: ₦" + str(self.balance))
