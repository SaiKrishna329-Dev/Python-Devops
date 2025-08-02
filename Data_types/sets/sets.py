sample_set = set()  # Empty set
sample_set.add(10)
sample_set.add(13)
sample_set.add(100)
sample_set.add(100)
sample_set.add(12)
print(sample_set) # --> {10,12,100,13} - order is maintained and duplicates not allowed
print(sample_set[0])  # sets won't support indexing due to order won't be maintained.

# Create a list with repeats
list1 = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1] 
test = set(list1)
print(test)  # {1,2,3,4,5,6} - order is maintained and duplicates not allowed 