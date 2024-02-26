d={}
for i in range(n):
    k=input("Enter roll number:")
    v={}
    for j in range(m):
        sub=input("Enter Subject:")
        marks=int(input("Enter marks:"))
        v[sub]=marks
        d[k]=v
for i in d:
    l=list(d[i].values())
 print(f"(i) :)
