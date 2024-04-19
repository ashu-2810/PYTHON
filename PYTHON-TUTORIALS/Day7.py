#File I/O 
"""python can be used to perform operations on a file(read & write data)
Types of file
1. Text files : .txt, .docx, .log, etc
2. Binary Files : .mp4, .mov, .png, .jpeg, etc
"""
#Open, read & close File
"""we have to open a file before reading or writing"""
# f = open("demo.txt","r") #read mode
# data =f.read(5)
# data =f.read()
# print(data)
# print(type(data))
# line1 = f.readline()
# print(line1)
# f.close()
""" 
"r" - open for reading(default)
"w" - open for writing, all data get deleted and the you can overwrite
"x" - create a new file and open it for writing
"a" - open for writing, appending to the end of the file if it exists
"b" - binary mode
"t" - text mode(default)
"+" - open a disk file for updating(reading and writing)
"""

#writing to a file
# by using "w"

#with Syntax
with open("demo.txt","w") as f:
    f.write("hello this is deleted file means all data has been deleted")
with open("demo.txt","r") as f:
    data = f.read()
    print(data)


#deleting a file
"""using the os module
    Module (like a code library) is a file written by another programmer that generally has functions we can use
    # - > import os
    # - > os.remove(filename)
    """
""" to install new module write
    -> pip install tensorflow
    or
    -> pip3 install tensorflow"""
import os
os.remove("demo.txt")

#create a file "practice.txt"using python add the data in it
"""
    Hi everyone
    we are learning File I/O
    using Java.
    I like programming in Java
"""
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java\n")

#WAF that replace all occurance of "java" with "python" in practice.txt file
with open("practice.txt","r")as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#search if the word "learning" exist in the file or not
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("found")
    else:
        print("not found")

#WAF to find which line of the file does the word "learning" occur first. print -1 if word not found
def search_word(word):
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")
search_word("learning")
def check_for_line(word):
    with open("practice.txt","r")as f:
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1
    return -1
check_for_line("learning")

#from a file containing numbers seperated by comma, print the count of even numbers.
import os
os.remove("practice.txt")

with open("practice.txt","w") as f:
    data = f.write("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30")

count = 0
with open("practice.txt","r") as f:
    data = f.read()
    """num = ""
    for el in range(len(data)):
        if(data[el]==","):
            print(int(num))
            num=""
        else:
            num+=data[el]"""
    num = data.split(",")
    for el in num:
        if((int(el) %2) == 0):
            count+=1
print(num)
print(count)

os.remove("practice.txt")