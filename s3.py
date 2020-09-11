import boto3
import time

#Setting user inputs as global vars
mbname=morpheus['customOptions']['fbname']
s3region=morpheus['customOptions']['fregion']
user1=morpheus['customOptions']['fnoofusers']

def create_bucket(bucket_name,bucket_region):
    s3_client = boto3.client('s3')
    if bucket_region == 'eu-west-1':
        s3_client = boto3.client('s3')
        s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': bucket_region
        }
    )
    else:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)

#create bucket with the name provided when Operational workflow is executed
create_bucket(mbname,s3region)

#Sleep for 10secs for the bucket to be created
time.sleep(10)

#Update tags to the bucket created
def set_bucket_tags(bucket):
   s3 = boto3.resource('s3')
   bucket_tagging = s3.BucketTagging(bucket)
   response = bucket_tagging.put(
        Tagging = {
            'TagSet': [
                {
                    'Key': 'Key 1', 
                    'Value': 'Value 1'
                },
                {
                    'Key': 'Key 2',
                    'Value': 'Value 2'
                } 
            ]    
        }
    )

set_bucket_tags(mbname)

#Enable versioning
def bucket_versioning(bucket_name):
    s3 = boto3.resource('s3')
    bucket_versioning = s3.BucketVersioning(bucket_name)
    response = bucket_versioning.enable()
    
#Check if versioning is required
fbversion=morpheus['customOptions']['fbversion'] 
if fbversion == 'yes':
    bucket_versioning(mbname)
else:
    print('Versioning is not enabled')


flogvalue=morpheus['customOptions']['flogvalue']

#Setup Logging
def blogging(logboolean):
    if logboolean == 'yes':
        s3 = boto3.client('s3')
        #bucket_logging = s3.BucketLogging(mbname)
        response = s3.put_bucket_logging(
            Bucket=mbname,
            BucketLoggingStatus={
                'LoggingEnabled': {
                    'TargetBucket': mbname,
                    'TargetGrants': [
                        {
                            'Grantee': {
                                'DisplayName': 'cuxtud',
                                'EmailAddress': 'vjanish1984@gmail.com',
                                'ID': '23',
                                'Type': 'AmazonCustomerByEmail',
                                'URI': 'string'
                            },
                            'Permission': 'FULL_CONTROL'
                        },
                    ],
                    'TargetPrefix': mbname
                }
            }
        )
    else:
        print('Logging not requested')

#blogging(flogvalue)

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

#create access and secret keys for the user
def create_keys(usernameaa):
    iam = boto3.client('iam')
    response = iam.create_access_key(UserName=usernameaa)
    print (response)

if user1 == '2':
    create_iam_User('anishtest1')
    addto_group('anishtest1')
    create_keys('anishtest1')
    create_iam_User('anishtest2')
    addto_group('anishtest2')
    create_keys('anishtest2')
else:
    create_iam_User('anishtest1')
    addto_group('anishtest1')
    create_keys('anishtest1')