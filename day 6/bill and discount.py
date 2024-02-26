#discound and bill for male and female
n=int(input("Enter no.of items"))
d={}
for  i in range(n):
    k=input("Enter items:")
    v=int(input("Enter item price:"))
    d[k]=v
l=[]
for i in d:
     l.append(d[i]-d[i]*(3*n)/100)
g=input("Enter gender")
if g=="male":
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print("items - price : discount-price")
for i in d:
    print(f"{i} - {d[i]} : {l[j]}")
    j+=1
else:
     print("*"*20)
print(f"Total bill : {bill}")
