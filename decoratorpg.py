<<<<<<< HEAD




def my_decorator(func):
    def wrap_func():
        print("**************")
        func()
        print("**************")
    return wrap_func

@my_decorator
    

def hello():
    print("hello world")

=======




def my_decorator(func):
    def wrap_func():
        print("**************")
        func()
        print("**************")
    return wrap_func

@my_decorator
    

def hello():
    print("hello world")

>>>>>>> master
hello()