w = float(input("Enter your weight: "))
h = float(input("Enter your height: "))
imc = w / (h ** 2)

if imc >= 16 and imc <= 16.9:
    print("VERY UNDERWEGHT!")
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 17 and imc <= 18.4:
    print("UNDERWEIGHT")
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print("Normal weight".upper())
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 25 and imc <= 29.9:
    print("Overweight".upper())
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 30 and imc <= 34.9:
    print("Obesity - level 1!".upper())
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
elif imc >= 35 and imc <= 40:
    print("Obesity - level 2!".upper())
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))
else:
    print("Obesity - level 3!".upper())
    print("Height: {:.2f}".format(h))
    print("Weight: {:.2f}".format(w))
    print("IMC: {:.2f}".format(imc))