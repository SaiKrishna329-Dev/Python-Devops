# Function
A function is a block of reusable code that performs a specific task. Functions make code organized, reusable, and easier to debug.

## Syntax

```python
def greet():
    print("Hello, world!")
greet()    
```  
- `def` - keyword to mention the function
- `greet` - function name
- `()` - parameters list
- Indented block → function body

## Docstring:

- A docstring (short for documentation string) is a string literal that appears right after the definition of a function, class, or module. It is used to document what the function/class/module does.
- It must be the first statement inside a function or class — otherwise, Python won't treat it as a docstring.

```python
def function_name():
    """
    This is a docstring.
    It describes what the function does.
    """
    # function code
```
-  To access this docstring, you use: ` print(function_name.__doc__)
`

## Lambda function :

- A lambda function is a small, anonymous (unnamed) function defined using the lambda keyword instead of def.

**syntax:** `lambda arguments: expression`

- lambda — keyword to define the function.
- arguments — comma-separated input parameters.
- expression — a single line that gets evaluated and returned.




| Feature                | Keyword    | Example                         |
| ---------------------- | ---------- | ------------------------------- |
| Define function        | `def`      | `def func():`                   |
| Call function          | N/A        | `func()`                        |
| Parameters             | ()         | `def greet(name):`              |
| Return value           | `return`   | `return a + b`                  |
| Default args           | `=`        | `def func(x=5):`                |
| Variable args          | `*args`    | `def func(*a):`                 |
| Variable kwargs        | `**kwargs` | `def func(**k):`                |
| Lambda function        | `lambda`   | `lambda x: x+1`                 |
| Nested functions       | N/A        | `def outer(): def inner(): ...` |
| Function documentation | `""" """`  | `"""docstring"""`               |
