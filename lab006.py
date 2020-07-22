class Person(object):
    def __init__(self, name):
        self.name = name
    last_word = "word"
    def say(self, stuff):
        self.last_word = stuff
        return stuff
    def ask(self, stuff):
        return self.say("Would you please " + stuff)
    def greet(self):
        return self.say("Hello, my name is " + self.name)
    def repeat(self):
        return self.last_word

class Account(object):
    interest = 0.02
    transactions = []

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(["deposit",amount])
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.transactions.append(["withdraw",amount])
        return self.balance
