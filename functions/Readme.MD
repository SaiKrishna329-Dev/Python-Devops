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
