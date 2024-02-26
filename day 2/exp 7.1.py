n=int(input())
sum=0
for i in range(1,n,2):
 if n>0:
    digit=n%10
    sum=sum*10+digit
    n//=10
print(sum)
