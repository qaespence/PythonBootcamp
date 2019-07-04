# <summary>
# Udemy course - Complete Python Bootcamp
# Section 8 Challenge Assignment
# </summary>

# Create a bank account class that has two attributes: owner and balance
# and two methods: deposit and withdraw
# Also, withdrawals may not exceed the available balance

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def owner(self):
        return self.name

    def bal(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into your account!")
        print(f"Current balance is $"+str(self.bal()))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from your account")
            print(f"Current balance is $"+str(self.bal()))
        else:
            print("Funds unavailable!")
            print(f"Current balance is $"+str(self.bal()))

    def __str__(self):
        return 'Account owner is:\t'+self.owner()+'\nAccount balance:\t'+str(self.bal())

acct1 = Account('Jose',100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
