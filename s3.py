import boto3
import time

mbname=morpheus['customOptions']['fbname']


def create_bucket(bucket_name):
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=bucket_name)

#create bucket with the name provided when Operational workflow is executed
create_bucket(mbname)

#Sleep for 10secs for the bucket to be created
time.sleep(10)

#Get the tags and then set them on the new bucket
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
