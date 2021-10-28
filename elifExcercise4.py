s1 = float(input("Enter \033[1;30;42m1st exam score:\033[m "))
s2 = float(input("Enter \033[1;30;43m2nd exam score:\033[m "))
a = (s1+s2)/2
if a > 7.0:
    print("Getting following scores: \033[1;30;45m{:.1f}\033[m , \033[1;30;45m{:.1f}\033[m and averange of \033[1;30;45m{:.1f}\033[m,this leads you to be \033[1;30;42mAPPROVED\033[m".format(s1,s2,a))
elif a > 5.0 and a < 7.0:
    print("Getting following scores: \033[1;30;45m{:.1f}\033[m , \033[1;30;45m{:.1f}\033[m and averange of \033[1;30;45m{:.1f}\033[m,this leads you to \033[1;30;43mRETAKE THAT EXAM\033[m".format(s1,s2,a))
elif a < 5.0:
    print("Getting following scores: \033[1;30;45m{:.1f}\033[m , \033[1;30;45m{:.1f}\033[m and averange of \033[1;30;45m{:.1f}\033[m,this leads you to be \033[1;30;41mREPROVED\033[m".format(s1,s2,a))
