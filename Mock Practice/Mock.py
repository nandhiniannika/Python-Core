# Create an abstract base Item and one concrete subclass Book:
# • Item requires get_summary(). • Book stores title, private _metadata dict, protected _available flag.
# Use properties to safely read metadata. • Include a shared catalog_tag and a way to update it globally.
# • Add a pricing method with a default parameter discount=0.
# • Include str and repr.
# • Add a small validator for metadata keys. Create books, print str/repr, update shared tag, shallow copy &
# deepcopy the book list and show differences.




nums = [12,15,7,18,20,21,25]
x = list(filter(lambda x :( x % 3 == 0 )^ (x % 5 == 0) , nums))
# print(x)


num = [12,15,7,18,20,21,25]
y = list(map(lambda x :round(( x *(9/5) + 32 ) , 2), num))
# print(y)

l = [12,15,7,18,20,21,25]
z = list(filter(lambda x : x % 3 == 0 , l))
# print(z)

from functools import reduce
l = [12,15,7,18,20,21,25]
# a = reduce(lambda x , y  : x +  y ,
#            (filter(lambda x : x % 3 != 0 , l)))
# print(a)


y = [12,15,7,18,20,21,25]
c = reduce(lambda a , b :a + b , filter(lambda x : x > 75 ,(map(lambda x : 3.14 * x * x, y))))
# print(c)


class Product:
    base_tax_rate = 5
    def __init__(self , name , base_price):
        self.name = name
        self.base_price = base_price

    def final_price(self):
        return Product.base_tax_rate * self.base_price
    @classmethod
    def change_Base(cls , new_value):
        cls.base_tax_rate = new_value
    @staticmethod
    def check(price):
        return price > 0 and price < 10000

# obj = Product("Milk" , 20)
# obj1 = Product("Bread" , 20)
# Product.change_Base(10)
# print(Product.base_tax_rate)
# print(Product.check(obj.final_price()))



def gen(l):
    max = 0
    for i in l:
        if i > max:
            max = i
        yield  max
l = [3,1,4,2]
# print(list(gen(l)))


class SmartLight:
    def __init__(self , room_name):
        self.room_name = room_name
        self.is_on = False
        self.brightness = 0
    def toggle(self):
        if not self.is_on:
            self.is_on = True
            self.brightness = 50
            print(f"{self.room_name} light is turned on")
        else:
            self.is_on = False
            self.brightness = 0
            print(f"{self.room_name} light is turned off")
    def set_brightness(self , level):
        if not self.is_on:
            print("Cannot Set the Brightness")
        elif 1 <= level <= 100:
            self.brightness = level
            print("")



# Create a CricketMatch class with:
# instance variables: team_name, runs, wickets
# instance method to update score
# class method to update stadium name
# static method to check winning score
#
# Use filter() for teams above winning score, map() for runs, and reduce() for total runs scored.
from functools import reduce
class CricketMatch:
    stadium_name = "Chepak"
    def __init__(self , team_name , runs , wickets):
        self.team_name = team_name
        self.runs = runs
        self.wickets = wickets
    def update(self,extra_runs):
        self.runs += + extra_runs
        return self.runs
    @classmethod
    def stadium(cls , new):
        cls.stadium_name = new
    @staticmethod
    def check(score):
        return score > 200
# obj = CricketMatch("RCB" , 225 , 5)
# obj2 = CricketMatch("CSK" , 215 , 4)
# obj3 = CricketMatch("RR" , 200 , 6)
# l = [obj , obj2, obj3]
# a = list(filter(lambda x : x.check(x.runs) , l))
# b= list(map(lambda x : x.runs , l))
# c = reduce(lambda x , y : x + y.runs, l , 0)
# for i in a :
#     print(i.team_name)
# print(b)
# print(c)


# Create a GymMember class with:
# instance variables: name, age, membership_fee
# instance method to renew membership
# class method to update gym name
# static method to check eligible members
#
# Use filter() for eligible members, map() for membership fees, and reduce() for total fee collection.


class GymMember:
    GymName = "ABC"
    def __init__(self , name , age , membership_fee):
        self.name = name
        self.age = age
        self.membership_fee = membership_fee
    def renew(self , add):
        self.membership_fee += add
        return self.membership_fee
    @classmethod
    def change(cls , new):
        cls.GymName = new
    @staticmethod
    def check(eligible):
        return eligible > 18

# obj = GymMember("Nandhini" , 21 , 2000)
# obj2 = GymMember("Vaishnavi" , 21 , 3000)
# obj3 = GymMember("Pavani" , 15 , 2000)
# l = [obj , obj2,obj3]
# a = list(filter(lambda x : x.check(x.age) , l))
# b = list(map(lambda x : x.membership_fee , l))
# c = reduce(lambda x , y : x + y.membership_fee , l , 0)
#
# print(list(map(lambda x : x.name , a)))
# print(b)
# print(c)



# Create a Flight class with:
# instance variables: flight_name, ticket_price, seats
# instance method to book seats
# class method to update airport name
# static method to check expensive flights
#
# Use filter() for expensive flights, map() for ticket prices, and reduce() for total ticket revenue.


class Flight:
    airport_name = "Hyderabad"
    def __init__(self , flight_name, ticket_price,seats):
        self.flight_name = flight_name
        self.ticket_price = ticket_price
        self.seats = seats
    def book(self , seats):
        self.seats += seats
    @classmethod
    def update(cls , new):
        cls.airport_name = new
    @staticmethod
    def check(exp):
        return exp > 20000
# obj = Flight("Indigo" , 5200 , 2)
# obj2 = Flight("Emirates" , 25000 , 6)
# obj3 = Flight("AirLines" , 2000 , 8)

# l = [obj , obj2 , obj3]
# a = list(filter(lambda x : x.check(x.ticket_price) , l))
# b = list(map(lambda x : x.ticket_price , l))
# c = reduce(lambda x , y : x + (y.seats * y.ticket_price) , l , 0)
#
# print(list(map(lambda x : x.flight_name , a)))
# print(b)
# print(c)




#
# Create a RestaurantItem class with:
# instance variables: item_name, category, price
# instance method to apply discount
# class method to update restaurant name
# static method to check special dishes
#



class RestaurantItem:
    name = "Zishann"
    def __init__(self , item_name, category, price):
        self.item_name = item_name
        self.category = category
        self.price = price
    def discount(self , d):
        self.price -= self.price * (d / 100)
        return self.price
    @classmethod
    def change(cls , new):
        cls.name = new
    @staticmethod
    def check(name):
        return name == "chicken"

obj = RestaurantItem("Panner" , "veg" , 250)
obj1 = RestaurantItem("chicken" , "Non-Veg" , 500)
obj2 = RestaurantItem("chicken" , "Non-Veg" , 520)
l = [obj , obj1 , obj2]

# Use filter() for special dishes, map() for item names, and reduce() for total menu price.

# a = list(filter(lambda x  : x.check(x.item_name) , l))
# b = list(map(lambda x : x.item_name , l))
# c = reduce(lambda x , y : x + y.price  , l , 0)
#
# print(list(map(lambda x : x.item_name , a)))
# print(b)
# print(c)



#
# Create a Course class with:
# instance variables: course_name, duration, fee
# instance method to apply scholarship
# class method to update institute name
# static method to check premium courses

class Course:
    name = "Vignan"
    def __init__(self , course_name, duration, fee):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee
    def apply(self , amount):
        self.fee -= amount
        return self.fee
    @classmethod
    def update(cls , new):
        cls.name =new
    @staticmethod
    def check(course):
        return course == "python"

obj = Course("python" , 2 , 20000)
obj2 = Course("java" , 3 , 25000)
obj3 = Course("python" , 3 , 20500)
#
# Use filter() for premium courses, map() for fees after scholarship, and reduce() for total fees.
#

# l = [obj , obj2 , obj3]
# a = list(filter(lambda x : x.check(x.course_name) , l))
# b = list(map(lambda x : x.apply(2500) , l))
# c = reduce(lambda x , y : x + y.fee , l , 0)
#
# print(list(map(lambda x : x.course_name , a)))
# print(b)
# print(c)

# Create a Bus class with:
# instance variables: bus_number, capacity, ticket_price
# instance method to calculate collection
# class method to update depot name
# static method to check deluxe buses

class Buses:
    depot = "kphb"
    def __init__(self,bus_number, capacity, ticket_price):
        self.bus_number = bus_number
        self.capacity = capacity
        self.ticket_price = ticket_price
    def calc(self):
        return self.capacity * self.ticket_price
    @classmethod
    def update(cls , new):
        cls.depot = new
    @staticmethod
    def check(price):
        return price > 800
obj = Buses(1984 , 20 , 154)
obj2 = Buses(8444 , 50 , 899)
obj3 = Buses(4444 , 45 ,700)
#
# l = [obj , obj2 , obj3]
# # Use filter() for deluxe buses, map() for ticket prices, and reduce() for total collection.
#
# a = list(filter(lambda x : x.check(x.ticket_price) , l))
# b = list(map(lambda x : x.ticket_price , l))
# c = reduce(lambda x , y : x + y.calc() , l , 0)
#
# print(list(map(lambda x : x.bus_number , a)))
# print(b)
# print(c)


l = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0]

# a = reduce(lambda x , y : x + y ,list(map(lambda x : x ** 2 , filter(lambda x : x % 2 == 0 , l))))
# print(a)





