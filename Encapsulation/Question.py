# Create a BankAccount class that stores:
# • account number • balance (should not be directly modifiable) You must:
# 1. Make the balance attribute inaccessible from outside.
# 2. Provide functions to deposit/withdraw that validate the amount.
# 3. Prevent withdrawal if balance becomes negative.
# 4. Show what happens if someone tries to modify balance directly and why encapsulation prevents it.
from collections.abc import set_iterator


class Bank:
    def __init__(self , AccNo , Balance , pin , name):
        self.AccNo = AccNo
        self.__Balance = Balance
        self.__pin = pin
        self._name = name
    def withdraw(self , amount):
        if amount > self.__Balance:
            print("Insufficient Balance")
        else:
            self.__Balance -= amount
            return self.__Balance
    def deposite(self , amount):
        self.__Balance =  self.__Balance + amount
        return self.__Balance
    def display(self):
        pin = int(input())
        if pin == self.__pin:
            return f"AccNo : {self.AccNo}\nBalance :{self.__Balance}\nName :  {self._name}"
obj = Bank(1234 , 20000,123 , "Visa")
obj.withdraw(500)
obj.deposite(2000)
# print(obj.display())


# 2. Design a Student class where marks:
# • should always be between 0 and 100
# •should never be set directly Enable updating marks only through a controlled method that performs range checks.
# Demonstrate:
# • trying to assign marks manually
# • why encapsulation protects invalid states

class Student:
    def __init__(self , marks):
        self._marks = marks
    @property
    def get(self):
        return self._marks
    @get.setter
    def get(self , new):
        if new > 0 and new <= 100:
            self._marks = new
        else:
            print("Invalid Marks")
# obj = Student(100)
# print(obj.get)
# obj.get = 35
# print(obj.get)


# 3. Create a SecureFile class that:
# • stores content privately
# • provides a method read(password)
# • refuses access if the password is incorrect
# • logs an "Unauthorized attempt" internally (cannot be accessed from outside)

class SecureFile:
    def __init__(self , name , password):
        self.name = name
        self.__password = password
        self.__logs = []
    def read(self):
        passwords = int(input())
        if passwords == self.__password:
            print("Succesful")
            return self.__password
        else:
            print("Incorrect Password")
            self.__logs.append("Unauthorized Access")
# obj = SecureFile("Visa" , 1234)
# obj.read()
# obj.read()

#
# .Design an Employee class
# where:
# • salary is hidden
# • outsiders cannot read salary directly
# • use getter method that logs each access attempt
# • provide a method to update salary but only if the new salary is higher (prevent accidental downgrade)

class Employee:
    def __init__(self , salary):
        self.__salary = salary
        self.logs = []
    @property
    def get(self):
        self.logs.append("Access")
        return self.__salary
    @get.setter
    def get(self , new):
        if new > self.__salary:
            self.__salary = new
        else:
            print("New Salary is less than old")
# obj = Employee(20000)
# print(obj.get)
# obj.get = 35000
# print(obj.get)



# 5. Create a Product class
# where:
# • price cannot be negative
# • discount cannot exceed 70%
# • internal final price calculation should not be directly exposed Provide only one public method get_final_price().

class Product:
    def __init__(self , price , discount):
        if price >= 0 and discount <= 70:
            self.__price = price
            self.__discount = discount
        else:
            print("Invalid Inputs")
    @property
    def get_final_price(self):
        final = self.__price  - (self.__price * ((self.__discount) / 100))
        return final

# obj = Product(10 , 70)
# print(obj.get_final_price)

# 6. Create a Character class
# with:
# • private _health
# • methods to damage(points) and heal(points)
# • health cannot drop below 0 or exceed max limit
# • expose only current health through a read-only getter

class Character:
    def __init__(self , health):
        self.max_limit = 50
        if health >= 0 and health <= self.max_limit:
            self.__health = health
        else:
            self.__health = 0
    def damage(self , points):
        self.__health -= points
        if self.__health < 0:
            self.__health = 0
    def heal(self , points):
        self.__health += points
        if self.__health > self.max_limit:
            self.__health = self.max_limit
    @property
    def current(self):
        return self.__health
#
# obj = Character(40)
# obj.damage(5)
# print(obj.current)
# obj.heal(10)
# print(obj.current)



# 7. Create: • An Engine class with private state like temperature
# • A Car class that uses an Engine but should: o Not allow users to manipulate engine temperature
# Only expose methods like start_car() or cool_engine()
# Demonstrate why giving direct engine access is dangerous.


class Engine:
    def __init__(self , temp):
        self.__temp = temp
    @property
    def getTemp(self):
        return self.__temp
class Car:
    def __init__(self):
        self.__engine = Engine(30)
    def start_car(self):
        print("Car Started")

    def cool_engine(self):
        print("Engine needed to be cooled")
    def showTemperature(self):
        print(self.__engine.getTemp)

# c = Car()
# c.start_car()
# c.cool_engine()
# c.showTemperature()

# 8. Create a ShoppingCart class
# where:
# • items are stored privately
# • users cannot directly modify item list
# • only add/remove methods are allowed
# • provide a method to get a safe copy of the cart items (not direct reference to internal list)

class ShoppingCart:
    def __init__(self):
        self.__items = []
    @property
    def get_items(self):
        return self.__items
    def add(self,n):
        return self.__items.append(n)
    def remove(self , v):
        return self.__items.remove(v)

# obj = ShoppingCart()
# obj.add("Book")
# obj.add("Pen")
# obj.remove("Pen")
# print(obj.get_items)


# 9. Implement a class incorrectly
# first:
# • Attendance stored in a list
# • Exposed directly so any outside code can modify it Then redesign properly:

# class Incorrectly:
#     def __init__(self):
#         self.attendence = []
#     def get(self):
#         return self.attendence
# obj = Incorrectly()
# obj.attendence.append("Present")
# obj.attendence.append("Present")
# obj.attendence.append("Absent")
# obj.attendence.append("Absent")
# print(obj.get())

# • Make attendance private
# • Provide controlled methods for marking attendance only


class Incorrectly:
    def __init__(self):
        self.__attendence = []
    def mark_attendence(self , status):
        self.__attendence.append(status)
    @property
    def attendence(self):
        return self.__attendence.copy()
        # return tuple(self.__attendence)

obj = Incorrectly()
obj.mark_attendence("Present")
obj.mark_attendence("Absent")


# obj.attendence.append("Absent")
# without .copy because it modifies original list  ['Present', 'Absent', 'Absent']
# so we use .copy that creates separate list or tuple because it is immutable

# obj.attendence.append(50)
# error because tuple is immutable

# obj.attendence.append("Present")
# it is not append in original list with .copy

print(obj.attendence)



















