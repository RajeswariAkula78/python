#factorial of number using cls and method and constructor
class day6:
    def __init__(self,data):
        self.data=data
        self.fact=fact
    def fact(self,n):
        f=1 
        for i in range(1,n+1):
            f*=i
        print(f)
obj=day6()
obj.fact(int(input()))
