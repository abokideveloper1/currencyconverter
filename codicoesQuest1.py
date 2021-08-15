from random import randint
from time import sleep
computer = randint(0,5)

print("-=-" * 20)
print("I thought about some number between 0 and 5,try to guess... ")
print("-=-" * 20)
n = int(input("What number did i think about?: "))
print("processing".upper())
sleep(3)

if n == computer:
    print("You're right,i thought about {}".format(computer))
else:
    print("You wronged it,i thought about {} instead of {}".format(computer,n))