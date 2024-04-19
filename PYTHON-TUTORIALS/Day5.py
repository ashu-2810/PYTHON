#Loops (loops are used to repeat instructions)
"""
while loop
    syntax:-
    while condition:
        some work...
"""
count = 1
while (count <= 5):
    print("hello")
    count += 1

#print num from 1 to 5
idx = 1
while idx<=5:
    print(idx)
    idx+=1
print()
#print num from 5 to 1
idx = 5
while (idx >= 1):
    print(idx)
    idx-=1
print()

#print num from 1 to 100
idx = 1
while (idx<=100):
    print(idx)
    idx+=1
print()

#print num from 100 to 1
idx=100
while (idx>=1):
    print(idx)
    idx-=1
print()

#print the multiplication table of a number n
x = 5 #or int(input("table of : "))
idx=1
while(idx<=10):
    print(x," X ",idx," = ",(x*idx))
    idx+=1
print()

#print the elements of the following list using loop
x = [1,4,9,16,25,36,49,64,81,100]
l=len(x)
# print(l)
idx=0
while (idx < l):
    print(x[idx])
    idx+=1
print()

#search for a no x in this tuple using loop
tipu = (1,4,9,16,25,36,49,64,81,100)
x = 36
idx = 0
while (idx < len(tipu)):
    if(x == tipu[idx]):
        print("found",idx)
    idx+=1
print()

#break & continue
"""Break : used to terminate the loop when encountered.
    Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration."""
idx = 1
while (idx <= 5):
    if(idx == 4):
        break
    else:
        print(idx)
    idx+=1

idx = 1
while (idx <= 5):
    if(idx == 3):
        idx += 1
        continue
    print(idx)
    idx += 1
print()

# for loops( used for sequential traversal for traversing list, string, tuples, etc.)
lists = ["potato","bringal","ladyfinger","cucumber"]
for el in lists:
    print(el)
print()

tups = (1,2,3,4,5,7,2,9)
for el in tups:
    print(el)
else:
    print()

strs = "apnacharacter"
for el in strs:
    print(el)
else:
    print()

#print elements of list
listss = [1,4,9,16,25,36,49,64,81,100]
for el in listss:
    print(el)
else:
    print()

#search num x in tuple 
tupss = (1,4,9,16,25,36,49,64,81,100)
x = 36
for el in tupss:  #(linear search)
    if (el == x):
        print("found x ")
        break
else:
    print("x not found")

#range()
"""range function returns a sequence of numbers starting from 0(by default), and increments by 1(by default),and stops before a specified number
syntax:- range(start?, stop, step?)
"""
for el in range(5):
    print(el)
for el in range(2,10,2):
    print(el)
print()

#print num from 1 to 100
for el in range(1,101):
    print(el)
print()

#print num from 100 to 1
for el in range(100,0,-1):
    print(el)
print()

#print the multiplication table of a num n
n=5
for el in range(1,11):
    print(n*el)
print()

#pass statement
"""pass is a null statement that does nothing. it is used as a placeholder for future code"""
for i in range(5):
    pass
print("some work")

#wap to find the sum of first n num
n = 5
sum = 0
el = 0
while(el <= n):
    sum+=el
    el+=1
print(sum)

#wap to find the factorial of first n num
n = 5
fact = 1
for el in range(1,n+1):
    fact*=el
print(fact)

