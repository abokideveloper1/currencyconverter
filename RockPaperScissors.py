from random import randint
from time import sleep
randomise = randint(0,2)
options = ("Rock","Paper","Scissors")
print("There is your choices: ")
print("[0] - rock".upper())
print("[1] - paper".upper())
print("[2] - scissors".upper())
player = int(input("Enter your choice: "))
print("You choose {} as your try".format(options[player]))
print("But computer has randomised its choice try as {}".format(options[randomise]))
print("jo".upper())
sleep(1)
print("ken".upper())
sleep(1)
print("po!!!".upper())

if player == 0 and randomise == 1:
    print("-=-"*10)
    print("So you win!!!".upper())
    print("-=-"*10)
elif player == 2 and randomise == 1:
    print("-=-"*10)
    print("So you win!!!".upper())
    print("-=-"*10)
elif player ==0 and randomise ==0:
    print("-=-"*10)
    print("there is a tie".upper())
    print("-=-"*10)
elif player == 1 and randomise == 1:
    print("-=-"*10)
    print("there is a tie".upper())
    print("-=-"*10)
elif player == 2 and randomise == 2:
    print("-=-"*10)
    print("there is a tie".upper())
    print("-=-"*10)
elif player == 1 and randomise == 0:
    print("-=-"*10)
    print("So computer wins!!!".upper())
    print("-=-"*10)
elif player ==1 and randomise == 2:
    print("-=-"*10)
    print("So computer wins!!!".upper())
    print("-=-"*10)
elif player == 0 and randomise == 2:
    print("-=-"*10)
    print("So you win!!!".upper())
    print("-=-"*10)
elif player == 2 and randomise == 0:
    print("-=-"*10)
    print("So computer wins!!!".upper())
    print("-=-"*10)

