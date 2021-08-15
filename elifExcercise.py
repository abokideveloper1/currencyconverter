p = float(input("Enter price of estate: "))
s = float(input("Enter your salary value: "))
y = int(input("Enter that much of years you want to pay parcels: "))
parcel = p / (y * 12)
percent = s * 30 / 100;
if parcel<=percent:
    print("Your estate will cost \033[1;30;44m{}\033[m,but with financing it will cost monthly parcels of \033[1;30;44m{}\033[m within \033[1;30;44m{} years period\033[m".format(p,parcel,y))
    print("\033[1;33;42mCongratulations,your financing has been approved!".upper())
else:
    print("Your estate will cost \033[1;30;44m{}\033[m,but with financing it will cost monthly parcels of \033[1;30;44m{:.2f}\033[m within \033[1;30;44m{} years period\033[m".format(p,parcel,y))
    print("\033[1;33;41mSorry,but your financing hasn't been approved!\033[m".upper())
