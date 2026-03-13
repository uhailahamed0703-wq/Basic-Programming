salary=float(input("Enter the salary: "))
credit_score=int(input("Enter the credit score: "))
employment_status=float(input("Enter the employment status (employed/unemployed): "))
if salary>3000 and credit_score>650 and employment_status>2:
    print("Your loan application is approved.")
elif salary>3000 and credit_score>650 or employment_status>2 and salary>3000 or credit_score>650 and employment_status>2:
    print("The loan receives conditional approval")
else:
    print("your loan application is rejected")