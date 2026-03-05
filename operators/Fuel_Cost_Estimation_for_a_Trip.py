distance = float(input("Enter the distance of the trip in kilometers: "))
fuel_efficiency = 40 
fuel_price = 13000
fuel_needed = distance / fuel_efficiency
total_fuel_cost = fuel_needed * fuel_price
print("The estimated fuel cost for the trip is:", total_fuel_cost)