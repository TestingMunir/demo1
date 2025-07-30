"""####  Classes and Objects
Object-Oriented Programming (OOP) is a programming paradigm that uses 
"objects" to design applications and computer programs. OOP allows for
 modeling real-world scenarios using classes and objects. This lesson covers 
 the basics of creating classes and objects, including instance variables and methods."""

class Dog:

    this_is_class_var="this is class var"

    def __init__(self,legs,category):
        self.legs=legs
        self.category=category

    def bark(self):
        legs=self.legs+1
        print("barking")
        return legs


tommy=Dog(4,"mamal")
barking_legs=tommy.bark()
print("thisiis barking legs:-  {}".format(barking_legs))

print(tommy.legs,tommy.category)
print(tommy.this_is_class_var)


### Modeling a Bank Account

## Define a class for bank account
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited. New balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds!")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. New Balance is {self.balance}")

    def get_balance(self):
        return self.balance
    
## create an account

account=BankAccount("Krish",5000)
print(account.balance)

## Call isntance methods
account.deposit(100)

account.withdraw(300)

print(account.get_balance())