class A:
    def __init__(self , n):
        self.n = n
        self.c = 0
    def __iter__(self):
        return self
    def __next__(self):
           if self.c < self.n:
               self.c += 1
               print(self.c)
           else:
               raise StopIteration

# obj = A(5)
# for i in obj:
#     print(i)

class Even:
    def __init__(self , l):
        self.l = l
        self.c = 0
    def __iter__(self):
        return self
    def __next__(self):
        while(self.c < len(self.l)):
            val = self.l[self.c]
            self.c +=1
            if  val % 2 == 0:
                return val

        raise StopIteration


# obj = Even([1,2,3,4])
# print(list(obj))



class Reverse:
    def __init__(self , s):
        self.s = s
        self.done = False
    def __iter__(self):
        return self
    def __next__(self):
        if(not self.done):
            self.done = True
            return self.s[::-1]
        else:
            raise StopIteration

# obj = Reverse("Nandhini")
# print(list(obj))



class element:
    def __init__(self , l):
        self.l = l
        self.c = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.c < len(self.l):
            idx = self.c
            val = self.l[self.c]
            self.c += 1
            return val , idx
        raise StopIteration


# obj = element([1, 2 , 3, 4 ,5])
# for i in obj:
#     print(i)


def gen(num):
    for i in str(num):
        yield int(i)

# obj = gen(1234)
# for i in obj:
#     print(i)


def number_sum(l):
    c = 0
    s = 0
    while c < len(l):
        s += l[c]
        yield s
        c += 1
# obj = number_sum([1,2,3,4])
# for i in obj:
#     print(i)


def check_vowels(s):
    vowels = "aeiouAEIOU"
    for i in s:
        if i in vowels:
            yield i

# obj = check_vowels("Nandhini")
# for i in obj:
#     print(i)


class word:
    def __init__(self , s):
        self.s = s.split(" ")
        self.c = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.c < len(self.s):
            w = self.s[self.c]
            self.c += 1
            return w
        raise StopIteration

# obj = word("I am a Good Girl")
# for i in obj:
#     print(i)


class Even_String:
    def __init__(self , s):
        self.s = s
        self.c = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.c < len(self.s):
            ch = self.s[self.c]
            c = self.c
            self.c += 1
            if c % 2 == 0:
                return ch
        raise StopIteration

# obj = Even_String("Nandhini")
# for i in obj:
#     print(i)


def max_value(l):
    m = l[0]
    for i in l:
        if i > m:
            m = i
        yield m

# obj = max_value([4 , 3 , 2 ,1])
# for i in obj:
#     print(i)








