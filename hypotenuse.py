from math import hypot
side1 = float(input("Enter first side of triangle: "))
side2 = float(input("Enter second side of triangle: "))
hypotenuse = hypot(side1,side2)
print("Hypotenuse of both sides {} and {} equals {:.2f}".format(side1,side2,hypotenuse))