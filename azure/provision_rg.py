# Import the needed credential and management objects from the libraries.
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
import os

#retrieve the value entered by user in operational workflow from morpheus
rg_name=morpheus['customOptions']['fargname']

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from moprheus cypher.

subscription_id = "3b6ff759-299c-4a48-bef8-d1e612b57658"

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

# Provision the resource group.
rg_result = resource_client.resource_groups.create_or_update(
    rg_name,
    {
        "location": "centralus"
    }
)


print('Provisioned resource group %s in the %s region') % (rg_result.name, rg_result.location)

# Update the resource group with tags
rg_result = resource_client.resource_groups.create_or_update(
    rg_name,
    {
        "location": "centralus",
        "tags": { "environment":"test", "department":"tech" }
    }
)

print('Updated resource group %s with tags') % (rg_result.name)

## reference: https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-example-resource-group