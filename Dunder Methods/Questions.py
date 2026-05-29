class A:
    def __init__(self , x):
        self.x = x
    def __add__(self , o):
        return self.x + o
# obj = A(20)
# print(obj + 20)


class A:
    def __init__(self , x):
        self.x = x
    def __add__(self , o):
        if isinstance(o , int):
            return self.x + o
        if isinstance(o , A):
            return self.x + o.x
        else:
            print("Wrong Class")
            return 0

# obj = A(20)
# print(obj + 20)
# obj1 = A(50)
# obj2 = A(30)
# print(obj1 + obj2)
class A:
    def __init__(self , x , y , z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"x:{self.x} , y:{self.y} , z:{self.z}"
    def __repr__(self):
        return f"x:{self.x} , y:{self.y} , z:{self.z}"

    def __add__(self , o):
        if isinstance(o , int):
            return self.y + o
        elif isinstance(o , str):
            return self.x + o
        elif isinstance(o , A):
            return  self.x + o.x , self.y + o.y ,self.z + o.z
        else:
            print("Wrong Class")
            return 0
# s2 = s = A("Hello" , 20 , 10)
# s = A("Hello" , 20 , 20)
# s3 = A("Hello" , 20 , 20)
# print(s + "Hi")
# print(s + 20)
#
#
#
# print(s)
# print([s])


class Products:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"name : {self.name} , price:{self.price} , quantity:{self.quantity}"
class cart:
    def __init__(self):
        self.l = []
    def __add__(self , other):
         self.l.append(other)
         return self
    def __sub__(self, other):
        if other in self.l:
            self.l.remove(other)
        else:
            print("No items")
        return self
    def total_price(self):
        s = 0
        for i in self.l:
            s += i.price * i.quantity
        return s
    def __repr__(self):
        for i in self.l:
            print(i)
        print(f"total products:{len(self.l)}")
#
# p1 = Products("milk" , 2 , 2)
# c1 = cart()
# print(p1)
# print(c1)
# print(c1 + p1)


class Relation:
    def __init__(self,a):
        self.a = a
    def __gt__(self,other):
        return self.a > other.a
    def __lt__(self,other):
        return self.a < other.a
    def __ge__(self,other):
        return self.a >= other.a
    def __le__(self,other):
        return self.a <= other.a
    def __eq__(self, other):
        return self.a == other.a
# e1 = Relation(45)
# e2 = Relation(45)
# print(e1 > e2)
# print(e1 < e2)
# print(e1 >= e2)
# print(e1 <= e2)
# print(e1 == e2)
import math
class vector:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    def __sub__(self , other):
        return self.x - other.x
    def check(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __gt__(self , other):
        return self.check() > other.check()
    def __lt__(self , other):
        return self.check() < other.check()
    def __ge__(self , other):
        return self.check() >= other.check()

    def __le__(self , other):
        return self.check() <= other.check()
    def __eq__(self , other):
        return self.check() == other.check()
    def __str__(self):
        return f"{self.x} , {self.y}"
# v1 = vector(2 , 5)
# v2 = vector(5,2)
# v3 = vector(3,4)
# print(v1 + v2 + v3)
# print(v1 - v2)
# print(v1 > v2)
# print(v1 < v2)
# print(v1 >= v2)
# print(v1 <= v2)
# print(v1 == v2)
# print(v1)




class BankAccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self , amount):
        self.balance += amount
    def withdraw(self , amount):
        if self.balance>=amount:
            self.balance -= amount
        else:
            return f"Insufficient Balance"
    def __str__(self):
        return f"Account Holder :{self.account_holder} \n Balance :{self.balance}"
    def __add__(self , other):
        return self.balance + other.balance
    def __sub__(self, other):
        return self.balance - other.balance
    def __lt__(self, other):
        return self.balance < other.balance
    def __eq__(self, other):
        return self.balance == other.balance
    def __getattribute__(self, item):
        print(f"Accessing attribute {item}")
        return object.__getattribute__(self,item)
    def __setattr__(self, name, value):
        if name == "balance" and value < 0:
            print("Negative Balance is not allowed")
        else:
            return object.__setattr__(self , name , value)
# obj = BankAccount("Nandhini" , 10000)
# obj.deposit(10000)
# obj.withdraw(5000)
# print(obj)
# obj2 = BankAccount("Harshitha" , 1000)
# print(obj + obj2)
# print(obj - obj2)
# print(obj < obj2)
# print(obj == obj2)
# obj.balance = 1000000
# print(obj)




class Product:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return f"Product : {self.name} \n Price : {self.price} \n Quantity : {self.quantity}"
    def __add__(self,other):
        return self.total_price() + other.total_price()
    def __mul__(self , num):
        return self.price * num
    def __gt__(self , other):
        return self.total_price() > other.total_price()
    def __eq__(self , other):
        return self.price == other.price
    def __setattr__(self, name,value):
        if name == "price" and value <0:
            print("Price should be greater that 0")
        else:
            return object.__setattr__(self , name , value)
    def __getattr__(self, item):
        return f"Attribute not found {item}"
# obj = Product("Milk" , 20 , 5)
# obj2 = Product("Tea Packets" , 10 , 20)
# print(obj)
# print(obj2)
# print(obj + obj2)
# print(obj * 5)
# print(obj == obj2)
# print(obj > obj2)
# obj.price = 40
# print(obj.color)



class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks > 90:
            return "A"
        elif self.marks > 60:
            return "B"
        else:
            return "C"
    def __str__(self):
        return f"Student Name : {self.name} \n Marks : {self.marks} \n Grade :{self.grade()}"
    def __add__(self , other):
        return self.marks + other.marks
    def __truediv__(self, num):
        return self.marks / num
    def __lt__(self, other):
        return self.marks < other.marks
    def __ge__(self, other):
        return self.marks >= other.marks
    def __getattribute__(self, item):
        print(f"Accessing attribute of {item}")
        return object.__getattribute__(self , item)
    def __setattr__(self, name, value):
        if (name == "marks" and (value < 0 or value > 100)):
            print("Marks should be in range 0 to 100")
        else:
            return object.__setattr__(self, name, value)
# obj = Student("Nandhini" , 100)
# print(obj)
# obj2 = Student("Harshitha" , 99)
# print(obj2)
# obj2.marks = -99
# print(obj < obj2)
# print(obj >= obj2)
# print(obj / 5)




class Rectangle:
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def __str__(self):
        return f"Length : {self.length} , Breadth : {self.breadth} , Area :{self.area()}"
    def __add__(self , other):
        return self.area() + other.area()
    def __sub__(self , other):
        return self.area() + other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __getattr__(self, item):
        return f"{item} is missing"
    def __setattr__(self, name, value):
        if (name == "length" and value < 0) or (name == "breadth" and value < 0):
            print("Length and Breadth should be greater than 0")
        else:
            return object.__setattr__(self, name, value)
# obj = Rectangle(100,200)
# print(obj)
# obj2 = Rectangle(50 , 25)
# print(obj2)
# print(obj + obj2)
# print(obj + obj2)
# print(obj + obj2)


# Question 9: Laptop Specification
# Create a class Laptop with:
# •	attributes: brand, ram, price
# •	method: upgrade_ram(extra_ram)
# Implement:
# •	__str__()
# •	__add__() → add prices of two laptops
# •	__mul__() → multiply price for bulk purchase
# •	__lt__() → compare price
# •	__eq__() → compare RAM
# •	__getattribute__() → print access message
# •	__setattr__() → RAM and price must be positive


class Laptop:
    def __init__(self , brand , ram , price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def upgrade_ram(self , extra_ram):
        self.ram += extra_ram
        return self.ram
    def __str__(self):
        return f"Brand : {self.brand}, RAM : {self.ram}, Price = {self.price}"
    def __add__(self, other):
        return self.price + other.price
    def __mul__(self , other):
        return self.price * other.price
    def __lt__(self, other):
        return s7elf.price < other.price
    def __eq__(self , other):
        return self.ram == other.ram
    def __getattribute__(self, item):
        print("Nandhini is accessing Youuuu!!!!!!")
        return super().__getattribute__(item)
    def __setattr__(self, key, value):
        if (key == "ram" or key == "price") and value < 0:
            value = 0
        super().__setattr__(key , value)
l1 = Laptop("HP" , 256,60000)
l2 = Laptop("Lenovo" , 369, 65000)

print(l1 + l2)
print(l1 * l2)
print(l1 < l1)
print(l1 == l2)
print(l1)
print(l2)





# Question 10: Game Player
# Create a class Player with:
# •	attributes: name, health, attack_power
# •	method: attack(enemy)
# Implement:
# •	__str__()
# •	__add__() → combine attack powers
# •	__sub__() → reduce health after attack
# •	__gt__() → compare health
# •	__eq__() → compare attack power
# •	__getattr__() → return custom message for unavailable player stat
# •	__setattr__() → health cannot go below 0


class Player:
    def __init__(self , name , health , attack_power):
        self.name = name
        self.health= health
        self.attack_power = attack_power
    def attack(self , enemy):
        self.attack_power -= enemy
        return f"{self.name} attacked {enemy.name}"
    def __str__(self):
        return f"Name : {self.name}, Health : {self.health}, Attack Power :{self.attack_power}"
    def __add__(self , other):
        return self.attack_power + other.attack_power
    def __sub__(self , other):
        return self.attack_power - other.attack_power
    def __gt__(self , other):
        return self.attack_power > other.attack_power
    def __eq__(self , other):
        return self.attack_power == other.attack_power
    def __getattr__(self, item):
        return f"{item} is Not present"
    def __setattr__(self, key, value):
        if key == 'health' and value < 0:
            value = 0
        super().__setattr__(key , value)

p1 = Player("Nandhini" , 50 , 250)
p2 = Player("Vaishnavi" , -25 , 50)

# print(p1 + p2)
# print(p1 - p2)
# print(p1 > p2)
# print(p1 == p2)
# print(p1)
# print(p2)


























