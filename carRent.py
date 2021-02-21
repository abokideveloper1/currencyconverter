days = int(input("Enter days of rent period: "))
km = float(input("Enter how many km's did this car run: "))
days_price = 60 * days
km_price = 0.15 * km
total_price = days_price + km_price
print("The rent costs:{:.2f}".format(total_price))