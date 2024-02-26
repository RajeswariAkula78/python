class A:
    def hi(self):
        print("hi")
    def hi(self,data):
        print("hello")
class B:
    def hi(self,data):
        print("HI")
a=A()
b=B()
a.hi(4)
b.hi(5)
