length = float(input("Enter the length of the wall in meters: "))
width = float(input("Enter the width of the wall in meters: "))
height = float(input("Enter the height of the wall in meters: "))
paint_coverage = 10  # square meters per can

area = 2*(length*height + width*height)
cans_needed = area / paint_coverage
print("The area of the wall is:", area, "square meters")
print("You will need", cans_needed, "cans of paint to cover the wall.")