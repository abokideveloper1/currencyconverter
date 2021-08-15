num = int(input("Enter any number you wish: "))
U = num // 1 % 10
T = num // 10 % 10
H = num // 100 % 10
TS = num // 1000 % 10
print("Analyzing number {}...".format(num))
print("Unit: {}".format(U))
print("Tens: {}".format(T))
print("Hundred: {}".format(H))
print("Thousand: {}".format(TS))