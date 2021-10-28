l1 = int(input("Enter value for first line: "))
l2 = int(input("Enter value for second line: "))
l3 = int(input("Enter value for third lime: "))
if l1 < l2 + l3 and l2 < l1 +l3 and l3 < l1 + l2:
    print("\033[1;30;42mThese lines can build a triangle\033[m".upper())
    if l1 == l2 == l3:
        print("These lines can build an equilateral triangle".upper())
    elif l1 != l2 != l3 != l1:
            print("These lines can build a scalene triangle".upper())
    else:
        print("These lines can build an isosceles triangle".upper())


else:
    print("\033[1;30;41mThese lines can't build a triangle\033[m".upper())
