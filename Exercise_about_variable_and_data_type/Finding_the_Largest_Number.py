A=float(input("Enter the first number: "))
B=float(input("Enter the second number: "))
C=float(input("Enter the third number: "))
if A >= B and A >= C:
    print("The largest number is:", A)
elif B >= A and B >= C:
    print("The largest number is:", B)
else:
    print("The largest number is:", C)