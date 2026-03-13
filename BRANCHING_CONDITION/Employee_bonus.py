salary=float(input("Enter your salary: "))
years_of_service=int(input("Enter your years of service: "))
if years_of_service > 10:
    bonus=salary*0.25
    print("Your bonus is: $", bonus)
elif years_of_service > 5 and years_of_service < 9:
    bonus=salary*0.15
    print("Your bonus is: $", bonus)
elif years_of_service > 1 and years_of_service < 4:
    bonus=salary*0.05
    print("Your bonus is: $", bonus)
else:
    print("No bonus")

print("your total salary is: $", salary+bonus)