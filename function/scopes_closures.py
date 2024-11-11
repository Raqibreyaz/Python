username = 'raqib'

def changeUsername():
    global username
    username = 'reyaz'
    print("changing username")
    
print(username)
changeUsername()
print(username)

def func1():
    x = 12;
    def func2():
        print('in func2',x)
    return func2

x = func1();
