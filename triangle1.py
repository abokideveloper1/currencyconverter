print("-="*20)
print("Triangles analyzer")
print("-="*20)
l1 = float(input("Enter first line of triangle: "))
l2 = float(input("Enter second line of triangle: "))
l3 = float(input("Enter third line of triangle: "))

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print("Those lines above can build a triangle")
else:
    print("Those lines above can't build a triangle")