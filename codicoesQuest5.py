from datetime import date
y = int(input("Enter year you want to analyze (enter 0 to analyze current year): "))
if y == 0:
    y = date.today().year
if y % 4 == 0 and y % 100 !=0 or y % 400 ==0:
    print("The year {} is a leap year".format(y))
else:
    print("The year {} isn't a leap year".format(y))