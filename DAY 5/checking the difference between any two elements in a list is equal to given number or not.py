n,m=map(int,input().split())
list=list(map(int,input().split()))
flag=0
for i in list:
    for j in range(n):
        if l[i]-l[j]==m:
            flag=1
x=True if flag==1 else False
print(x)
