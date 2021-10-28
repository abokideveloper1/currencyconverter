from datetime import date
by = int(input("Enter your \033[1;32;40m birth year\033[m: "))
cy = date.today().year
a = cy - by
if a <= 9:
    print("You are \033[1;33;40m{} years old\033[m".format(a))
    print("So you're a \033[1;35;40mCHILD category athlete\033[m.")
elif a <= 14:
    print("You're \033[1;33;40m{} years old\033[m.".format(a))
    print("So you're a \033[1;36;40mYOUNGSTER category athlete\033[m.")
elif a <= 19:
    print("You're \033[1;33;40m{} years old.\033[m".format(a))
    print("So you're a \033[1;34;40mJUNIOR category athlete\033[m. ")
elif a <= 25:
    print("You're \033[1;33;40m{} years old\033[m.".format(a))
    print("So you're a \033[1;32;40mSENIOR category athlete\033[m.")
else:
    print("You're \033[1;33;40m{} years old\033[m.".format(a))
    print("So you are a \033[1;31;40mMASTER category athlete\033[m.")
