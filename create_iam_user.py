import boto3

#Create IAM User

def create_iam_User(usernameaa):
    iam = boto3.resource('iam')
    user = iam.User(usernameaa)
    user = user.create(
    #Path='string',
    PermissionsBoundary='arn:aws:iam::370459551696:policy/Morpheus-S3',
    UserName = usernameaa,
    Tags=[
        {
            'Key': 'Key 1',
            'Value': 'Value 1'
        },
    ]
)

def addto_group(usernameaa):
    iam = boto3.resource('iam')
    user = iam.User(usernameaa)
    user = user.add_group(
    GroupName='Morpheus'
)
def create_keys(usernameaa):
    iam = boto3.client('iam')
    response = iam.create_access_key(UserName=usernameaa)
    print (response)

create_iam_User('anishtest1')
addto_group('anishtest1')
create_keys('anishtest1')

