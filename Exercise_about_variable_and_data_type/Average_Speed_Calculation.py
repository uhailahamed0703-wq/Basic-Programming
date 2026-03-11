distance_traveled=float(input("Enter the distance traveled in kilometers: "))
travel_time=float(input("Enter the travel time in hours: "))

speed=distance_traveled/travel_time
print("The average speed is:", speed, "km/h")
if speed > 80:
    print("High speed")