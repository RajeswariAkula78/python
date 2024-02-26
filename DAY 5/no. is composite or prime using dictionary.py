#checking no.is prime or composite using dictionary
def isprime(a):
    for i in range(2,a):
        if a%i==0:
           return "Composite"
        else:
           return "Prime"
n=int(input())
d={}
for i in range(n):
    k=i+1
    v=isprime(i+1)
    d[k]=v
print(d)
    
