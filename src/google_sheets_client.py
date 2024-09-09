import gspread
from google.oauth2.service_account import Credentials
from typing import List, Dict, Any
from gspread.exceptions import SpreadsheetNotFound, WorksheetNotFound

class SheetsClient:
    def __init__(self, credentials_file: str):
        scopes = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        try:
            credentials = Credentials.from_service_account_file(credentials_file, scopes=scopes)
            self.client = gspread.authorize(credentials)
        except FileNotFoundError:
            raise FileNotFoundError(f"Credentials file '{credentials_file}' not found.")
        except ValueError as e:
            raise ValueError(f"Invalid credentials file: {str(e)}")

    def get_worksheet_data(self, spreadsheet_name: str, worksheet_name: str) -> List[Dict[str, Any]]:
        try:
            sheet = self.client.open(spreadsheet_name).worksheet(worksheet_name)
            return sheet.get_all_records()
        except SpreadsheetNotFound:
            raise ValueError(f"Spreadsheet '{spreadsheet_name}' not found.")
        except WorksheetNotFound:
            raise ValueError(f"Worksheet '{worksheet_name}' not found in spreadsheet '{spreadsheet_name}'.")

    def update_worksheet(self, spreadsheet_name: str, worksheet_name: str, data: List[Dict[str, Any]]):
        try:
            sheet = self.client.open(spreadsheet_name).worksheet(worksheet_name)
            sheet.clear()
            if data:
                headers = list(data[0].keys())
                values = [list(row.values()) for row in data]
                sheet.append_rows([headers] + values)
        except SpreadsheetNotFound:
            raise ValueError(f"Spreadsheet '{spreadsheet_name}' not found.")
        except WorksheetNotFound:
            raise ValueError(f"Worksheet '{worksheet_name}' not found in spreadsheet '{spreadsheet_name}'.")
        except gspread.exceptions.APIError as e:
            raise RuntimeError(f"Error updating worksheet: {str(e)}")
