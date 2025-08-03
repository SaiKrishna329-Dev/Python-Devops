#1 script to find sum of even and odd numbers in a given list

sample_list = [12, 20, 30, 33, 45, 7, 70]

even_num = []
sum_even = 0

odd_num = []
sum_odd = 0
for ele in sample_list:
    if ele % 2 == 0:
        even_num.append(ele)
        sum_even += ele
       
    else:
        odd_num.append(ele)   
        sum_odd += ele

print(sum_even, sum_odd) 

#2 To know the string to list conversions

sample_str = "python will be helpful for devops"
sample_str_list = list(sample_str)
print(sample_str_list)  # this will covert str to list

for char in sample_str:
    print(char) # this will do the iteration for each char in str and prints column wise.

sample_str_list = ['p', 'y', 't', 'h', 'o', 'n', ' ', 'w', 'i', 'l', 'l', ' ', 'b', 'e', ' ', 'h', 'e', 'l', 'p', 'f', 'u', 'l', ' ', 'f', 'o', 'r', ' ', 'd', 'e', 'v', 'o', 'p', 's']   
sample_str = ""

for char in sample_str_list:
    sample_str += char
    print(sample_str)
# sample_str = " ".join(sample_str_list)
# print(sample_str)

#3 loops with tuple

sample_tuple = ('a', 'b', 'c', 'd')
for c in sample_tuple:
    print(c)

sample_tuple_list = [('a', 1), ('b', 2), ('c', 3)]
for val1, val2 in sample_tuple_list:
    print(val1, val2)

#4 with dictionaries

dict = {'a': 1, 'b': 2, 'c': 3}
for k in dict.keys():
    print(k)
for v in dict.values():
    print(v) 
for k, v in dict.items():
    print(k, v)        

#5 search for the element in the given list

sample_list = [12, 20, 20, 30, 20, 33, 45, 7, 70]
ele_to_search = 20
idx = 0

for num in sample_list:
    if num == ele_to_search:
        print("element found at index", idx)
        # break
        continue
    idx += 1    
else:
    print("element not found")    

#6 Enumerate - to represent index with number

sample_list = [10, 10, 20, 30, 5, 80, 90]
for idx, ele in enumerate(sample_list):
    print(idx, ele)

#7 Range     

sample_list = [10, 10, 20, 30, 5, 80, 90]
for idx in range(len(sample_list)):
    print(sample_list[idx], idx)

#8 While Loop

sample_list = [10, 10, 20, 30, 5, 80, 90]
idx = 0

while (idx < len(sample_list)):
    print(sample_list[idx])
    idx += 1

#9 zip() -  is a built-in Python function that combines multiple iterables (like lists, tuples, etc.) into pairs (or tuples) element by element.
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e']

for ele1, ele2 in zip(list1, list2):
    print(ele1, ele2)

#10 

sample_list = [10, 2, 20, 30, 5, 80, 90]
element_to_search = 80

if element_to_search not in sample_list:
    print("Element not found")
else:
    print("Element found")






