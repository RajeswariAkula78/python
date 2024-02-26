def encryption(s,k):
 s1=""
 for i in s:
    x=ord(i)+k
    s1+=chr(x)
 print(s1)
def decryption(s,k):
 s1=""
 for i in s:
    x=ord(i)-k
    s1+=chr(x)
 print(s1)
k=int(input("enter the key value:"))
s=input("enter the string value:")
op=input("select operation:")
if op=="encryption":
    encryption(s,k)
elif op=="decryption":
    decryption(s,k)
else:
    print("no operation")
