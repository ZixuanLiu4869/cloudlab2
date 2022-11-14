# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from azure.storage.blob import BlobServiceClient


def main(name:str) -> list:
    try:
        lines = []
        num = 0
        print("Azure Blob Storage Python quickstart sample")
        AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=mapreducezixuanliu;AccountKey=9ChPx5lB5sgzJ3XADgji4hxjmUU+nKLRBGA9vdRLr3eH9+u0ndibxBdNXYfbSumfN50q3cMJ9jiF+AStRDFL9g==;EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(container="mycontainer")
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            file = container_client.download_blob(blob.name).readall()
            file = str(file, encoding='utf-8').split('\r\n')
            for line in file:
                lines.append((num, line))
                num += 1

        print(lines)
    except Exception as ex:
        print('Exception:')
        print(ex)

    return lines