from azure.storage.blob import BlobServiceClient
import os

# Azure Storage account connection string
AZURE_CONNECTION_STRING = "your_connection_string_here"
CONTAINER_NAME = "your-container-name"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

def upload_file(local_file_path, blob_name):
    """Uploads a file to Azure Blob Storage."""
    with open(local_file_path, "rb") as data:
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data, overwrite=True)
    print(f"Uploaded {local_file_path} to Azure Blob Storage as {blob_name}")

def download_file(blob_name, download_path):
    """Downloads a file from Azure Blob Storage."""
    blob_client = container_client.get_blob_client(blob_name)
    with open(download_path, "wb") as file:
        file.write(blob_client.download_blob().readall())
    print(f"Downloaded {blob_name} to {download_path}")

# Example usage
if __name__ == "__main__":
    upload_file("backup.zip", "backup.zip")
    download_file("backup.zip", "restored_backup.zip")
