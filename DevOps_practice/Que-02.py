# Write a Python script that terminates EC2 instances older than 30 days.

import boto3
from datetime import datetime, timezone, timedelta

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Define time threshold
days_threshold = 30
cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_threshold)  # calculates the date and time for “X days ago”

# Describe all instances
response = ec2.describe_instances(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
    ]
)

instances_to_terminate = []

# Loop through all reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        launch_time = instance['LaunchTime']  # Already in UTC
        
        if launch_time < cutoff_date:
            print(f"Instance {instance_id} launched at {launch_time} — eligible for termination.")
            instances_to_terminate.append(instance_id)

# Terminate eligible instances
if instances_to_terminate:
    print("\nTerminating instances:", instances_to_terminate)
    terminate_response = ec2.terminate_instances(InstanceIds=instances_to_terminate)
    print("Termination initiated:", terminate_response)
else:
    print("No instances older than 30 days found.")
