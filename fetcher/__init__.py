# # This function is not intended to be invoked directly. Instead it will be
# # triggered by an orchestrator function.
# # Before running this sample, please:
# # - create a Durable orchestration function
# # - create a Durable HTTP starter function
# # - add azure-functions-durable to requirements.txt
# # - run pip install -r requirements.txt
from azure.storage.blob import BlobServiceClient

STORAGEACCOUNTURL = 'https://assignement.blob.core.windows.net'
STORAGEACCOUNTKEY = 'my secret key ;)'
CONTAINERNAME = 'barth-container'


def main(name: str) -> dict:
    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(STORAGEACCOUNTURL, STORAGEACCOUNTKEY)
    container_client = blob_service_client.get_container_client('barth-container')
    blob_list = container_client.list_blobs()
    
    files = {}
    
    for blob in blob_list:
        blob_client = blob_service_client.get_blob_client(CONTAINERNAME, blob.name, snapshot=None)
        blob_data = blob_client.download_blob()
        
        data = blob_data.readall().decode("utf-8")
        lines = data.splitlines()
        
        splitted_data = {i: line for i, line in enumerate(lines)}
        files[blob.name] = splitted_data

    return files
