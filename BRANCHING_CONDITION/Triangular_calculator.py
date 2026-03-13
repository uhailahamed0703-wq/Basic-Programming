side_1=float(input("Enter the length of the first side of the triangle: "))
side_2=float(input("Enter the length of the second side of the triangle: "))
side_3=float(input("Enter the length of the third side of the triangle: "))

if side_1==side_2==side_3:
    print("The triangle is equilateral.")
elif side_1==side_2 or side_1==side_3 or side_2==side_3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")