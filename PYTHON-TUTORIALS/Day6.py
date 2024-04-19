#Function & Recursion
"""function is a block of statement that perform a specific task"""
def sum(a,b):
    return (a+b)
print(sum(5,4))

def printHello():
    print("hello")
printHello()
printHello()
printHello()
printHello()

#average of three no
def avg(num1,num2,num3):
    avg = (num1+num2+num3)/3
    return avg
average = avg(2,3,4)
print(average)

#Built-in function & User Defined Function
#Built-in Function (print(), len(), type(), range(), etc.)
#User Defined Function (avg(), sum(), as created above)

#Default parameters : assigning a default value to parameter, which is used when no argument is passed
def calcMul(a=1,b=2):
    print(a*b)
    return a*b
calcMul()

#WAP to print the length of a list
lenlist = [1,2,3,4,5,6,7,8]
def lenOfList(lenlist): #how len() function works
    count = 0
    for el in range(len(lenlist)):
        count+=1
    return count
count = lenOfList(lenlist)
print("length of list is : ",count)

#WAP to print the elements of a list in a single line
num = [1,2,3,4,5,6,7,8,9]
def nums(num):
    for el in range(len(num)):
        print(num[el],end=" ")
nums(num)
print()
#WAP to find the factorial of n 
def fact(n):
    facto = 1
    for el in range(1,n+1):
        facto*=el
    return facto
numfact = fact(5)
print(numfact)

#WAP to convert usd to inr(1usd = 83rs)
usd = 2
def USD_to_INR_Converter(usd):
    return (usd*83)
inr = USD_to_INR_Converter(usd)
print(inr)

#WAP to take input if odd print odd if even print even
n = 12 #or int(input("Enter number : "))
def check_odd_even(n):
    if((n%2)== 0):
        print("EVEN")
    else:
        print("ODD")
check_odd_even(n)

#Recursion 
"""when a function call itself repeatedly"""
def show(n):
    if(n == 0): #Base case (stopping condition)
        return
    show(n-1)
    print(n)
show(5)

# factorial using recursion
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)
nr = fact(5)
print(nr)

#WAP recursive fuction to calculate the sum of first n numbers
def rec_sum(n):
    if(n == 0 ):
        return 0
    return rec_sum(n-1) + n
print(rec_sum(10))

#WAP to print all elements in a list using recursive function(list & index are parameter)
def print_list(lists,idx = 0):
    if (idx == len(lists)):
        return
    print(lists[idx])
    print_list(lists,idx+1)
lists = ["mango","lichi","apple","banana","grapes"]
print_list(lists)