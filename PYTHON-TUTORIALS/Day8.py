#OOPS(Object oriented programming system)
"""to map with real world scenarios, we started using objects in code
This is called object oriented programming"""

#Class & objects
"""class is a blueprint for creating objects"""
#creating class
class Student:
    name = "karan"
#creating object(instance)
s1 = Student()
print(s1.name)

class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

#__init__ function
"""constructor
    all classes have a function called __init__(), which executed when the class is being initiated"""
class Student:
    name = "karan"
    def __init__(self,name,marks):
        # print(self) # refers to object(s1)
        self.name=name
        self.marks=marks
        print("adding new student in databases..")
    
s1 = Student("karan",97)
print(s1.name,s1.marks)
s2 = Student("arjun",88)
print(s2.name,s2.marks)
"""the self parameter is a refrence to the current instance of the class, and is used to access variables that belongs to the class"""

#class & instance(object) Attributes

#Methods
"""methods are function that belong to objects"""
class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome student",self.name)
    def getmarks(self):
        return self.marks

s1 = Students("arjun",97)
s1.welcome()
print(s1.getmarks())

#create student class that takes name & marks of 3 subjects as arguments in constructor then create a method to print the average
class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for el in self.marks:
            sum += el
        print("hi",self.name,"your avg score is ",(sum/3))

s1 = Student("tony stark",[99,97,98])
s1.avg()

#Static Method
"""methods that dont use self parameter(work at class level)
    Decorators allows us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it"""
class St():
    @staticmethod #decorators
    def hello():
        print("hello everyone")
S1 = St.hello()
#four pillars of OOPs(abstraction, encapsulation, inheritance, polymorphism)
#Abstraction
"""hiding the implementation details of a class and only showing the essential features to the user"""
class Car:
    def __init__(self):
        self.acc= False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started")
car1 = Car()
car1.start()
#Encapsulation
"""wrapping data and functions into a single unit(object)"""

#create account class with attribute balance & account no. create method for debit, credit & printing the balance
class Account():
    def __init__(self,bal,accno):
        self.balance = bal
        self.acclno = accno
    #debit method
    def debit(self,ammount):
        self.balance -= ammount
        print("Rs.",ammount,"was debited")
        print("total balance = ",self.bal())
    #credit method
    def credit(self,ammount):
        self.balance += ammount
        print("Rs.",ammount,"was credited")
        print("total balance = ",self.bal())
    #print balance
    def bal(self):
        return self.balance

acc1 = Account(10000,12345)
# print(acc1.balance,acc1.accno)
acc1.debit(1000)
acc1.credit(500)
