real = float(input("Enter quantity of Brazilian Real money in your wallet: "))
print(" ")
print(" ======================= ")
usdollar = real * 0.19
audollar = real * 0.24
euro = real * 0.15
pound = real * 0.13
print("POSSESSING R$ {:.2f},YOU CAN BUY:\n US$ {:.2f} \n AU$ {:.2f} \n EU {:.2f} \n GB {:.2f} ".format(real,usdollar,audollar,euro,pound))
print(" ")
print(" ======================= ")