name = str(input("What's your name?: "))
print("My name is {},nice to meet you!".format(name))
print("My name is {:20},nice to meet you!".format(name))
print("My name is {:<20},nice to meet you!".format(name))
print("My name is {:>20},nice to meet you!".format(name))
print("My name is {:^20},nice to meet you!".format(name))
print("My name is {:=^20},nice to meet you!".format(name))
print(" ")
print("******SYSTEM PRIMITIVE TECHNICAL INFO******")
print(" ")
print("ONLY SPACE: ",name.isspace())
print("NUMERIC: ",name.isnumeric())
print("ALPHABETIC: ",name.isalpha())
print("ALPHANUMERIC: ",name.isalnum())
print("UPPER CASE: ",name.isupper())
print("LOWER CASE: ",name.islower())