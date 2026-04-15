list=[1,1,2,2,4,4,5,6]

unique_list=[]

for i in list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)