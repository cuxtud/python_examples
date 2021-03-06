import boto3
import logging
import requests
import json
from botocore.exceptions import ClientError
import time

mbname=morpheus['customOptions']['fbname']
user1=morpheus['customOptions']['fnoofusers']

#Create IAM User

def create_iam_User(usernameaa):
    iam = boto3.resource('iam')
    user = iam.User(usernameaa)
    user = user.create(
    PermissionsBoundary='arn:aws:iam::370459551696:policy/Morpheus-S3',
    UserName = usernameaa,
    Tags=[
        {
            'Key': 'Key 1',
            'Value': 'Value 1'
        },
    ]
)

#Add user to the group

def addto_group(usernameaa):
    iam = boto3.resource('iam')
    user = iam.User(usernameaa)
    user = user.add_group(
    GroupName='Morpheus'
)

def create_key(user_name):
    """
    Creates an access key for the specified user. Each user can have a
    maximum of two keys.
    :param user_name: The name of the user.
    :return: The created access key.
    """
    iam = boto3.resource('iam')
    try:
        key_pair = iam.User(user_name).create_access_key_pair()
    except ClientError:
        raise
    else:
        return key_pair

create_iam_User('anishtest3')
addto_group('anishtest3')
keys = create_key('anishtest3')
print(keys)

if user1 == "Two":
    create_iam_User('anishtest4')
    addto_group('anishtest4')
    keys2 = create_key('anishtest4')
    print(keys2)


#Create bucket policy for the 2 users

mresourcename='az-bucketpolicy' + mbname 
def policy(bucketname,resourcename):
    s3 = boto3.resource('s3')
    bucket_policy = s3.BucketPolicy(bucketname)
    newpolicy={
        "Statement": [
            {
            "Action": "s3:*",
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::" + bucketname,
            "Principal": {
                "AWS": [
                "arn:aws:iam::370459551696:user/anishtest3",
                "arn:aws:iam::370459551696:user/anishtest4"
                ]
            }
            }
        ]
    }
    jnewpolicy=json.dumps(newpolicy)
    response = bucket_policy.put(
    Policy=jnewpolicy
)
time.sleep(20)
policy(mbname,mresourcename)