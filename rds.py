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
    DBName='anishdbtest01',
    DBInstanceIdentifier='anisdbinstance',
    AllocatedStorage=50,
    DBInstanceClass='db.t3.small',
    Engine='sqlserver-ex',
    MasterUsername='anishadmin',
    MasterUserPassword='anis1sgpas23fh654',
    DBParameterGroupName='anishdb',
    DBSecurityGroups=[
        'string',
    ],
    VpcSecurityGroupIds=[
        'string',
    ],
    #AvailabilityZone='string',
    DBSubnetGroupName='string',
    PreferredMaintenanceWindow='string',
    DBParameterGroupName='string',
    BackupRetentionPeriod=123,
    PreferredBackupWindow='string',
    #Port=123,
    MultiAZ=True|False,
    EngineVersion='12.00.6329.1.v1',
    #AutoMinorVersionUpgrade=True|False,
    LicenseModel='string',
    #Iops=123,
    #OptionGroupName='string',
    #CharacterSetName='string',
    #PubliclyAccessible=True|False,
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    #DBClusterIdentifier='string',
    #StorageType='string',
    #TdeCredentialArn='string',
    #TdeCredentialPassword='string',
    #StorageEncrypted=True|False,
    #KmsKeyId='string',
    #Domain='string',
    CopyTagsToSnapshot=True|False,
    #MonitoringInterval=123,
    #MonitoringRoleArn='string',
    #DomainIAMRoleName='string',
    #PromotionTier=123,
    #Timezone='string',
    #EnableIAMDatabaseAuthentication=True|False,
    #EnablePerformanceInsights=True|False,
    #PerformanceInsightsKMSKeyId='string',
    #PerformanceInsightsRetentionPeriod=123,
    '''
    EnableCloudwatchLogsExports=[
        'string',
    ],
    ProcessorFeatures=[
        {
            'Name': 'string',
            'Value': 'string'
        },
    ]
    '''
    #DeletionProtection=True|False,
    #MaxAllocatedStorage=123
)

# check Create DB instance returned successfully
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("Successfully create DB instance")
else:
    print("Couldn't create DB instance")