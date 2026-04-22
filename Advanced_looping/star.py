for i in range(4):
    for j in range(5):
        if j==2:
            print("0",end=' ')
        else:
            print("X",end=' ')
    print()
print()
for i in range(4):
    for j in range(5):
        if j==2:
            print("0",end=' ')
        elif j==1 and i!=0 and i!=3:
            print("0",end=' ')
        elif j==3 and i!=0 and i!=3:
            print("0",end=' ')
        else:
              print("X",end=' ')
    print()