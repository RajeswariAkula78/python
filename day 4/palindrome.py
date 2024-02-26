#palindrome
def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return 1
    else:
        return 0
n,m=int(input()),int(input())
