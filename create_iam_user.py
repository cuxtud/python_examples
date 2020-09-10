import boto3

#Create IAM User

def create_iam_User():
    iam = boto3.resource('iam')
    user = iam.User('anishtest')
    user = user.create(
    #Path='string',
    PermissionsBoundary='arn:aws:iam::370459551696:policy/Morpheus-S3',
    user_name = 'anishtest',
    Tags=[
        {
            'Key': 'Key 1',
            'Value': 'Value 1'
        },
    ]
)