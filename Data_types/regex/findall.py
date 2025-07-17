 #The name findall usually refers to a function from Python's re (regular expressions) module: re.findall. This function searches a string for all non-overlapping matches of a pattern and returns them as a list.

# syntax :
#  re.findall(pattern, string, flags=0)


# Example usage of re.findall to find all words in a string:
import re

text = "Python is awesome. Python is easy to learn."
matches = re.findall(r'\b\w+\b', text)
print(matches)


# Example usage of re.findall to find all email addresses in a string:

import re
text = "Contact me at abc@example.com or test123@mail.org"
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print(emails)

# Example usage of re.findall to extract names from a string:

import re
text = "Name: Alice, Age: 25; Name: Bob, Age: 30"
names = re.findall(r'Name: (\w+)', text)
print(names)



