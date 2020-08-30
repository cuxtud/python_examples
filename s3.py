import boto3

mbname=morpheus['customOptions']['fbname']
def create_bucket(bucket_name):
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=bucket_name)

create_bucket(mbname)