vehicle_type=input("Enter the type of vehicle : ")
parking_duration=float(input("Enter the parking duration in hours: "))

if vehicle_type=="motorcycle":
    if parking_duration<=1:
        print("The parking fee is: $1")
    elif parking_duration>1:
        additional_hours=parking_duration-1
        additional_fee=additional_hours*0.5
        total_fee=1+additional_fee
        print("The parking fee is: $", total_fee)

elif vehicle_type=="car":
    if parking_duration<=1:
        print("The parking fee is: $2")
    elif parking_duration>1:
        additional_hours=parking_duration-1
        additional_fee=additional_hours*1
        total_fee=2+additional_fee
        print("The parking fee is: $", total_fee)

elif vehicle_type=="bus":
    if parking_duration<=1:
        print("The parking fee is: $3")
    elif parking_duration>1:
        additional_hours=parking_duration-1
        additional_fee=additional_hours*2
        total_fee=3+additional_fee
        print("The parking fee is: $", total_fee)