n = int(input("Enter a number: "))
r = n % 2

if r == 0:
    print("{} is an even number".format(n))
else:
    print("{} is an odd number".format(n))