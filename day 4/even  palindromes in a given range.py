#even palindromes in a range and list of palindromes
def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return 1
    else:
        return 0
n,m=int(input()),int(input())
l1,l2=[],[]
for i in range(n,m+1):
    flag=palindrome(i)
    if flag==1:
       l1.append(i)
    if i%2==0:
        if flag==1:
            l2.append(i)         
print(i)                   
print(str(l2))
