# How do you parse large log files efficiently in Python?

with open('dev.log') as f:
    for line in f:
        if "ERROR" in line:
            print(line)

# How can Python be used to interact with AWS resources?

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

#cretae S3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-devops-bucket')


# How can you execute shell commands using Python?

import subprocess  
result = subprocess.run(["df", "-h"], capture_output=True, text=True)  
print(result.stdout)
