#searching element form phone book
n=int(input("Enter no. of items"))
d={}
for i in range(n):
    name=input("name:")
    value=int(input("values:"))
    d[name]=value
for i in d:
    print(f"name:(i) value:{d[i]}")
if i in d:
    print("Found")
if i not in d:
    print("Not found")
print(name,value)           
