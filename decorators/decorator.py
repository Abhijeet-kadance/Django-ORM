# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function { func.__name__!r} took: {end_time-start_time:.4f} sec")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     return f"The sum is {sum(range(n))}"


# print(example_function(1000000))


# def test(func):
#     def wrapper():
#         print("Before Function calling")
#         func()
#         print("After Function calling")
#     return wrapper()

# def calling():
#     print("I am a callng function ....")
    
# calling = test(calling)
# calling


# def test(func):
#     def wrapper(*args,**kwargs):
#         print("Before Calling Wrapper")
#         func(*args,**kwargs)
#         print("After Calling wrapper")
#     return wrapper
    
# @test
# def calling(name):
#     print("Calling : ", name)

# calling("Abhi")


# def test(func):
#     def wrapper(*args,**kwargs):
#         print("Before Calling Wrapper")
#         func(*args,**kwargs)
#         print("After Calling wrapper")
#     return wrapper
    
# @test
# def calling(name):
#     print("Calling : ", name)

# calling("Abhi")



##################################### CLASS BASED DECORATOR ####################################


# class Testing:
#     def __init__(self,func):
#         self.func = func
    
#     def wrapper(self,*args,**kwargs):
#         print("Before calling class method")
#         test = self.func(*args,**kwargs)
#         print("After calling class method")
#         return test

#     def __call__(self,*args,**kwargs):
#         return self.wrapper(*args,**kwargs)
    

# @Testing
# def calling():
#     print("I am calling function ......")
#     return "Done"

# print(calling())



class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CallCounter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
# print(greet.count)
