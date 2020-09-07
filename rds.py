import boto3
ENGINE_NAME = 'mysql'
ENGINE_VERSION = '5.7.00'
DB_INSTANCE_TYPE = 'm1.small'
DB_NAME = 'mysql_db'
DB_USER_NAME = 'db_user1'
DB_USER_PASSWORD = 'db_pass123'

# Create DB instance
client = boto3.client('rds')
respone = client.create_db_instance(
    DBName='',
    DBInstanceIdentifier='',
    AllocatedStorage=,
    DBInstanceClass='',
    Engine='',
    MasterUsername='',
    MasterUserPassword='',
    DBParameterGroupName='',
)

# check Create DB instance returned successfully
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("Successfully create DB instance")
else:
    print("Couldn't create DB instance")