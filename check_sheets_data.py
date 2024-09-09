import os
from src.google_sheets_client import SheetsClient
import json
from dotenv import load_dotenv

load_dotenv()

def main():
    """
    Pretty much the same logic, only for Sheets client
    """
    credentials_file = os.getenv("GOOGLE_CREDENTIALS_FILE")
    spreadsheet_name = os.getenv("SPREADSHEET_NAME")
    worksheet_name = os.getenv("WORKSHEET_NAME2")
    
    if not credentials_file or not spreadsheet_name or not worksheet_name:
        raise ValueError("Required environment variables are not set. Please set GOOGLE_CREDENTIALS_FILE, SPREADSHEET_NAME, and WORKSHEET_NAME in your environment.")

    sheets_client = SheetsClient(credentials_file=credentials_file)

    try:
        data = sheets_client.get_worksheet_data(spreadsheet_name, worksheet_name)
        
        print("Data retrieved from Google Sheets:")
        
        for record in data:
            print(json.dumps(record, indent=4))
            print()
    
    except ValueError as e:
        print(f"An error occurred: {str(e)}")
    except RuntimeError as e:
        print(f"An API error occurred: {str(e)}")

if __name__ == "__main__":
    main()
