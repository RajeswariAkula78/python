#to print keys and values of dictionary using function
n=int(input("Enter no.of items:"))
d={}
for i in range(n):
      key=input("key:")
      value=input("values:")
      d[key]=value
for i in d:
      print(f"key:(i) value:{d[i]}")
for i in d.keys():
      print(i)
for i in d.values():
      print(i)
    
