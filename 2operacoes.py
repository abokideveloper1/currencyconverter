n1 = int(input("Enter first value: "))
n2 = int(input("Enter second value: "))

s = n1+n2
m = n1-n2
mt = n1*n2
d = n1/n2
ed = n1//n2
r = n1%n2
sqrt = n1 ** n2

print("The sum equals {},\n subtraction equals {}, \n multiplication equals {}, \n float division equals {}, \n integer division equals {}, \n remainder equals {} \n  ".format(s,m,mt,d,ed,r),end=" ")
print("Square equals {} \n ".format(sqrt),end=" ")
print("Square shortened to three float: {:3f}".format(sqrt))
