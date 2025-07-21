import os

print(os.getenv("pass"))


# Example usage of os.getenv to retrieve an environment variable:
# os.getenv() is used to get the value of an environment variable.
# you can access environment variables using the built-in "os module".

import os

my_var = os.getenv("MY_VAR")  # Returns None if not set
print(my_var)
