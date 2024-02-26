n=int(input())
i=2
while i < (n**0.5)+1:
 if n%i==0:
    print("Not a Prime")
    break
 i+=1
else:
    print("prime")

    
