# Cloud-Based File Sharing with Google Drive API

This project enables you to upload and share files on Google Drive using Python and the Google Drive API.

## Prerequisites

Before running this script, ensure you have the following:
- A Google Cloud Project with Google Drive API enabled
- A Service Account with a JSON key file
- Python installed (3.x recommended)
- Required Python libraries installed: `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, and `google-api-python-client`

## Setup Guide

### Step 1: Enable Google Drive API
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Navigate to **APIs & Services** > **Library**.
4. Search for and enable **Google Drive API**.

### Step 2: Create a Service Account
1. In **APIs & Services**, go to **Credentials**.
2. Click **Create Credentials** > **Service Account**.
3. Fill in the required details and click **Create and Continue**.
4. Under **Grant this service account access**, assign the **Editor** role (or a more restrictive role if preferred).
5. Click **Done**, then open the new service account.
6. Under **Keys**, click **Add Key** > **Create new key**.
7. Select **JSON** and click **Create**. A `.json` file will be downloaded.

### Step 3: Install Required Python Libraries
Run the following command to install dependencies:
```sh
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Step 4: Configure the Script
1. Save the downloaded JSON key file in the project directory.
2. Rename it to `service-account-key.json`.
3. Create a Python script file `script.py` and copy the script provided in this repository.

### Step 5: Run the Script
Execute the script with:
```sh
python script.py
```
This will upload the file and share it with the specified user.

## How It Works
1. **Authentication:** Uses service account credentials to authenticate with Google Drive API.
2. **File Upload:** Uploads a specified file to Google Drive.
3. **Sharing Permissions:** Grants write access to a specific user.

## Notes
- The service account needs access to the Drive folder where you want to upload files.
- The `role` in `share_file()` can be adjusted to `'reader'`, `'commenter'`, or `'writer'`.
- Modify the script to handle folder uploads or other permission settings as needed.
