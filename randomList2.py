from random import shuffle
n1 = str(input("Enter 1st name: "))
n2 = str(input("Enter 2nd name: "))
n3 = str(input("Enter 3rd name: "))
n4 = str(input("Enter 4th name: "))
list1 = [n1,n2,n3,n4]
shuffle(list1)
print("Presentation sequence will be that \n {}".format(list1))