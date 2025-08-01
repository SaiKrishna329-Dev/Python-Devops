# Slicing and Indexing :

sample_str = 'a'
sample_str = "devops is my dream job" # with this we can have '' with in the "" string.
sample_str = """python for devops"""
# devops needs basics of python""" 

print(len(sample_str)) # length of string

print(sample_str.upper()) # entire string will become in capital letters

print(sample_str.capitalize()) # first character will become the capital letter

print(sample_str.count("python")) # counts how many times the substring "python" appears in sample_str, and prints that number.

ans = sample_str.split(" ") #splits the string into list
ans = sample_str.split("\n") # This line splits the string sample_str into a list of lines, using the newline character (\n) as the separator.
ans = sample_str.splitlines() # Smart method to split on all types of line breaks: \n, \r\n, and \r. 
#(Use splitlines() if you're processing multi-line text from files or user input, since it handles all types of line endings safely.)
# can retain line endings with splitlines(True).
print(ans)

# Indexing:

print(sample_str[1])
print(sample_str[-1])  # This line prints the last character, -2 = second last char, -3 = third last char


#Slicing :  Syntax = sequence[start:stop:step]


print(sample_str[:])    # this will print the entire string

print(sample_str[1:4]) # gives result of 1,2,3 index

print(sample_str[0:-1]) # prints all string except the last char bcz -1(index) is exclusive.

print(sample_str[-1:-4]) # You're trying to slice forward from -1 to -4 — but -1 is after -4, so Python finds no characters in that direction.

#That means: The slice is invalid in the forward direction, so the result is an empty string.

print(sample_str[-4:-1])

print(sample_str[::]) #this will print the entire string

print(sample_str[::2]) # this will print the char of index of start, start+2, start + 4..., etc

print(sample_str[-1::2]) # -1 refers to the last character, which is at the end of the string.

 #With a positive step, slicing moves right, but there’s no character after the last one, so it returns only the last character.

print(sample_str[::-1]) # to reverse the string

"""  Breakdown of sample_str[0:-1]:
sample_str → a string variable (e.g., "hello").

[start:end] → slice syntax, where:

start = 0 → the slicing starts from index 0 (the first character).

end = -1 → ends one character before the last, because negative indexing counts from the end (-1 is the last character).

👉 So sample_str[0:-1] returns all characters except the last one. """


sample_str = 'abc'
sample_str *= 10
print(sample_str)

sample_str = "Microsoft Windows [Version 10.0.22621.2861]"
sample_str = "{1}{0}".format(sample_str, "abc")
print(sample_str)

