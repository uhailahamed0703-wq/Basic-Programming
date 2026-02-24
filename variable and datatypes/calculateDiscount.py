price=float(input("Enter the item price"))
if price>=100000:
    print("You recieved 10 percentage Discount")
    Total_Payment=price*0.1
    print("Total payment is: ",Total_Payment)

else:
    print("No Discount")
    print("Total payment is: ",price)
