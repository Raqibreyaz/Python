
def func1():
    return lambda x,y : x-y 

z = func1()

print(z(5,3))

n=10

print([n*x for x in range(1,11)])

for i in range(n,n*10+1,n):print(i)

print("raquibreyaz"[-2:-5])

def func2():
    x = 5
    return lambda : print(x)

childFunction = func2()

print(childFunction)
