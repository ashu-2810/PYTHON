# OOPs Part 2
#del keyword
"""used to delete object properties or object itself"""
class Student():
    def __init__(self,name):
        self.name = name

s1 = Student("ashu")
print(s1.name)
del s1
# print(s1.name)

#private(like) attributes & methods
"""conceptual implementation in python  
    private attributes & methods are ment to be used only within the class and are not accessible from outside the class"""
class Account():
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no #public
        self.__acc_pass = acc_pass #private
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("ashua","12345")
print(acc1.acc_no)
acc1.reset_pass()

class Person:
    __name = "anonymous"  #private attribute
    def __hello(self):  #private method
        print("hello",self.__name)
    def welcome(self):
        self.__hello()

p1 = Person()
# p1.__hello()
# print(p1.__name)
p1.welcome()

#Inheritance
"""when one class(child/derived) derives the properties & method of another class(parent/base)"""
class Car:   #single Inheritance
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")
    
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
car1.start()
car1.stop()
print(car1.color)

#inheritance types
"""
    o single Inheritance
    o multi-level Inheritance
    o multiple Inheritance
"""
class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class C"
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#Super method
"""super() method is used to access methods of the parent class"""
class Car:
    def __init__(self,types):
        self.types = types
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")
    
class ToyotaCar(Car):
    def __init__(self,name,types):
        super().__init__(types)
        self.name = name
        super().start()

car1 = ToyotaCar("prius","electrical")
print(car1.types)

#class Method
"""a class method is bound to the class & receives the class as an implicit first argument
    Note:- static method cant access or modify class state & generally for utility"""
class Person:
    name = "anonymous"
    # def changeName(self,name):
    #     # self.name=name
    #     # Person.name=name
    #     # self.__class__.name="Rahul"
    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 =Person()
p1.changeName("Ashu")
print(p1.name)
print(Person.name)

#Property decorator
"""we use @property decotator on any method in the class to use the method as a property"""
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    #     self.percentage = str((self.phy+self.chem+self.math)/3)+"%"
    # def calculatePercentage(self):
    #     self.percentage = str((self.phy+self.chem+self.math)/3)+"%"

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

stu1 = Student(98,97,99)
print(stu1.percentage)
stu1.phy = 86
print(stu1.percentage)
stu1.phy = 90
print(stu1.percentage)

# stu1.calculatePercentage()
# print(stu1.percentage)

#Polymorphism:operator Overloading
"""when the same operator is allowed to have different meaning according to the context
    Operators & Dunder function
    a+b     # addition        a.__add__(b)
    a-b     #substraction     a.__sub__(b)
    a*b     #multiplication   a.__mul____(b)
    a/b     #division         a.__truediv____(b)
    a%b     #addition         a.__mod____(b)

    @getter
    @setter
"""
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    # def add(self,num2):
    def __add__(self,num2):
        newReal = self.real+num2.real
        newImg = self.img+num2.img
        return Complex(newReal,newImg)
    def __sub__(self,num2):
        newReal = self.real-num2.real
        newImg = self.img-num2.img
        return Complex(newReal,newImg)
    
num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(4,6)
num2.showNumber()
# num3 = num1.add(num2)
# num3.showNumber()
num3 = num1-num2
num3.showNumber()

#Define a circle class to create a circle with radius r using the constructor.
#Define an area()method of the class which calculates the area of circle
#Define a perimeter()method of the class which allow you to calculate the perimeter of the circle
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        print((22/7)*self.r**2)
    def perimeter(self):
        print(2*(22/7)*self.r)
c1 = Circle(21)
c1.area()
c1.perimeter()

#Define a Employee class with attributes role, department & salary this class also has a showdetails()method
#define a Engineer class that inherits properties from Employee & haas additional attributes: name & age
class Employee:
    def __init__(self,role,dep,sal):
        self.role= role
        self.dep = dep
        self.sal = sal
    def showdetails(self):
        print("role=",self.role,"\ndep=",self.dep,"\nsal=",self.sal)

e1 = Employee("head","it",100000)
e1.showdetails()

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","It",90000)

eng1 = Engineer("ashu",22)
eng1.showdetails()

#create a class called order which stores item & its price
#  use Dunder function __gt__() to convert that:
#order1>order2 if price of order1>price of order2
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price= price
    def __gt__(self,odr2):
        return self.price>odr2.price

odr1 = Order("chips",20)
odr2 = Order("tea",10)
print(odr1>odr2)