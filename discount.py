price = float(input("What's the price of product?: "))
discountvalue = int(input("Enter the percentage of discount you want: "))
discount = (discountvalue/100) * price
pricediscount = price - discount
print("The {} % discount for this product equals {:.2f} based on a price of {:.2f} ".format(discountvalue,pricediscount,price))