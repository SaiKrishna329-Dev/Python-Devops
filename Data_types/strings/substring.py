text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
else:
    print(substring, "not found in the text")




# The "in" keyword checks for a case-sensitive match - if substring provided as IS then it will not match with "is" in the text.
# It returns True if the substring is found, otherwise False.
# This method is case-sensitive, meaning "is" and "IS" would be treated differently
# It can be used to check for substrings in strings.
# It can also be used to check for elements in lists, tuples, and other iterable objects
# It is a simple and efficient way to check for the presence of a substring or element.
# It can be used with any iterable, not just strings.
# It is commonly used in conditional statements to perform actions based on the presence or absence of a substring or element.
# It is a built-in feature of Python and does not require any additional libraries
# It is often used in loops and list comprehensions to filter or process elements based on their presence in a collection.
# It works on strings, lists, tuples, etc.

