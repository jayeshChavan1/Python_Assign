# def print_text():
#     print('this is text')
# print_text()


# def max_min(x):
#     return min(x),max(x)
# a=[1,2,3,4,5]
# n= max_min(a)
# print(n)

# def person(name,id=10): #default arg
#     print(name)
#     print(id)
# person("rob")

# def sum(a,*b):   # multiple arg
#     c=a
#     for i in b:
#         c=c+i
#     print(c)
# sum(1,2,3,4,5)

# def sum(*b):
#     c=0
#     for i in b:
#         c=c+i
#     print(c)
# sum(1,2,3,4,5)
#
# def person(name,**data):
#     print(name)
#     for i in data:
#         print(i)
# person("rob",id=10,city="Delhi")

# def fun(a,*b,**c):
#     print(a)
#     print(b)
#     print(c)
# fun(1,2,3,"hello",name="rob",id=10)

# def fruit(x):
#     for i in x:
#         print(i)
# a=["mango","berry","apple"]
# fruit(a)

# def sqr(x):
#     return x**2
# print(sqr(5))
# print(sqr(7))
# print(sqr(8))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# def printme(str):
#    print("This prints a passed string into this function")
#    print(str)
#    return;
#
# printme()

# def person(name,id=10):
#     print(name)
#     print(id)
# person(id=1,name='rob')
# person(name='bob')


#
# def sum(*a):
#     c=0
#     for i in a:
#        c=i+c
#     return c
# b=sum(1,2,3,4,5,5)
# print(b)

# def pers(**a):
#     for k,v in a.items():
#         print(k,v)
# pers(name="rob",age=20,no=2)

# def pos(arg1,arg2,arg3=30,arg4=40):
#     print(arg1,arg2,arg3,arg4)
# pos(arg1=4,arg1=3,arg2=23,arg4=34)
#
# def pos(arg1,arg2,arg3=30,arg4=40):
#     print(arg1,arg2,arg3,arg4)
# pos(4,3,23,arg4=34)

#
# def iseven(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l=[1,2,3,4,5,6,7,8,9,10]
# l1=list(filter(iseven,l))
# print(l1)

# def f1():
#     print("ADD")
#     def sum(a,b):
#         print("sum",a+b)
#     sum(4,5)
#     sum(5,6)
#     sum(2,3)
#     print("End inner")
# f1()
# print("end outer")



# def smdiv(func):
#     def inner(a,b):
#         if b==0:
#             print("It will give error because in denominator is zero")
#         else:
#             return func(a,b)
#     return inner
#
# @smdiv
#
# def div(a,b):
#     return a/b
#
# print(div(10,2))
# print(div(10,0))

# a = list(filter(lambda x:x*2,range(10)))
# print(a)
#
# a = list(map(lambda x:x*2,range(10)))
# print(a)
#
# a = list(filter(lambda x:x%2==0,range(10)))
# print(a)
#
# a = list(map(lambda x:x%2==0,range(10)))
# print(a)

