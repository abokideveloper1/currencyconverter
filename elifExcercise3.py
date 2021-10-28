from datetime import date
c = date.today().year
b = int(input("Enter your birth year: "))
s =
a = c - b
print("Who was born in \033[1;30;42m{}\033[m is \033[1;30;43m{} years old\033[m in \033[1;30;44m{}\033[m".format(b,a,c))
if a == 18:
    print("You must enlist IMMEDIATELY")
elif a < 18:
    r = 18 - a
    ey = c + r
    print("There is \033[1;30;44m{} years remaining\033[m for you to enlist".format(r))
    print("Your enlistment will happen on year of \033[1;30;42m{}\033[m".format(ey))
elif a > 18:
    r = a - 18
    ey = c - r
    print("You should be enlisted \033[1;30;44m{} years ago\033[m".format(r))
    print("Your enlistment happened on year of \033[1;30;42m{}\033[m".format(ey))
