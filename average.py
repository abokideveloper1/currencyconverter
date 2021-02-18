n1 = float(input("Enter first score: "))
n2 = float(input("Enter second score: "))
n3 = float(input("Enter third score: "))
n4 = float(input("Enter fourth score: "))
n5 = float(input("Enter fifth score: "))
n6 = float(input("Enter sixth score: "))
n7 = float(input("Enter seventh score: "))
n8 = float(input("Enter eighth score: "))
exam1 = float(input("Enter first exam score: "))
exam2 = float(input("Enter second exam score: "))
bimester1 = n1+n2+n3+n4+exam1
bimester2 = n5+n6+n7+n8+exam2
average = (bimester1+bimester2) / 2
print("AVERAGE: {}".format(average))
