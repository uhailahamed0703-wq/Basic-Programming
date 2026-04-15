n=int(input("How many numbers in list?: "))
numbers=[]

for i in range(n):
    num=int(input("Enter the number : "))
    numbers.append(num)

total=0
for num in numbers:
    total=total+num
print("The sum of list is : ",total)