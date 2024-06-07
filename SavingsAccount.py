from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, account_user, balance=0):
        super().__init__(account_number, account_user, balance)
        self.__interest_rate = 0.05

    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate
        return self.__interest_rate

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        if amount > 700000:
            print("Your withdrawal limit has been exceeded")
        else:
            super().withdraw(amount)

    def add_interest(self):
        interest_rate = self.get_interest_rate()
        interest = self.balance * interest_rate
        self.deposit(interest)
        return interest


savings = SavingsAccount(90649922431, "Daniel Adegbola", 5500)
savings.deposit(3500)
savings.withdraw(750)
savings.withdraw(950000)
savings.add_interest()
savings.display()
