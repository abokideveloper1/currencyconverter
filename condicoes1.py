s1 = float(input("Enter first score: "))
s2 = float(input("Enter second score: "))
a = (s1+s2)/2
print("Your average score is {:.2f}".format(a))

if a >= 6.0:
    print("Your score is good! CONGRATULATIONS!")
else:
    print("Your score isn't that good at all!,you need to study more!")