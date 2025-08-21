 #The name findall usually refers to a function from Python's re (regular expressions) module: re.findall. 
 #This function searches a string for all non-overlapping matches of a pattern and returns them as a list.

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


import re 
text = "Python is awesome, isn't it?"
#words = re.findall(r'\b\w\b', text) # prints only one character word in string()
#print(words)

result = re.findall(r'\b\w{2}\b', text) # prints only 2 letter word.
print(result)

re.findall(r'\b\w{3,}\b', text) # prints 3 or more character word
re.findall(r'\b\w{4,6}\b', text) # prints 4,5,6 character words in the string.


