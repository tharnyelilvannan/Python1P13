# Author: Tharny Elilvannan
# Last Updated: October 24, 2024
# Purpose: Simulates a bank.

import random

# bank that allows you to deposit and withdraw funds
class Bank:

    # new accounts are attached to a name, password, and initial balance
    def __init__(self, name, initialDeposit, password):
        self.name = name
        self.accountNumber = random.randint(1, (2**63 - 1))
        self.balance = initialDeposit
        self.password = password

    # returns amount of money in account
    def getBalance(self):
        
        # if password is correct
        if (self.checkPassword()):
            return self.balance
        else:
            return "Incorrect password."
        
    # returns unique account number
    def getAccountNumber(self):

        if (self.checkPassword()):
            return self.accountNumber
        else:
            return "Incorrect password."
        
    # withdraw funds from account    
    def withdraw(self):

        # checks if password is correct
        if (self.checkPassword()):
            withdrawal = input("Enter the amount you would like to withdraw: ")

            # checks if there is enough money in the account
            if (self.overdraft(withdrawal)):
                self.balance = self.balance - withdrawal
                return self.balance
            else:
                return "Insufficient funds."
        else:
            return "Incorrect password."
        
    # deposits money into the account
    def deposit(self):

        if (self.checkPassword()):
            depositAmount = input("Enter the amount you would like to deposit: ")

            self.balance = self.balance + depositAmount
            return self.balance
        else:
            return "Incorrect password."
            
    # checks password
    # returns true if password is correct 
    def checkPassword(self):
        password = input("Enter your password: ")

        if (password == self.password):
            return True
        else:
            return False
        
    # checks if there is enough money in the account to do a withdrawal
    # returns true if there is enough money
    def overdraft(self, withdrawal):
        if ((self.balance - withdrawal) < 0):
            return False
        else:
            return True
        

account1 = Bank("Tharny Elilvannan", 2000, "hello")
print(account1.getBalance())
print(account1.getAccountNumber())