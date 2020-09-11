import boto3

#Create IAM User

def create_iam_User(usernameaa):
    iam = boto3.resource('iam')
    user = iam.User(usernameaa)
    user = user.create(
    #Path='string',
    PermissionsBoundary='arn:aws:iam::370459551696:policy/Morpheus-S3',
    user_name = usernameaa,
    Tags=[
        {
            'Key': 'Key 1',
            'Value': 'Value 1'
        },
    ]
)

create_iam_User('anishtest')
