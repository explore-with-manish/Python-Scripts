# def fib(n):
#     a,b=0,1

#     result=[]
#     while a<n:
#         result.append(a)
#         a,b=b, a+b

#     return result

# for r in fib(15):
#     print(r)

# -------------------------------------------------

# def idGenerator():
#     yield 1
#     yield 2
#     yield 3

# print(idGenerator())

# x = idGenerator()

# print(next(x))
# print(next(x))
# print(next(x))

# for i in idGenerator():
#     print(i)

# ------------------------------------------------

def fib(n):
    a,b=0,1

    while a<n:
        yield a        
        a,b=b, a+b


for r in fib(15):
    print(r)
