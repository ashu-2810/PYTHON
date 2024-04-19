# Dictionary & Set
"""Dictionaries are used to store data values in key:value pair
    they are unordered, mutable(changeable) & dont allow duplicate keys"""
info = {
    "name" : "ashu",
    "age" : 35,
    "adult" : True,
    "marks" : 94.4,
    "subjects" : ["python", "C", "C++", "Java"],
    "topics" : ("dict", "set")
}
print(info)
#accessing the values
print(info["name"])
print(info["adult"])
print(info["subjects"])
print(info["topics"])
#reassign 
info["name"] = "Nehal Choudhary"
print(info)
#nesting Dictionaries
student = {
    "name" : "ashu",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
print(student["subject"]["math"])

#Dictionary Methods
# student.key()
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
# student.values()
print(student.values())
# student.items()
print(student.items())
#student.get("key")
print(student.get("subject"))
print(student.get("name"))
#student.update(newstudent)
student.update({"city" : "ranchi"})
print(student)

#set
"""set is the collection of the unordered items.
    set is mutable but its element are immutable
    each element in the set must be unique & immutable"""
coll = {1, 2, 2, 2, "hello", "world", "hello"}
print(coll)
print(len(coll))
#empty set
collec = set()
print(type(collec))

#set method
coll.add(3)
print(coll)
coll.remove(3)
print(coll)
print(coll.pop())
print(coll.pop())
coll.clear()
print(coll)
coll1 = {1,2,3}
coll2 = {3,4,5}
print(coll1.union(coll2))
print(coll1.intersection(coll2))

# store word meaning in dictionary
dict1 = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"
}
print(dict1)

#given a list of subject for students. one classroom is required for 1 subject. how many classroom are needed by all student
subject = {"python", "java", "C++", "python","javascript","java","python","java","C++","C"}
print("no of class needed is : ",len(subject))

#WAP to enter marks of 3 sub from the user and store them in a dictionary. start with empty dictionary & add one by one use subject name as key & marks as value
"""sub = {}
x = int(input("phy : "))
y = int(input("chem : "))
z = int(input("maths : "))
sub.update({"phy" : x, "chem" : y, "maths" : z})
print(sub)"""

#WAP to store 9 & 9.0 as seprate values in the set (with help of built-in data types)
values = {("folat",9.0),("int",9)}
print(values)