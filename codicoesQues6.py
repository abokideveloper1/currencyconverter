n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 > n2 and n1 > n3:
    print("{} is the biggest number".format(n1))
if n2 > n1 and n2 > n3:
    print("{} is the biggest number".format(n2))
if n3 > n1 and n3 > n2:
    print("{} is the biggest number".format(n3))
if n1 < n2 and n1 < n3:
    print("{} is the smallest number".format(n1))
if n2 < n1 and n2 < n3:
    print("{} is the smallest number".format(n2))
if n3 < n1 and n3 < n2:
    print("{} is the smallest number".format(n3))