#1 print any thing
print("hello world","my age is 23")
print( 23, 35, 35 + 23 )

#2 variables(a variables is a name given to a memory location in a program)
name = "Ashu"
age = 23
price = 25.99
print(name, age, price)
old = False
a=None
#3 type of the values of the variables
#  Data Types(integers, string, float, boolean, none)
print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(a))

#4 keywords(reserved words in python)

#5 print sum
a = 2
b = 5
sum = a + b
print(sum)

#6 type of tockens
# punctuators (punctuators are symbols to organize sentance structure in programming like (), {}, [], @, #, etc.)

#7 expression execution
#(string & numeric values can operate together with *)
A,B = 2,3
Text = "@"
print(2*Text*3)
#(string & string can operate with *)
A,B="2",3
Txt = "@"
print((A+Txt)*B)
#(numeric values can operate with all arithmetic operators)
A,B=2,3
C=4
print(A+B*C)
#(arithmetic expression with integer and float will result in float)
A,B=10,5.0
C=A*B
print(C)
#(result of division operator with two integer will be float)
A,B=1,2
C=A/B
print(C)
#(integer division with float and int will give int displayed as float)
A,B=1.5,3
C=A//B
print(C,A/B)
#(remainder is negative when denominator is negative)
A,B=-5,2
C=A%B
print(C)

#8 comments in python
""" This is 
    multi line  
        comment"""

#9 input in python
""" input() statement is used to accept values( using keyword) from user

# string input
name = input("name : ")

# int input
age = int(input("age : "))

# float input
price = float(input("price : "))

"""


#10 practice time (F, T, T, F, T) ( a. True)

#11 Conditional statements (if-elif-else)
light = "red" # or input("light : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken! ")

marks = 92 #or  int(input("marks: "))
if(marks >= 90):
    print("A")
elif(marks >=80 and marks < 90):
    print("B")
elif(marks >=70 and marks < 80):
    print("C")
else:
    print("D")

#12 ternary operator
food = "cake" #or  input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)

print("YES") if food == "cake" else "NO"

#13 clever if
age= 21 #or  int(input("age : "))
vote = ("yes","no") [age >= 18]
print(vote)

# Simple Intrest
p = 20000
r = 10
t = 3
si = (p*r*t)/100
print(si)

# 14 types of operators
"""
o Arithmetic Operators(+, -, *, /, %, **)
o Relational / Comparision Operators(==, !=, >, <, >=, <=)
o Assignment Operators(=, +=, -=, *=, /=, %=, **=)
o Logical Operators(not, and, or)
"""

#15 type Conversion
a,b=1,2.0
sum=a+b
print(sum)
#manual type-casting
c=int(b)
sum=a+c
print(sum)

# WAP to input 2 num & print their sum
"""num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
sum = num1 + num2
print("sum : ",sum)"""

#WAP to input side of a square & print its area
"""side = float(input("side : "))
area = side ** 2
print("area : ",area)"""

#WAP to input 2 float num & print their average
"""num1 = float(input("num1 : "))
num2 = float(input("num2 : "))
average = (num1 + num2) / 2
print("average : ",average)"""

#WAP to input 2 int num print true if num1 >= num2 False if not
"""num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
if(num1 >= num2):
    print("True")
else:
    print("False")"""
