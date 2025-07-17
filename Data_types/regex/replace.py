
# re.sub() is used to search a string for a regex pattern and replace all occurrences with a new string.

# Syntax:
# re.sub(pattern, replacement, string, count=0, flags=0)
# pattern: The regex pattern to search for.

# replacement: The string to replace matches with.

# string: The original string.

# count: (Optional) Number of replacements (default is 0 = replace all).

# flags: (Optional) Regex flags like re.IGNORECASE.


# Example usage of re.sub to replace digits with a hash symbol:

import re

text = "My number is 98765 and pin is 560001"
result = re.sub(r'\d', '#', text)
print(result)



# Example usage of re.sub to remove special characters from a string:
import re
text = "Hello@# World!!"
result = re.sub(r'[^\w\s]', '', text)
print(result)


# Example usage of re.sub to format dates from YYYY-MM-DD to DD/MM/YYYY:
import re

text = "Today is 2025-07-17"
result = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\1/\2', text)
print(result)


# | Pattern                   | Replaces                                    |
# | ------------------------- | ------------------------------------------- |
# | `\d`                      | Digits                                      |
# | `\s+`                     | Multiple spaces                             |
# | `[^\w\s]`                 | Special characters (keeps words and spaces) |
# | `(\d{4})-(\d{2})-(\d{2})` | Rearranging date formats                    |

