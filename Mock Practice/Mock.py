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


