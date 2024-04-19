#16 Strings & Conditional Statements
"""string is a data type that stores a sequence of characters"""
str1 = "this is a string.\nwe are creating it in\tpython."
print(str1)
#length of string
str2 = "hello"
print(len(str2))
#indexing
print(str2[0])
print(str2[1])
print(str2[2])
print(str2[3])
print(str2[4])
#slicing
print(str2[1:4])
#negative slicing
str4 = "apple"
print(str4[-3:-1])

#17 String Functions
str3 = "i am a coder."
print(str3.endswith("er."))
print(str3.capitalize())
print(str3.replace("coder", "developer"))
print(str3.find("coder"))
print(str3.count("am"))

# WAP to input user first name & print its length
firstName = "ashu choudhary" #or  str(input("Enter your name : "))
print(len(firstName))

#WAP to find the occurance of '$' in a String
String = "$hello i $am the $ymbol $99.99"
print(String.count("$"))

# 18 Conditional Statement
#WAP to check if a num entered by the user is odd or even
num1 = 23
if((num1%2)== 0):
    print("even")
else:
    print("odd")

#WAP to find the greatest of 3 no entered by the user
num1 = 2
num2 = 3
num3 = 4
if(num1 > num2 and num1 > num3):
    print(num1," is greater")
elif(num2 > num3):
    print(num2," is greater")
else:
    print(num3," is greater")

#WAP to check if a no is a multiple of 7 or not
num1 = 14
if((num1 %7) == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")
