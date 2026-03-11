amount=float(input("Enter the total purchase amount: "))

if amount>=500000:
    print("You get 20% discount")
    discount=amount*0.20
    print("Your discount amount is:",discount)
    print("Your final amount is:",amount-discount)
elif amount>=250000:
    print("You get 10% discount")
    discount=amount*0.10
    print("Your discount amount is:",discount)
    print("Your final amount is:",amount-discount)
else:
    print("No discount available")
    print("Your final amount is:",amount)


