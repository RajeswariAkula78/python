#matrix formation and product of matrix elements
r,c=int(input("rows:")),int(input("columns:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
prod=1
for i in l:
    print(i)
    for j in i:
        prod*=j
    print(prod)
