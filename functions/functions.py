def sum_of_values():
    num1 = 10
    num2 = 20
    ans = num1 + num2
    return ans
result = sum_of_values()    
print(result)

def sum_of_values(*args, **kwargs): # args and keyward args
    print(args, kwargs)
    return sum(args), sum(kwargs.values())

ans = sum_of_values(10, 20, 30, 40, 50, 60, 70, num1=10, num2=20)
print(ans)

ans = sum_of_values(10, 20, 30, 40, num1=10)
print(ans)

ans = sum_of_values(10, 20)
print(ans)

def square(num):
    return num ** 2
ans = square(10)
print(ans)

sample_list = range(1, 11) # 1...10
square = lambda num: num ** 2

ans = map(square, sample_list)
print(ans)

for ele in ans:
    print(ele)

sample_list = range(1, 11) # 1...10
even = lambda x: x % 2 == 0
ans = filter(even, sample_list)
ans = list(filter(even, sample_list))
ans = list(map(even, sample_list))
print(ans)

for ele in ans:
    print(ele)

# List comprehension
sample_list = range(1, 11) # 1...10
for ele in sample_list:
    if ele % 2 == 0:
        print(ele)