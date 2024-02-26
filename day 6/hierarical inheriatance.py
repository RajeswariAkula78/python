class A:
    def hi(self):
        print("hello1")
class B(A):
    def __init__(self):
        print("hello2")
class C(B):
    def __init__(self):
        print("hello3")
b=B()
b.hi()
c=C()
c.hi()
