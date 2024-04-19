#program to add two numbers
"""def sumofTwoNum():
    num1 = float(input("num1 : "))
    num2 = float(input("num2 : "))
    sum = num1 + num2
    print("the sum of ",num1,"and",num2,"is : ",sum)
sumofTwoNum()"""

#program to print hello world
"""def hello():
    return str("hello world")
print(hello())"""

#program to find the square root
"""def squareRoot():
    num1 = float(input("num1 : "))
    sqrts = num1**(1/2)
    return sqrts
print(squareRoot())"""

"""import math
num1 = 16
sr = math.sqrt(num1)
print(sr)"""

#program to calculate the area of triangle
"""def calcAreaOfTriangle():
    height = 12.5
    base = 5.5
    area = (1/2)*base*height
    print(area)
calcAreaOfTriangle()"""

#WAP to swap two variables
"""def swaping():
    x = 13
    y = 12
    print(x,y)
    temp = x
    x = y
    y = temp
    print(x,y)
swaping()"""

"""def swapp():
    x=13
    y =12
    print(x,y)
    x,y = y,x
    print(x,y)
swapp()"""

#WAP to convert km to miles
"""def kmTomiles():
    km = 100
    miles = km *(0.621371)
    print(miles,"miles")
kmTomiles()"""

#WAP to is num is positive or negative or 0
"""def checkNum():
    num = 12
    if(num > 0):
        print("positive num")
    elif(num < 0):
        print("negative num")
    else:
        print("the num is 0")
checkNum()"""

#WAP to check num is even or Odd
"""def checkOddEven():
    num = 11
    if((num%2) == 0):
        print("even number")
    else:
        print("odd number")
checkOddEven()"""

#WAP to check leap year
"""def checkLeapYear():
    year = 1600
    if(((year % 400) == 0) and ((year % 100) == 0)):
        print("leapyear")
    elif(year % 4 == 0 and year %100 !=0):
        print("leapyear")
    else:
        print("not a leap year")
checkLeapYear()"""

#WAP to find the largest among three numbers
"""def checklargest():
    num1 = 12
    num2 = 61
    num3 = 111
    if(num1 > num2 and num1 > num3):
        print("num1 : ",num1)
    elif(num2 > num1 and num2 > num3):
        print("num2 : ",num2)
    else:
        print("num3 : ",num3)
checklargest()"""

#WAP to check prime number
"""def checkPrime():
    num = int(input("num : "))
    if (num == 1 or num < 1):
        print("not prime")
        return
    check = 0
    for el in range(2,num):
        if(num % el == 0):
            check+=1
    if(check == 0 ):
        print("prime")
    else:
        print("not prime")
checkPrime()"""

#WAP to generate a random number
"""import random
def generateRandomNum():
    num = random.randint(1,6)
    print(num)
generateRandomNum()"""

#WAP to print all prime number
"""def checkPrime(num):
    check= 0
    for el in range(2, num):
        if(num % el == 0):
            check+=1
    if(check == 0):
        print(num,end=" ")
def printAllPrime():
    lower = int(input("lower value : "))
    upper = int(input("upper value : "))
    for el in range(lower,upper+1):
        checkPrime(el)
printAllPrime()"""

"""def printprime():
    lower = 2
    upper = 50
    for el in range(lower,upper+1):
        if el> 1:
            for le in range(2,el):
                if(el%le == 0):
                    break
            else:
                print(el,end=" ")
printprime()"""

#WAP to convert C to F
"""def celTOFer():
    C = int(input("enter celsius : "))
    F = (C * (9/5))+32
    print("fahrenheit : ",F)
celTOFer()"""

#WAP the factorial of the number
"""def findFact():
    num = int(input("Enter num! : "))
    fact = 1
    if(num >= 0):
        for el in range(1,num+1):
            fact *=el
        print(fact)
    else:
        print("incorect value")
findFact()"""
#using recurssion
"""def recFact(num):
    if(num == 0):
        return 1
    else:
        return (num *recFact(num-1))
num = int(input("enter num : "))
result = recFact(num)
print(result)"""

#WAP to print multiplication table
"""def table():
    num = int(input("num : "))
    for el in range(1,11):
        print(num,"X",el,"=",(num*el))
table()"""

#WAP to print fibonacci sequence
"""def fibonacci():
    num = int(input("enter range to print fabonacci : "))
    a = 0
    b = 1
    if (num == 1):
        print(a)
    else:
        print(a,b,end=" ")
    for el in range(1,num-1):
        c = a+b
        a = b
        b = c
        print(c,end=" ")
fibonacci()"""

#WAP to check armstrong number or not
"""def armstrongNum():
    num = int(input("enter the number to check armstrong number : "))
    lengthOfNumber = len(str(num))
    sum = 0
    temp = num
    while temp>0:
        digit = temp%10
        sum +=digit**lengthOfNumber
        temp = temp//10
    if(sum == num):
        print(sum,"is an armstrong number")
    else:
        print(num,"is not an armstrong number")
armstrongNum()"""

#WAP to print armstrong numers
"""def allArmstrongnum():
    lower = 100
    upper = 10000
    for el in range(lower,upper+1):
        lengthofnum = len(str(el))
        sum  = 0 
        temp = el        
        while temp >0:
            digit = temp %10
            sum+=digit**lengthofnum
            temp//=10
        if(el == sum):
            print(el,end=" ")
allArmstrongnum()"""

#WAP to find the sum of natural num
"""def sum_of_numbers():
    num = 15
    if(num<0):
        print("negative num not allowed")
    else:
        sum = 0
        while num>0:
            sum+=num
            num-=1
        print(sum)
sum_of_numbers()"""

#WAP to display powers of 2 using anonymous function
#LAMBDA function
"""nterms = int(input("no of terms : "))
result = list(map(lambda x : 2 ** x, range(nterms+1)))
print(result)
for el in range(1,nterms+1):
    print(result[el])"""

#WAP to find num divisible by another num
"""def num_divisible_Bynum():
    n = int(input("enter the num : "))
    for i in range(1,100):
        if((i%n) == 0):
            print(i)
num_divisible_Bynum()"""

"""def num_divisible_Bynum():
    lst = [39,48,26,98,33,67,87,52]
    result  = list(filter(lambda x : x%13 == 0,lst))
    print(result)
    for i in range(len(result)):
        print(result[i])
num_divisible_Bynum()"""

#WAP to convert decimal to binary, octal and hexadecimal
"""def numconverter():
    num = 12.12
    decnum = int(num)
    print("the decimal number is :",num)
    print("the num in binary :",bin(decnum))
    print("the num in octal :",oct(decnum))
    print("the num in hexadecimal :",hex(decnum))
numconverter()"""

#WAP to find Ascii value
"""def ascii_val():
    char = "1"
    print("the ascii value is : ",ord(char))
ascii_val()"""

#WAP to find HCF(highest common factor) or GCD(greatest common diviser)
def hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if(((x%i) == 0)and ((y%i) == 0)):
            hcf = i
    return hcf
x=12
y=30
print("hcf: ",hcf(x,y)) 