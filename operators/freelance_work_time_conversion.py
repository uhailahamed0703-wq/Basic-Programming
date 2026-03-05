hours=float(input("Enter the number of hours worked:"))
Minutes=float(input("Enter the number of minutes worked:"))

Minutes_to_hour=Minutes/60
Total_hours=hours+Minutes_to_hour
Salary=Total_hours*85000
print("salary is",Salary)