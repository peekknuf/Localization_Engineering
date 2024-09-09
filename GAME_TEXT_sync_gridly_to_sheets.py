import os
import logging
from src.gridly_client import GridlyClient
from src.google_sheets_client import SheetsClient
from src.sync_manager import SyncManager
from dotenv import load_dotenv

load_dotenv()

def main():
    logging.basicConfig(level=logging.INFO)

    api_key = os.getenv("GRIDLY_API_KEY")
    view_id = os.getenv("GAME_VIEW_ID")
    google_credentials = os.getenv("GOOGLE_CREDENTIALS_FILE")
    spreadsheet_name = os.getenv("SPREADSHEET_NAME")
    worksheet_name = os.getenv("WORKSHEET_NAME2")

    if not api_key or not google_credentials:
        raise ValueError("Please set the environment variables for Gridly API and Google Sheets credentials.")
    gridly_client = GridlyClient(api_key)
    sheets_client = SheetsClient(credentials_file=google_credentials)

    sync_manager = SyncManager(sheets_client, gridly_client)

    try:
        sync_manager.sync_gridly_to_sheets(view_id, spreadsheet_name, worksheet_name)
        print(f"Successfully synced data from Gridly to Google Sheets: {spreadsheet_name}/{worksheet_name}")
    except Exception as e:
        print(f"An error occurred during syncing: {e}")

if __name__ == "__main__":
    main()