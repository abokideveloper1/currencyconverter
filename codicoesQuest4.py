d = float(input("Enter travel distance: "))
k = 0.50 * d

if d > 200.00:
    k = (0.50 - 0.05) * d

print("You are about to begin a travel of {:.2f} kilometers".format(d))
print("And the price of travel costs R$ {:.2f}".format(k))