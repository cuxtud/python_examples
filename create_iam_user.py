import boto3

mbname=morpheus['customOptions']['fbname']
user1=morpheus['customOptions']['fnoofusers']

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
    print "check if this prints"
    print (response)

create_iam_User('anishtest1')
addto_group('anishtest1')
create_keys('anishtest1')

#Create bucket policy for the 2 users

def policy(bucketname):
    s3 = boto3.resource('s3')
    bucket_policy = s3.BucketPolicy(bucketname)
    response = bucket_policy.put(
    ConfirmRemoveSelfBucketAccess=True,
    Policy='string',
    ExpectedBucketOwner='string'
)