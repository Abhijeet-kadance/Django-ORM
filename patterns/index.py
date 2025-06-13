# Type Annotations/Hints

# Basic structure

# def funtion(args: type, args2: type, ...) -> return type 

# def greet(name:str, age:int) -> str:
#     return f"My name is {name} and I am {age} years old."

# data = greet("abhi",27)
# print(data)

# def greet(name: str, age: int) -> str:
#     return f"My name is {name} and I am {age} years old."

# data = greet(123, "twenty-seven")  # ❌ wrong types
# print(data)

########### Variable annotations

# name: str="Alice"
# age: int= 27

######## Complex Types

# Union means "either type A or type B".

# def double(x: float | int) -> float:
#     return x * 2

# print(double("10"))
#print(double(4))
# print(double(4.2210293712381273981238129387198237198273198237192387129783128e3719823789172387123871892371897127))


# def process_data(data:list[int]) -> dict[str, int | float]:
#     return {
#         "sum": sum(data),
#         "average": sum(data) / len(data) if data else 0.0
#     }

# print(process_data([1,2,3,4,5,6]))


# Custom class type Hinting

# class User:
#     def __init__(self,name):
#         self.name = name
        
# def get_username(user: User) -> str:
#     return user.name

# user = User("Abhi")
# print(get_username(user))


#####################################

# def squares(nums: list[int]) -> list[int]:
#     return [ x * x for x in nums]
    
# print(squares([1,2,3,4,5]))


