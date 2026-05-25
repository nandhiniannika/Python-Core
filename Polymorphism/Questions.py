# Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling make_sound().

class Animal:
    def make_sound(self):
        print("Animal Sounds")
class Dog(Animal):
    def make_sound(self):
        print("Bow Bowww")
class Cow(Animal):
    def make_sound(self):
        print("Mowwww")
class cat(Animal):
    def make_sound(self):
        print("meowwwww")

l = [Animal(),Dog(),cat(),Cow()]
# for i in l:
#     i.make_sound()


# Q2. Write a function operate(device) that calls device.start(). Pass in objects of Car, Computer, and WashingMachine —
# all of which define a start() method, but share no inheritance relationship. Show that Python’s polymorphism works through behavior, not type.

class Car:
    def start(self):
        print("Car is Started")
class Computer:
    def start(self):
        print("Computer is started")
class WashingMachine:
    def start(self):
        print("Washing machine started")
def operate(device):
    device.start()

l = [Car() , Computer() ,  WashingMachine()]
# for i in l:
#     operate(i)

# Q3. Create a Vector class that supports: • + operator → add coordinates • == operator → compare equality
# Show how operator overloading gives natural polymorphism to user-defined classes.

class Vector:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def __add__(self , other):
        return self.x + other.x, self.y + other.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# obj = Vector(1,2)
# obj2 = Vector(3 , 4)

# print(obj + obj2)
# print(obj ==  obj2)


# Q4. Create a base class Transport with move() and derived classes Bus and Bike that override it but also
# call the parent implementation using super().
# Show the combination of reuse + custom behavior.

class Transport:
    def move(self):
        print("Moving")

class Bus(Transport):
    def move(self):
        print("Bus Moving")
        super().move()
class Bike(Transport):
    def move(self):
        print("Bike Moving")
        super().move()
        return "Transport Done"

# obj = Bike()
# obj2 = Bus()
# print(obj.move())
# obj2.move()


# Q6. Design:
# • Base class Payment with process(amount) • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python handles it.

class Payment:
    def process(self , amount):
        print(f"{amount}")

class CreditCard(Payment):
    def process(self , amount , card_type):
        print(f"{amount} , {card_type}")

p= Payment()
c = CreditCard()

# p.process(1000)
# c.process(1000 ,"Visa")

# Create: Class Sorter with change(strategy) method.Separate strategy classes: BS, MS, QS, each implementing a different
# logic method.
# Demonstrate how polymorphism can be achieved without inheritance by using interchangeable strategy objects.

class BS:
    def logic(self,arr):
        arr.sort()
        return arr
class Ms:
    def logic(self , arr):
        arr.sort()
        return arr
class QS:
    def logic(self , arr):
        arr.sort()
        return arr
class Sorter:
    def change(self , strategy , arr):
        return strategy.logic(arr)
arr = [5,4,3,2,1]
s = Sorter()
# l = [BS() , Ms() , QS()]
# for i in l:
#     print(s.change(i , arr))

# Q8. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount
# → overrides again but calls parent using super() Show how polymorphism works across multiple levels.

class BaseAccount:
    def withdraw(self,amount):
        print(f"Withdrawing Amount {amount}")
class SavingsAccount(BaseAccount):
    def withdraw(self,amount):
        print(f"Savings Account {amount}")
class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self,amount):
        print(f"Premium Savings Account {amount}")
        super().withdraw(amount)

# l = [BaseAccount() , SavingsAccount() , PremiumSavingsAccount()]
# for i in l:
#     i.withdraw(1000)

# Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and Rectangle, each implementing a draw() method.
# Add another unrelated class Car with draw() and pass it — what happens and why?

class Circle:
    def draw(self):
        print("This is a Circle")
class Square:
    def draw(self):
        print("This is Square")
class Rectangle:
    def draw(self):
        print("This is Rectangle")
class Car:
    def draw(self):
        print("This is Car")
def draw(shape):
    shape.draw()

# l = [Circle() , Square() ,Rectangle() , Car()]
# for i in l:
#     draw(i)

# Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a pay() method.
# Now implement a version that checks types explicitly using isinstance() before calling pay().
# Compare both designs and explain why one breaks the spirit of polymorphism.

class UPI:
    def pay(self , mpin):
        print("UPI")
class Card:
    def pay(self , pin , otp):
        print("card")
class Cash:
    def pay(self , amount):
        print("cash")
def payment(x):
    if isinstance(x , UPI):
        x.pay(1787)
    elif isinstance(x, Cash):
        x.pay(8000)
    elif isinstance(x , Card):
        x.pay("A87" , 5078)
    else:
        print("Wrong Choice")
l = [UPI() , Card() , Cash()]
for i in l:
    payment(i)










