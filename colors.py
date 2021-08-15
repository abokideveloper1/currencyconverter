print("\033[1;31;43mHello world!\033[m")
print("\033[4;30;45mHello world!")
print("\033[7;30mHello world!\033[m")
print("\033[0;33;44mHello world!\033[m")
print("\033[7;33;44mHello world!\033[m")
a = 3
b = 5
print("The variables are outputting \033[32m{}\033[m and \033[31m{}\033[m respectively".format(a,b))
print("The variables are outputting \033[32;44m{}\033[m and \033[31;44m{}\033[m respectively".format(a,b))
name = "Alexandre"
print("Hello nice to meet you,my name is {}{}{}!!!".format("\033[4;34m",name,"\033[m"))
print("Hello nice to meet you,my name is {}{}!!!".format("\033[4;34m",name))
colors = {"Clean":"\033[m","Blue":"\033[34m","Yellow":"\033[33m","Black and White":"\033[7;30m"}
print("Hello nice to meet you,my name is {}{}{}!!!".format(colors["Black and White"],name,colors["Clean"]))
