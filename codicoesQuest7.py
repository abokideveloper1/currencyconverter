s = float(input("Enter your salary: "))

if s <= 2150.00:
    d = s + (s * 15 / 100)
else:
    d = s + (s * 10 / 100)

print("You were earning R$ {:.2f},but for now you'll earn R$ {:.2f}".format(s,d))