## Lambda function:

# Add two numbers
add = lambda a, b: a + b
print(add(1, 2))

# check even or odd
is_even = lambda x: x % 2 == 0
print(is_even(4))

# Sort a List of Tuples by Second Element

sample_pairs = [(1,4), (3,2), (3,5)]
sort_pairs = sorted(sample_pairs, key= lambda x: x[1] )
print(sort_pairs)

# map() — Apply a function to each element in a list

sample_list = range(1, 11) # 1...10
square = lambda num: num ** 2

ans = map(square, sample_list)
print(ans)

for ele in ans:
    print(ele)

# filter() — Filter elements using a condition

sample_list = range(1, 11) # 1...10
even = lambda x: x % 2 == 0
ans = filter(even, sample_list)
ans = list(filter(even, sample_list))
ans = list(map(even, sample_list))
print(ans)

for ele in ans:
    print(ele)

# reduce() — Reduce to a single value (requires functools)

from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, nums)
print(product)

# # List 

sample_list = range(1, 11) # 1...10
for ele in sample_list:
    if ele % 2 == 0:
        print(ele)