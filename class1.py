
# class comp:
#
#
#     def config(self):
#         print("hello")
#
# com1 = comp()
# com2 = comp()
#
# comp.config(com1)
# comp.config(com2 )



# class prt:
#     '''doc strng'''
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
#     def prnt(self):
#     #     print(self.name)
#     #     print(self.age)
#
# print(prt.__doc__)
#
# a = prt("rob",29)  #object create
# b = prt("bob",30)
# a.prnt() #method calling
# b.prnt()


#
# class employee:
#     def __init__(self,eno,ename):
#         self.eno=eno
#         self.ename=ename
#
#     def display(self):
#         print("name",self.ename)
#         print("number",self.eno)
#
#
# e1=employee(11,"rob")
# #print(e1.ename,e1.eno)   #print in one line
# print(e1.__dict__)   #print in dict format




# Declare instance from outside class

# class Test:
#     def __init__(self):
#         self.a=100
#         self.b=200
#     def t2(self):
#         self.c=300
#         self.d=400
#
# t1=Test()
# t1.t2()
# t1.a=500
# t1.e=600
# t1.f=700
# t3=Test()
# print(t1.__dict__)
# print(t3.__dict__)


#delete remove instance variable from an object

# class Test:
#     def __init__(self):
#         self.a=1
#         self.b=2
#         self.c=3
#
# t1=Test()
# t2=Test()
# del t1.c          #remove instance variable from object
# print(t1.__dict__)
# print(t2.__dict__)


#static variable
# class Test:
#     a=10         # static variable / class level variable
#     def __init__(self):
#         self.b=20
#
# t1=Test()
# print(t1.a,t1.b)


# class Test:
#     a=10
#     def __init__(self):
#         self.b=20
#         Test.c=30
#
#     def mt(self):
#         self.d=40
#         Test.d=50
# t1=Test()
# t1.mt()
# print(Test.__dict__)
#



# class Country:
#
#     def m1(self):
#         print("India")
#
# class State(Country):
#
#     def m2(self):
#         print("MH")
#
# class City(State):
#
#     def m3(self):
#         print("Mumbai")
#
# person1 = City()
# person1.m1()
# person1.m2()
# person1.m3()

# # parent class
#
#
# class Bird:
#
#     def __init__(self):
#         print("Bird is ready")
#
#     def whoisThis(self):
#         print("Bird")
#
#     def swim(self):
#         print("Swim faster")
#
# # child class
# class Penguin(Bird):
#
#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")
#
#     def whoisThis(self):
#         print("Penguin")
#
#     def run(self):
#         print("Run faster")
#
# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()
#



class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

ob = B()
