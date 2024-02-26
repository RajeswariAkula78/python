n=int(input())
sum=0
for i in range(n):
 if n>0:
    digit=n%10
    sum=sum*10+digit
    n//=10
 else:
        break
print(sum)
