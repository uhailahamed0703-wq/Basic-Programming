hours=float(input("Enter the number of hours: "))

first_2_hours_fee=5000
additional_hour_fee=3000
if hours <= 2:
    total_fee=first_2_hours_fee
else:
    additional_hours=hours-2
    total_fee=first_2_hours_fee+(additional_hours*additional_hour_fee)
print("The total parking fee is:", total_fee)