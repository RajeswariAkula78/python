a,b,c,d=map(int,input().split(" "))
fa=a-a*c/100
fb=b-b*d/100
if fa==fb :
 print ("any one you can buy")
else :
 if fa<fb :
  print("buy first one")
 else :
  print("buy second one")
