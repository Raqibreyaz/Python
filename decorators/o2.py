# def debug(func):     
#     return lambda *args,**kwargs:func(*args,**kwargs)

# @debug    
# def greet(name,greeting="Hello"):
#     print(f"{greeting} {name}")
    
# greet(greeting="Hi",name="chacha")

def debug(func):
    def wrapper(*args,**kwargs):
        args_value =", ".join(str(arg) for arg in args)
        kwargs_value =", ".join(str(arg) for arg in kwargs.items())
        print(f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper

@debug
def hello():print("hello")

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting} {name}")
    
hello()
greet("raquib",greeting="Hi")