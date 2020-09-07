import boto3
import datetime

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
    DBInstanceIdentifier='anisdbinstance',
    AllocatedStorage=100,
    DBInstanceClass='db.t3.small',
    Engine='sqlserver-ex',
    MasterUsername='anishadmin',
    MasterUserPassword='anis1sgpas23fh654',
    #DBParameterGroupFamily='string',
    DBParameterGroupName='default.sqlserver-ex-12.0',
    #DBSecurityGroups=[
    #    'default',
    #],
    #VpcSecurityGroupIds=[
    #    'sg-f90f86bd',
    #],
    #AvailabilityZone='string',
    DBSubnetGroupName='db_mysql_aurora',
    #PreferredMaintenanceWindow='string',
    #BackupRetentionPeriod=123,
    #PreferredBackupWindow='string',
    #Port=123,
    #MultiAZ=True,
    EngineVersion='12.00.6329.1.v1',
    #AutoMinorVersionUpgrade=True|False,
    #LicenseModel='string',
    #Iops=123,
    #OptionGroupName='string',
    #CharacterSetName='string',
    #PubliclyAccessible=True|False,
    Tags=[
        {
            'Key': 'Key 1',
            'Value': 'Value 1'
        },
    ],
    #DBClusterIdentifier='string',
    #StorageType='string',
    #TdeCredentialArn='string',
    #TdeCredentialPassword='string',
    #StorageEncrypted=True|False,
    #KmsKeyId='string',
    #Domain='string',
    CopyTagsToSnapshot=True
    #MonitoringInterval=123,
    #MonitoringRoleArn='string',
    #DomainIAMRoleName='string',
    #PromotionTier=123,
    #Timezone='string',
    #EnableIAMDatabaseAuthentication=True|False,
    #EnablePerformanceInsights=True|False,
    #PerformanceInsightsKMSKeyId='string',
    #PerformanceInsightsRetentionPeriod=123,
    #EnableCloudwatchLogsExports=[
    #    'string',
    #],
    #ProcessorFeatures=[
    #    {
    #        'Name': 'string',
    #        'Value': 'string'
    #    },
    #]
    #DeletionProtection=True|False,
    #MaxAllocatedStorage=123
)

# check Create DB instance returned successfully
#if response['ResponseMetadata']['HTTPStatusCode'] == 200:
#    print("Successfully create DB instance")
#else:
#    print("Couldn't create DB instance")