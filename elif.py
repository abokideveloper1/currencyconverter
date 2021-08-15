name = str(input("What's your name?: "))

if name == "Alexandre":
    print("You have such a beautiful name")
    print("Have a good day {}!".format(name))
elif name == "Gustavo":
    print("Your name is such a common name!")
    print("Have a good day {}!".format(name))
elif name == "Roshni" or name == "Priyanka" or name == "Puja":
    print("These lovely name is such a common one in India")
    print("Have a good day {}!".format(name))
elif name in "Eniola,Priyanka,Kamala,Devi,Nalini":
    print("Only the most beautiful ones bear this name!")
    print("Have a good day {}!".format(name))
else:
    print("Just a random name")
    print("Have a good day {}!".format(name))