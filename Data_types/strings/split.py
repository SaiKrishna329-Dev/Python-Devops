arn = "arn:aws:iam::123456789012:user/devops-engineer arn:aws:iam::123456789012:user/john.doe"
arn_list = arn.split(" ")
print("arn_list:", arn_list)
user_names = [a.split("/")[-1] for a in arn_list]
print("user_names:", user_names)



# In Python:

# list[0] → first element

# list[1] → second element

# ...

# list[-1] → last element

# list[-2] → second-last, and so on