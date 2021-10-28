from math import sqrt

w = float(input("Enter your weight: "))
h = float(input("Enter your height: "))
imc = sqrt(h) / w

if imc >= 16 or imc <= 16.9:
    print("VERY UNDERWEGHT!")
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 17 or imc <= 18.4:
    print("UNDERWEIGHT")
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 18.5 or imc <= 24.9:
    print("Normal weight".upper())
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 25 or imc <= 29.9:
    print("Overweight".upper())
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 30 or imc <= 34.9:
    print("Obesity - level 1!".upper())
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 35 or imc <= 40:
    print("Obesity - level 2!".upper())
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
else:
    print("Obesity - level 3!".upper())
    print("Height: {:.2f".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))