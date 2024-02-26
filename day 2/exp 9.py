def armstrong(n,m):
    for i in range(n,m+1):
        sum=0
        x=i
while n>=0:
    temp=i%10
    sum=temp*10
    i//=10
if sum==x:
     print(x)
n,m=int(input()),int(input())
armstrong(n,m)













     
