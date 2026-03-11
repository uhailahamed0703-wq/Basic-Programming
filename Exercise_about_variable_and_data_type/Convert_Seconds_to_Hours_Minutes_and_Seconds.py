total_seconds=float(input("Enter the total number of seconds: "))
hours=total_seconds//3600
remaining_seconds=total_seconds%3600

minutes=remaining_seconds//60
seconds=remaining_seconds%60
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)  