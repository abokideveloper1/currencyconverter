n1 = int(input("\033[1;30;42mEnter a 1st number:\033[m "))
n2 = int(input("\033[1;30;44mEnter a 2nd number:\033[m "))

if n1 > n2:
    print("That \033[1;30;42mfirst number\033[m is \033[1;30;45mlarger\033[m than that \033[1;30;44msecond number\033[m.")
elif n2 > n1:
    print("That \033[1;30;44msecond number\033[m is \033[1;30;45mlarger\033[m than that \033[1;30;42mfirst number\033[m.")
elif n1 == n2 and n2 == n1:
    print("\033[1;30;41mBoth inputs\033[m are about that \033[1;30;42msame number.\033[m")
else:
    print("\033[1;30;41mInvalid input\033[m")
