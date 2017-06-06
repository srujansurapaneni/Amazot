# Boto 3
import boto3
ec2 = boto3.resource('ec2')

ec2.instances.filter(InstanceIds=ids).terminate()
