n = int(input("Enter a number: "))
o = int(input("Enter a number for option: "
"\033[1;30;42m[1]binary\033[m,\033[1;30;44m[2]octagonal\033[m,\033[1;30;45m[3]hexadecimal\033[m: "))

if o ==1:
    print("That number \033[1;30;43m{}\033[m if converted to \033[1;30;42mBINARY\033[m equals \033[1;30;41m{}\033[m".format(n,bin(n)))
elif o ==2:
    print("That number \033[1;30;43m{}\033[m if converted to \033[1;30;44mOCTAGONAL\033[m equals \033[1;30;41m{}\033[m".format(n,oct(n)))
elif o ==3:
    print("That number \033[1;30;43m{}\033[m if converted to \033[1;30;45mHEXADECIMAL\033[m equals \033[1;30;41m{}\033[m".format(n,hex(n)))
else:
    print("\033[1;30;41mInvalid input for number option\033[m")