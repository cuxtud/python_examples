import boto3
import time

mbname=morpheus['customOptions']['fbname']
s3region=morpheus['customOptions']['fregion']
print(s3region)

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

#Get the tags and then set them on the new bucket
'''
s3 = boto3.resource('s3')
bucket_tagging = s3.BucketTagging(mbname)
Set_tag = bucket_tagging.put(
    Tagging={
        'TagSet' :[
            {
                'Key':'Key1',
                'Value':'Value1'
            },
        ]
    }
)
'''
def set_bucket_tags(bucket, update=True, **new_tags):
    session = boto3.session.Session(profile_name='default')
    client = session.client('s3')
    response = client.put_bucket_tagging(
        Bucket=bucket,
        Tagging={
            'TagSet': [{'Key': str(k), 'Value': str(v)} for k, v in new_tags.items()]
        }
    )

set_bucket_tags(mbname, True, key1="value1", key2="value2", key3="value3")

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