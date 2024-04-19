#Mini Projects

#Guess the Number
"""
import random
target = random.randint(1,100)
while True:
    num = input("guess the target or Quit(Q): ")
    if(num == "Q"):
        break
    num = int(num)
    if(num == target):
        print("correct guess!!")
        break
    elif(num > target):
        print("guess the smaller number!!")
    else:
        print("guess the greater number!!")

print("----GAME OVER----")
"""

#Random Password Generator
import random
import string
pass_len = 8
charVal = string.ascii_letters+string.digits+string.punctuation
# password = ""
# for el in range(pass_len):
#     password += (random.choice(charVal))
# print("your",pass_len,"length random password is :-> ",password)

#list comprehension
ranPass ="".join([(random.choice(charVal)) for el in range(pass_len)])
print("random Password: ",ranPass)