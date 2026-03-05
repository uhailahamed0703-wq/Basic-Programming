One_person_water_consumption = 2.5 # liters per day
family_size = 5
gallon_contains=19 #liters
gallon_price=19000

Total_weekly_water_requirement=7*(One_person_water_consumption*family_size)
Total_weekly_gallons_required=int(Total_weekly_water_requirement/gallon_contains)+1
Total_weekly_cost=Total_weekly_gallons_required*gallon_price

print("Total weekly water requirement for the family is:", Total_weekly_water_requirement, "liters")
print("Total weekly gallons required for the family is:", Total_weekly_gallons_required, "gallons")
print("Total weekly cost for the family's water consumption is:", Total_weekly_cost, "rupiah")