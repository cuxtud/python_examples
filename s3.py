import boto3
import time

#Setting user inputs as global vars
mbname=morpheus['customOptions']['fbname']
s3region=morpheus['customOptions']['fregion']

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
def set_bucket_tags(bucket, **new_tags):
    session = boto3.session.Session(profile_name='default')
    client = session.client('s3')
    response = client.put_bucket_tagging(
        Bucket=bucket,
        Tagging={
            'TagSet': [
                {'Key': str(k), 'Value': str(v)} 
                for k, v in new_tags.items()
                ]
        }
    )

#Call the function with key value pairs for tags
set_bucket_tags(mbname, key 1="value1", key2="value2", key3="value3")

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