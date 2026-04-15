list=[9,100,101,88,3,7]

largest=list[0]
second=list[0]
for i in list:
    if i>largest:
        largest=i
for i in list:
    if i>second and i<largest:
        second=i

print("second largest number is : ",second)
