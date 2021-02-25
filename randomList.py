from random import choice
n1 = str(input("Enter 1st student's name: "))
n2 = str(input("Enter 2nd student's name: "))
n3 = str(input("Enter 3rd student's name: "))
n4 = str(input("Enter 4th student's name: "))
studentlist = [n1,n2,n3,n4]
randomvar = choice(studentlist)
print("STUDENT CHOSEN TO ERASE BLACKBOARD: {}".format(randomvar))