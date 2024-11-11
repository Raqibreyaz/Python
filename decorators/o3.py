from time import sleep

def cache(func):
    memory = {}
    def wrapper(*args):
        if(args in memory):
            print('memory',memory)
            print("returning cached value")
            return memory[args]
        else:
            print('calculating and caching value')
            result= func(*args)
            memory[args] = result
            return result
        
    return wrapper

@cache
def long_running_function(a,b):
    sleep(4)
    return a+b

print(long_running_function(5,3))
print(long_running_function(2,7))
print(long_running_function(5,3))
