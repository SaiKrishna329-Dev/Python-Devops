# Get Public IPs of Running EC2 Instances

import boto3

def get_running_instances_public_ips(region="us-east-1"):
    ec2 = boto3.client("ec2", region_name=region)

    # Describe running instances
    response = ec2.describe_instances(
        Filters=[
            {"Name": "instance-state-name", "Values": ["running"]}
        ]
    )

    public_ips = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            ip = instance.get("PublicIpAddress")
            if ip:
                public_ips.append({
                    "InstanceId": instance["InstanceId"],
                    "PublicIP": ip
                })
    return public_ips


if __name__ == "__main__":
    region = "us-east-1" 
    ips = get_running_instances_public_ips(region)

    if ips:
        print("Public IPs of running instances:")
        for inst in ips:
            print(f"{inst['InstanceId']}: {inst['PublicIP']}")
    else:
        print("No running instances with public IPs found.")
