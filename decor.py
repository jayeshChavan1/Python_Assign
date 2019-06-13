#decor
# def dec(fun):
#     def inner(word):
#         if word == "rob":
#             print("good")
#         else:
#             fun(word)
#     return inner
#
# @dec
# def wish(word):
#     print("heyy",word)
# wish("bob")
# wish("rob")
# wish("alex")

# def div(a,b):
#     print(a/b)
#
# def smartdiv(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner
#
# div = smartdiv(div)
# div(2,4)

