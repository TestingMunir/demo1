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


# Inheritance

class car:
    def __init__(self,windows, doors,enginetype,max_speed):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
        self.max_speed=max_speed

    def  power_source(self,enginetype):
        return"this person drive a {} car".format(enginetype)

    def drive_speed(self,speed,max_speed):
        return f"this person driveing at {speed} but max speed is {max_speed}"


audi=car(2,2,"petrol",300)
print(audi.power_source("petrol"))
print(audi.drive_speed(50,300))


class Tesla(car):
    def __init__(self, widows, doors, enginetype,self_driving):
        super().__init__(widows, doors, enginetype,max_speed=200)
        self.self_driving = self_driving

    def self_driving_mode(self):
        if self.self_driving:
            return "self driving mode is on"
        
        else:
            return "self driving mode is off"

tesla_m1=Tesla(2,2,"petrol",False)
print(tesla_m1.self_driving_mode())