sample_dict = {
    'colors': ['orange', 'red', 'blue'],
    'numbers': [1234, 456, 789, 10],
    'tools': ['Ansible', 'Terraform', 'Prometheus', 'Docker', 'Kubernetes'],  # this is a nested dictionary
    (1234, 456, 789): 'a',
}

print(sample_dict['colors'][1]) # prints within colors index 1 element.

print(sorted(sample_dict['colors'])) #sorts the order of colors.

sample_dict['numbers'][-1] = 100
print(sample_dict['numbers']) # replaces the last element in the numbers with 100

sample_dict ['fruits'] = ['apple', 'mango', 'banana']    # this adds the fruits key to the old sample_dict make it as one dict.

print(sample_dict)

print(sample_dict.keys()) # prints only keys as list

print(sample_dict.values()) #prints only values as list

print(sample_dict.items()) # prints the key and values as list within list each element as tuple.

# output for items:

[
    ('colors', ['orange', 'red', 'blue']), 
    ('numbers', [1234, 456, 789, 10]), 
    ('tools', ['Ansible', 'Terraform', 'Prometheus', 'Docker', 'Kubernetes']), 
    ((1234, 456, 789), 'a')
]