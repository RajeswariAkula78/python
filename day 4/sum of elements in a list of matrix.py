#matrix formation and sum of matrix elements
r,c=int(input("rows:")),int(input("columns:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
summ=0
for i in l:
    print(i)
    summ+=sum(i)
print(summ)
