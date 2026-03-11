length=float(input("Enter the length:"))
width=float(input("Enter the width:"))

area= length*width
perimeter= 2*(length+width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

if area>100:
    print("large area")