class A:

    def m1(self):
        print("Parent")

class B(A):

    def m2(self):
        print("Child 1")

class C(A):

    def m3(self):
        print("Child 2")

class D(C):

    def m4(self):
        print("Chile 3")


x1=B()       #Single inheritance
x1.m1()
x1.m2()


x1=D()        #Multilevel inheritance
x1.m1()
x1.m4()


x2=B()         #Hierarchical inheritance
x2.m1()
x2.m2()

x1=C()
x1.m1()
x1.m3()


class E(B,C):      #Multiple inheritance
    pass

x1=E()
x1.m1()


