import math
angle = float(input("Enter angle: "))
sine = math.sin(math.radians(angle))
tangent = math.tan(math.radians(angle))
cosine = math.cos(math.radians(angle))
print("SINE FOR {} EQUALS {:.2f} \n TANGENT FOR {} EQUALS {:.2f} \n COSINE FOR {} EQUALS {:.2f}".format(angle,sine,angle,tangent,angle,cosine))