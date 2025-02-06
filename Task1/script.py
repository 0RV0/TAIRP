from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define the required scope
SCOPES = ['https://www.googleapis.com/auth/drive']

# Set up OAuth 2.0 credentials
SERVICE_ACCOUNT_FILE = 'service-account-key.json'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Create a Drive API service
drive_service = build('drive', 'v3', credentials=creds)

# Upload a file to Google Drive
def upload_file(file_path, file_name):
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_path, resumable=True)
    
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    return file.get('id')

# Share a file with a specific user
def share_file(file_id, email):
    permission = {
        'type': 'user',
        'role': 'writer',  # Can be 'reader', 'writer', 'commenter', etc.
        'emailAddress': email
    }
    
    drive_service.permissions().create(
        fileId=file_id,
        body=permission,
        fields='id'
    ).execute()

# Example usage:
if __name__ == "__main__":
    file_path = 'path/to/your/file.txt'
    file_name = 'file.txt'
    user_email = 'user@example.com'

    file_id = upload_file(file_path, file_name)
    share_file(file_id, user_email)
