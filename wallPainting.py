n1 = float(input("Enter wall width: "))
n2 = float(input("Enter wall clearance: "))
area = n1 * n2
print("Wall area equals {} through {} of width and {} of clearance".format(area,n1,n2))
wallp = area / 2
print("You'll need {} litres to paint this wall".format(wallp))