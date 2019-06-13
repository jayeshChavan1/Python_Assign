# Single inheritance

# class A:
#
#     def m1(self):
#         print("A")
#
#
# class B(A):
#
#     def m2(self):
#         print("B")
#
# x1=B()
# x1.m1()
# x1.m2()



#Multilevel

# class A:
#     fact = 10
#     def m1(self):
#         print("A")
#
#
# class B(A):
#
#     def m2(self):
#         print("B")
#
# class C(B):
#
#     def m3(self):
#         print("C")
#
# x1=C()
# x1.m1()
# x1.m2()
# x1.m3()
# print(x1.fact)


# #Hierarchical
#
# class A:
#
#     def m1(self):
#         print("Parent")
#
# class B(A):
#
#     def m2(self):
#         print("Child 1")
#
# class C(A):
#
#     def m3(self):
#         print("Child 2")
#
# x2=B()
# x2.m1()
# x2.m2()
#
# x1=C()
# x1.m1()
# x1.m3()
#



#Multiple

class A:

    def m1(self):
        print("A class")

class B:

    def m1(self):
        print("B class")

class D:

    def m1(self):
        print("D class")


class C(A,B,D):

    def m2(self):
        print(super(B,self).m1())

x1=C()
x1.m1()
