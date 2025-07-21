total = 10 
# add_assign = total += 3 doesn't work in Python, bcz we are doing 2 assignments at once
total += 3  # 10+3 = 13
total -= 2  # 13-2 = 11
total *= 4  # 11*4 = 44
total /= 2  # 44/2 = 22.0
total %= 3  # 22.0%3 = 1.0 , final value of total is 1.0.So in print statements below, we will assign total to 1 for all operations.

add_assign = total
subtract_assign = total
multiply_assign = total
divide_assign = total
modulus_assign = total


print("add_assign: ", add_assign)
print("subtract_assign: ", subtract_assign)
print("multiply_assign: ", multiply_assign)
print("divide_assign: ", divide_assign)
print("modulus_assign: ", modulus_assign)

