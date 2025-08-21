 #The name findall usually refers to a function from Python's re (regular expressions) module: re.findall. 
 #This function searches a string for all non-overlapping matches of a pattern and returns them as a list.

# syntax :
#  re.findall(pattern, string, flags=0)


# Example usage of re.findall to find all words in a string:
import re

text = "Python is Awesome. Python is easy to learn."
matches = re.findall(r'\b\w+\b', text)
print(matches)

import re 
text = "Python is Awesome. Python is easy to learn."
matches = re.findall(r'\b[A-Z][a-zA-Z]*\b', text) # prints only words starting with capital letters
print(matches)

re.findall(r'\b[A-Z][a-zA-Z]*(?:\s+[A-Z][a-zA-Z]*)*\b', text) # prints two capital letter words as one word which are seperated by space.

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
words = re.findall(r'\b\w\b', text) # prints only one character word in string()
print(words)

result = re.findall(r'\b\w{2}\b', text) # prints only 2 letter word.
print(result)

re.findall(r'\b\w{3,}\b', text) # prints 3 or more character word
re.findall(r'\b\w{4,6}\b', text) # prints 4,5,6 character words in the string.

import re 
text = "Order IDs are 123, 456, and 7890."
nums = re.findall(r'\b\d+\b', text)
print(nums)

text = "Order IDs are 123.65, 456, and 78.90."
nums = re.findall(r'\d+\.\d+', text)
print(nums)

text = "Order IDs are 123.65, 456, and 78.90."
nums = re.findall(r'\d+(?:\.\d+)?', text) # prints both int and float
print(nums)

text = "Order IDs are 123.65, 456, and 78.90 -78 -33"
nums = re.findall(r'-?(\d+(?:\.\d+)?)', text) # prints all the values and removes the - sign
print(nums)

text = "Order IDs are 123.65, 456, and 78.90 -78 -33"
nums = re.findall(r'-?\d+(?:\.\d+)?', text) # prints all the values with - sign
print(nums)

text = "Meeting on 21-08-2025, another on 05-12-2024."
dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)
print(dates)

text = "Loving #Python #Regex #100DaysOfCode"
hashtags = re.findall(r'#\w+', text)
print(hashtags)

# Extract all HTML tags

text = "<html><body><h1>Hello</h1></body></html>"
html = re.findall(r'<(/?\w+)>', text)
print(html)
print(re.findall(r'<\/?(\w+)', text)) # prints without '/' sign

#Extract all prices

text = "Products cost $20, @1500, and €30.50."
prices = re.findall(r'[$@]\d+(?:\d\.\d+)?', text)
print(prices)

# Extracts IP's

text = "Valid IPs: 192.168.1.1, 10.0.0.5, 255.255.255.255"
ips = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', text)  
print(ips)

#Extract quoted strings

text = 'She said "hello", then he replied "hi".'
quoted = re.findall(r'"(.*?)"', text) # lazy and needy, fethes only as small as possible
print(quoted)
print(re.findall(r'"(.*)"', text)) # greedy, prints as max as possible.. from "hello to hi"