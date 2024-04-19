#List & Tuples

#List ( A built-in data type that stores set of values. , it can store elements of diffrent types(integer, float, string, etc.))
marks=[94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
#indexing
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
#length of list
print(len(marks))
#list are mutable(list can be change)
marks[3] = 92.4
print(marks)
#list Slicing
print(marks[1:4])
#negative Slicing
print(marks[-4:-2])

#List Methods
first = [2, 1, 3]
print(first)
first.append(4)
print(first)
first.sort()
print(first)
first.sort(reverse = True)
print(first)
first.reverse()
print(first)
first.insert(0, 0)
print(first)
first.remove(4)
print(first)
first.pop(2)
print(first)

#Tuples( a built-in data type that lets us create immutable sequences of values)
tup = (87, 67, 33, 96, 76, 33)
print(tup)
#indexing
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
#slicing
print(tup[1:3])

#tuple Method
print(tup.index(33)) #it give first occurance
print(tup.count(33)) #it counts how many time 33 is in the Tuple

#WAP to ask the user to enter names of their 3 favorite movies & store them in a list
"""mov1 = input("movie 1 : ")
mov2 = input("movie 2 : ")
mov3 = input("movie 3 : ")
movies = []
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)"""
# OR
"""movies=[]
mov=input("movie 1 : ")
movies.append(mov)
mov=input("movie 2 : ")
movies.append(mov)
mov=input("movie 3 : ")
movies.append(mov)
print(movies)"""
# OR
"""movies = []
movies.append(input("movie 1 : "))
movies.append(input("movie 2 : "))
movies.append(input("movie 3 : "))
print(movies)"""

#WAP to check if a list contains a palindrome of elements, hint: use copy() method
pal = [1, 2, 3, 2, 1]
pal2 = pal.copy()
pal2.reverse()
if(pal == pal2):
    print("palindrome")
else:
    print("not palindrome")

#WAP to count the number of students with the "A" grade in tuple 
grades = ("C","D","A","A","B","B","A")
print("total grade A count is : ",grades.count("A"))

#WAP sort grades from "A" to "D" store it in list
grades = ["C","D","A","A","B","B","A"]
grades.sort()
print(grades)