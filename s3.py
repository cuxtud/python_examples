import boto3

mbname=morpheus['customOptions']['fbname']
print(mbname)

def create_bucket(bucket_name):
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=bucket_name)

def set_bucket_keys(bucket_name, update=True, **new_tags):
    """
    Add/Update/Overwrite tags to AWS S3 Object

    :param bucket_key: Name of the S3 Bucket
    :param update: If True: appends new tags else overwrites all tags with **kwargs
    :param new_tags: A dictionary of key:value pairs 
    :return: True if successful 
    

    #  I prefer to have this var outside of the method. Added for completeness
    client = boto3.client('s3')   

    old_tags = {}

    if update:
        try:
            old = client.get_bucket_tagging(Bucket=bucket_name)
            old_tags = {i['Key']: i['Value'] for i in old['TagSet']}
        except Exception as e:
            print(e)
            print("there was no tag")

    new_tags = {**old_tags, **new_tags}

    response = client.put_bucket_tagging(
        Bucket=bucket_name,
        Tagging={
            'TagSet': [{'Key': str(k), 'Value': str(v)} for k, v in new_tags.items()]
        }
    )
    print(response)
    """


create_bucket(mbname)
#set_object_keys(mbname, True, name="My Name", colour="purple")

s3 = boto3.resource('s3')
bucket_tagging = s3.BucketTagging('mbname')
tags = bucket_tagging.tag_set
tags.append({'Key':'Owner', 'Value': 'owner'})
Set_tag = bucket_tagging.put(Tagging={'TagSet' :tags})
