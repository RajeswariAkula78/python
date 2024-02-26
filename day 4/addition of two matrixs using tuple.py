#addition of two matxics using tuple
r,c=int(input()),int(input())
l1,l2,l3=[],[],[]
for i in range(r):
    l1.append(tuple(map(int,input().split())))
    for i in range(r):
    l2.append(tuple(map(int,input().split())))
