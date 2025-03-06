##Generator
#it is normal function

# def first():
#     return 1  ## it return value
# n=first()
# print(n)

# def first():
#     yield 1  ## it return object
#     yield 2
#     yield 3
#     yield 4 
# n=first()
# print(n)
# print(list(n))

# def first():
#     yield 1
#     yield 2
#     yield 3
#     yield 4 
# n=first()
# print(n)
# print(next(n))
# print("hi")
# print("hello")
# print("welcome")
# print(next(n))


def natural_no(x):
    i=1
    while i<=x:
        yield i
        i=i+1
n= int(input("Enter any value"))
p=natural_no(n)
#print(p)
#print(list(p))
print(next(p))
print("x")
print(next(p))
print("y")
for i in p:
    print(i)