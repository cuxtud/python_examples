# Import the needed credential and management objects from the libraries.
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
import os

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
#subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
subscription_id = "3b6ff759-299c-4a48-bef8-d1e612b57658"

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

# Provision the resource group.
rg_result = resource_client.resource_groups.create_or_update(
    "PythonAzureExample-rg",
    {
        "location": "centralus"
    }
)
print(rg_result.name)

# Within the ResourceManagementClient is an object named resource_groups,
# which is of class ResourceGroupsOperations, which contains methods like
# create_or_update.
#
# The second parameter to create_or_update here is technically a ResourceGroup
# object. You can create the object directly using ResourceGroup(location=LOCATION)
# or you can express the object as inline JSON as shown here. For details,
# see Inline JSON pattern for object arguments at
# https://docs.microsoft.com/azure/developer/python/azure-sdk-overview#inline-json-pattern-for-object-arguments.

print('Provisioned resource group {rg_result.name} in the {rg_result.location} region')

# The return value is another ResourceGroup object with all the details of the
# new group. In this case the call is synchronous: the resource group has been
# provisioned by the time the call returns.

# Update the resource group with tags
rg_result = resource_client.resource_groups.create_or_update(
    "PythonAzureExample-rg",
    {
        "location": "centralus",
        "tags": { "environment":"test", "department":"tech" }
    }
)

print('Updated resource group {rg_result.name} with tags')

# Optional lines to delete the resource group. begin_delete is asynchronous.
# poller = resource_client.resource_groups.begin_delete(rg_result.name)
# result = poller.result()