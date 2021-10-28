print("Alexandre's stores".upper())
print("=="*10)

p = float(input("Enter total price of shopping: "))
print("Press [1] for paying through cash/cheque")
print("Press [2] for paying through 2 installments")
print("Press [3] for paying through 3 installments")
print("Press [4] for paying through credit card cash")
c = int(input("Choose an option: "))
print(" ")

if c == 1:
    d = p * 10/100
    tp = p - d;
    print("Price: {:.2f}".format(p).upper())
    print("Price with discount: {:.2f}".format(d).upper())
    print("Total to pay: {:.2f}".format(tp).upper())
elif c == 2:
    r = p/2;
    print("Price: {:.2f}".format(p).upper())
    print("Double installments price: {:.2f}".format(r).upper())
    print("Total to pay: {:.2f}".format(p).upper())
    print("Total to pay through double installments: {:.2f}".format(r).upper())

elif c == 3:
    r = p/3
    tp = p - r
    print("Price: {:.2f}".format(p).upper())
    print("Triple installments price: {:.2f}".format(r).upper())
    print("Total to pay: {:.2f}".format(tp).upper())
    print("Total to pay through triple installments: {:.2f}".format(r).upper())

elif c == 4:
    i = int(input("Enter through how many installments do you wish to pay: "))
    r = p/i
    if i == 1:
        d = p * 5/100
        tp = p - d

        print("Price: {:.2f}".format(p).upper())
        print("Total to pay: {:.2f}".format(tp).upper())
        print("Total to pay through {}x installments: {:.2f}".format(i,d).upper())
    if i == 2:
        print("Price: {:.2f}".format(p).upper())
        print("{}x installments price: {:.2f}".format(i, r).upper())
        print("Total to pay: {:.2f}".format(p).upper())
        print("Total to pay through {}x installments: {:.2f}".format(i, r).upper())
    else:
        r = p * 20/100
        t = p + r
        print("Price: {:.2f}".format(p).upper())
        print("{}x installments price: {:.2f}".format(i, r).upper())
        print("Total to pay: {:.2f}".format(p).upper())
        print("Total to pay through {}x installments with extra tax: {:.2f}".format(i, t).upper())




else:
    print("Invalid option!".upper())
