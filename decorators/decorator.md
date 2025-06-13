## 📌 What is a decorator?

    A decorator is just a function that takes another function as input and returns a new function that usually adds some extra behavior before, after, or around the original function.

***Basic Form***

    def decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper

Now, if you apply it like this:

    @decorator
    def greet():
        print("Hello!")


It works fine because greet() takes no arguments, and the wrapper() inside the decorator also takes no arguments.


## ❌ What goes wrong?

Suppose your function takes arguments:

    @greet_decorator
    def greet(name):
        print(f"Hello, {name}!")

But your decorator is defined like this:

    def greet_decorator(func):
        def wrapper():  # ← This doesn't accept 'name'
            func()
        return wrapper

When you call greet("Alice"), Python is essentially doing this:

    wrapper("Alice")

But wrapper doesn't accept any arguments, so it throws:

    TypeError: wrapper() takes 0 positional arguments but 1 was given