v = float(input("Enter car velocity: "))
charge = (v - 80) * 7.00
if v > 80:
    print("You surpassed maximum velocity of 80 km/h,it is demanded that you pay a charge of R$ {:.2f}".format(charge))
else:
    print("Have a good day!,drive safe!")