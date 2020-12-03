'''
Анонимные функции, lambda-выражения
'''
lfunc = lambda x, y, z = 1: x + y + z
print("lfunc(1,2,3): ",lfunc(1,2,3))
print("lfunc(1,2): ",lfunc(1,2))
print("lfunc(x=1,y=3): ",lfunc(x=1,y=3))
print("lambda result: ", \
(lambda a,b,sep=", ":
sep.join((a,b)))("Hello","World!"))
print("\n")

x = int(input())
lam = lambda x: x % 3
if lam(x) == 0:
    print(lam(x))