# Data Backup and Restore with Azure Blob Storage

This project demonstrates how to back up and restore files using Azure Blob Storage with Python.

## Prerequisites

Before running the script, ensure you have the following:
- An **Azure Storage Account**
- A **Storage Container** in Azure Blob Storage
- An **Azure Connection String**
- Python 3 installed
- Required Python libraries installed

## Setup

### Step 1: Install Required Libraries
Run the following command to install dependencies:
```sh
pip install azure-storage-blob
```

### Step 2: Configure the Script
1. Replace `your_connection_string_here` in `AZURE_CONNECTION_STRING` with your actual Azure Storage connection string.
2. Replace `your-container-name` with your Azure Blob Storage container name.

### Step 3: Run the Script
Execute the script with:
```sh
python azure_blob_backup.py
```

## How It Works
- **Upload File**: The script uploads `backup.zip` to Azure Blob Storage.
- **Download File**: The script downloads the file as `restored_backup.zip`.

## Notes
- Ensure your Azure Storage account has proper access permissions.
- Modify file paths as needed for your specific backup and restore requirements.

Happy coding!
