import unittest
import os
from src.google_sheets_client import SheetsClient
from dotenv import load_dotenv

load_dotenv()
class TestSheetsClientReal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.credentials_file = os.getenv("GOOGLE_CREDENTIALS_FILE")
        cls.spreadsheet_name = os.getenv("SPREADSHEET_NAME")
        cls.worksheet_name = os.getenv("WORKSHEET_NAME")

        if not cls.credentials_file or not cls.spreadsheet_name or not cls.worksheet_name:
            raise ValueError("Required environment variables are not set. Please set GOOGLE_CREDENTIALS_FILE, SPREADSHEET_NAME, and WORKSHEET_NAME.")

        cls.sheets_client = SheetsClient(credentials_file=cls.credentials_file)

    def test_get_worksheet_data_success(self):
        try:
            result = self.sheets_client.get_worksheet_data(self.spreadsheet_name, self.worksheet_name)

            expected_result = [
                {
                    "Record ID": "Accept_Button",
                    "Character": "None",
                    "Russian": "Принять",  # Assuming this is the correct non-escaped format
                    "English (United States)": "Accept",
                    "Character limit": 0,
                    "Version": 1,
                    "NarrativeComment": "None"
                }
            ]
            self.assertEqual(result[0], expected_result[0])
        
        except ValueError as e:
            self.fail(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    unittest.main()
