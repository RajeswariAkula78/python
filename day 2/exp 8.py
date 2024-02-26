n=int(input())
temp=0
arm=0
while n > 0:
     digit=n%10
     arm=arm+digit*digit*digit
     n//10
if temp==arm:
 print("armstrong number")
else:          
 print("not an armstrong number")
