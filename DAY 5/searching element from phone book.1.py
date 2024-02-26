#searching element form phone book
n=int(input("Enter no.of items"))
d={}
for i in range(n):
    name,value=map(str,input().split())
    d[name]=value
m=int(input("No of search items:"))
for i in range(m):
    s=input()
    if s in d:
        print(s,d[s])
        
    else:
        print("Not Found")
