for i in range(5):
    for j in range(5):
        if i==2 or j==2:
            print("*",end=" ")
        else:
            print("_",end=" ")
    print()

print()

for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end=" ")
        else:
            print("_",end=" ")
    print()