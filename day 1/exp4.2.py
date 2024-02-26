x,y=map(int,input().split(" "))
if x>y:
 print("in sufficiant amount")
else :
 if x<y and x%5==0:
  print("Transaction is successful")
 else:
  print("Incorrect with draw amount(not multiple of 5)")
