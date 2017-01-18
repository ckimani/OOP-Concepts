class BankAccount:
    """
    Parent class of bank account specifies main operations, withdraw and deposit
    """
    def __init__(self):
        pass
    def withdraw(self):
        pass
    def deposit(self):
        pass

class CurrentAccount(BankAccount):
    """
    Minimum balance is zero
    """
    def __init__(self):
        BankAccount.__init__(self)
        self.balance = 0
        self.amount = 0

    def deposit(self, amount):
        self.amount = amount
        if not (self.amount > 0):
            return 'Invalid deposit amount'
        else:
            self.balance += self.amount
            return self.balance

    def withdraw(self, amount):
        self.amount = amount
        if not (self.amount > 0):
            return 'Invalid withdraw amount'
        else:
            if ((self.amount > self.balance) or (self.balance - self.amount) < 0):
                return 'Cannot withdraw beyond the current account balance'
            else:
                self.balance -= self.amount
                return self.balance
            

class SavingsAccount(BankAccount):
    """
    Minimum balance is 500
    """
    def __init__(self):
        BankAccount.__init__(self)
        self.balance = 500
        self.amount = 0
    
    def deposit(self, amount):
        self.amount = amount
        if not (self.amount > 0):
            return 'Invalid deposit amount'
        else:
            self.balance += self.amount
            return self.balance
    
    def withdraw(self, amount):
        self.amount = amount
        if not (self.amount > 0):
            return 'Invalid withdraw amount'
        else:
            if (self.balance - self.amount) < 500:
                return 'Cannot withdraw beyond the current account balance'
            else:
                self.balance -= self.amount
                return self.balance
