# Boto 3
import boto3
ec2 = boto3.resource('ec2')

# Boto 3
ec2.create_instances(ImageId='<ami-image-id>', MinCount=1, MaxCount=5)
