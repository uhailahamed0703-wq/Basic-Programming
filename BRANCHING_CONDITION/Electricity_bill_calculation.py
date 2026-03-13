usage=float(input("Enter the electricity usage in kWh: "))
if usage>300:
    print("The electricity bill is: $", usage*0.20)
elif usage<=100:
    print("The electricity bill is: $", usage*0.10)
elif usage>100 and usage<=300:
    print("The electricity bill is: $", usage*0.15)