import boto3

mbname=morpheus['customOptions']['fbname']
print(mbname)

def create_bucket(bucket_name):
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=bucket_name)

def set_object_keys(bucket_name, key, update=True, **new_tags):
    """
    Add/Update/Overwrite tags to AWS S3 Object

    :param bucket_key: Name of the S3 Bucket
    :param update: If True: appends new tags else overwrites all tags with **kwargs
    :param new_tags: A dictionary of key:value pairs 
    :return: True if successful 
    """

    #  I prefer to have this var outside of the method. Added for completeness
    client = boto3.client('s3')   

    old_tags = {}

    if update:
        old = client.get_object_tagging(
            Bucket=bucket_name,
            Key=key,
        )

        old_tags = {i['Key']: i['Value'] for i in old['TagSet']}

    new_tags = {old_tags, new_tags}

    response = client.put_object_tagging(
        Bucket=bucket_name,
        Key=key,
        Tagging={
            'TagSet': [{'Key': str(k), 'Value': str(v)} for k, v in new_tags.items()]
        }
    )

    return response['ResponseMetadata']['HTTPStatusCode'] == 200

create_bucket(mbname)
set_object_keys(mbname, name="My Name", colour="purple")