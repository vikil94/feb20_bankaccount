class BankAccount:

    interest_rate = 1
    accounts = []

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    @classmethod
    def create(cls):
        account = BankAccount()
        cls.accounts.append(account)
        return account

    @classmethod
    def total_funds(cls):
        total = 0
        # cls.accounts refers to the list accounts
        for num in range(0, len(cls.accounts)):
            # it is a class variable so needs the cls
            total += cls.accounts[num].balance
            # in order to call on that variable
        return total

    @classmethod
    def interest_time(cls):
        for num in range(0, len(cls.accounts)):
            current_account = cls.accounts[num]
            current_account.balance = current_account.balance
            * (1 + current_account.interest_rate / 100)


# my_account = BankAccount.create()
# your_account = BankAccount.create()
# print(my_account.balance)  # 0
# print(BankAccount.total_funds())  # 0
# my_account.deposit(200)
# your_account.deposit(1000)
# print(my_account.balance)  # 200
# print(your_account.balance)  # 1000
# print(BankAccount.total_funds())  # 1200
# BankAccount.interest_time()
# print(my_account.balance)  # 202.0
# print(your_account.balance)  # 1010.0
# print(BankAccount.total_funds())  # 1212.0
# my_account.withdraw(50)
# print(my_account.balance)  # 152.0
# print(BankAccount.total_funds())  # 1162.0
