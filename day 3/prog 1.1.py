s=input()
s1=""
for i in s:
 if i in "aeiou":
    if i==s[0]:
         print(i)
         if i==s[1]:
          print(i)
         if i==s[2]:
             print(i)
             if i==s[3]:
                 print(i)
                 if i==s[4]:
                    print(i)
 if s.count(i)%2!=0:
    s1+=i
print(min(s1))
