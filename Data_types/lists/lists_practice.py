sample_list = [1,2,3,4,5,6,7]
sample_list.append(8) # add the 8 to above list as continuation.
print(sample_list)

sample_list.append([8,9])
print(sample_list)

sample_list.extend([11,12,13])
print(sample_list)

sample_list.pop(2) # removes the mentined index element from the list and prints the rest of the list.
print(sample_list)

ele = sample_list.pop(2) # removes the mentined index element from the list and prints that element from list.
print(ele)

sample_list.reverse()
print(sample_list)

sample_list = ['b','d','w','a','g','f']
sample_list.sort()
print(sample_list)

sample_list_sorted = sorted(sample_list)
print(sample_list_sorted)


# Nesting Lists
sample_list = [1, 2, 3, 4, [60, 70, 80], 6, 7, 8]
print(sample_list[4][0]) # prints the 4 index first element -60


list1 = [1, 2, 3]
list2 = [10, 20, 30]
sample_list = [list1, list2]
print(sample_list)

sample_list = [[1, 2, 3], [10, 20, 30]]

a, b, c = [1, 2, 3] # Unpacking
print(a, b, c)

#Swapping values
a = 1
b = 2
a, b = b, a
print(a, b)
a = 2
b = 1

sample_list = [1, 2, 3, 4, [60, 70, 80], 6, 7, 8]
sample_list[-2] = 700 # replacing the 7 with 700 in the list
sample_list = sample_list[::-1]
print(sample_list)

sample_list = [1,2,3]
sample_list += [4,5,6]
print(sample_list)

sample_list = [1,2,3]
sample_list *= 4
print(sample_list)
