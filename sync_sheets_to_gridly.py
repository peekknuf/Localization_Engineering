import os
from src.google_sheets_client import SheetsClient
from src.gridly_client import GridlyClient
from src.sync_manager import SyncManager
from dotenv import load_dotenv

load_dotenv()

def main():
    google_credentials_file = os.getenv("GOOGLE_CREDENTIALS_FILE")
    gridly_api_key = os.getenv("GRIDLY_API_KEY")
    gridly_view_id = os.getenv("GAME_VIEW_ID")
    spreadsheet_name = os.getenv("SPREADSHEET_NAME")
    worksheet_name = os.getenv("WORKSHEET_NAME2")

    if not all([google_credentials_file, gridly_api_key, gridly_view_id, spreadsheet_name, worksheet_name]):
        raise ValueError("One or more environment variables are missing. Please set GOOGLE_CREDENTIALS_FILE, GRIDLY_API_KEY, GRIDLY_VIEW_ID, SPREADSHEET_NAME, and WORKSHEET_NAME.")

    sheets_client = SheetsClient(credentials_file=google_credentials_file)
    gridly_client = GridlyClient(api_key=gridly_api_key)
    sync_manager = SyncManager(sheets_client=sheets_client, gridly_client=gridly_client)

    try:
        print(f"Syncing from Google Sheets '{spreadsheet_name}/{worksheet_name}' to Gridly view ID '{gridly_view_id}'...")
        sync_manager.sync_sheets_to_gridly(spreadsheet_name, worksheet_name, gridly_view_id)
        print("Sync completed successfully.")
    except Exception as e:
        print(f"An error occurred during the sync: {str(e)}")

if __name__ == "__main__":
    main()