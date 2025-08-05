# functions with parameters: You can pass values into functions using parameters

def greet(name):
    print("hello", name)

greet("sai")  

# # functions with retun values: Functions can return results using the return keyword

def sum_of_values():
    num1 = 10
    num2 = 20
    ans = num1 + num2
    return ans
result = sum_of_values()    
print(result)

def sum_of_values(a, b):
    return a + b
result = sum_of_values(10, 20)  
print(result)  

#Function with *args and **kwargs : 

def sum_of_values(*args, **kwargs): # args and keyward args
    print(args, kwargs)
    return sum(args), sum(kwargs.values())

ans = sum_of_values(10, 20, 30, 40, 50, 60, 70, num1=10, num2=20)
print(ans)

ans = sum_of_values(10, 20, 30, 40, num1=10)
print(ans)

ans = sum_of_values(10, 20)
print(ans)

# # function with keyword arguments

def intro(name, age):
    print(f"{name} is {age} years old.")

intro(age=25, name="Krishna") # order is not mandotary here

#functions with default args: You can set default values for parameters

def greet(name="Guest"):
    print("Hello,", name)

greet()         # Output: Hello, Guest
greet("Sai")    # Output: Hello, Sai

# Return Multiple Values:

def mul_values(numbers):
    return min(numbers), max(numbers), sum(numbers) # min, max, sum are in-built functions in python.
min, max, sum = mul_values([10,30,40])
print(min, max, sum)

# # Nested function : 

def outer():
    def inner():
        print("nested function")
    inner()
outer()        

# # Docstrings (Function Documentation)

def greet(name):
    """This function greets the user."""
    print("Hello", name)

print(greet.__doc__)

# # Pass by Object Reference : 

def modify_list(lst):
    lst.append(100)

nums = [1, 2, 3]
modify_list(nums)
print(nums)  # Output: [1, 2, 3, 100]

# # Using Functions in Loops / Comprehensions:

def square(x):
    return x * x

squares = [square(x) for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

def square(num):
    return num ** 2
ans = square(10)
print(ans)