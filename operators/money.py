
amount = float(input("Enter the amount: "))


mod50 = amount % 50000
money50=(amount-mod50)//50000
amount=mod50


mod20 = amount % 20000
money20=(amount-mod20)//20000
amount=mod20


mod5 = amount % 5000
money5=(amount-mod5)//5000
amount=mod5


mod2 = amount % 2000
money2=(amount-mod2)//2000
amount=mod2

mod1 = amount % 1000
money1=(amount-mod1)//1000
amount=mod1

print("Number of 50000 notes:",money50)
print("Number of 20000 notes:",money20)
print("Number of 5000 notes:",money5)
print("Number of 2000 notes:",money2)
print("Number of 1000 notes:",money1)
