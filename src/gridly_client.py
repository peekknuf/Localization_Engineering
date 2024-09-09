import requests
from typing import List, Dict, Any

class GridlyClient:
    BASE_URL = "https://eu-central-1.api.gridly.com/v1"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"ApiKey {self.api_key}",
            "Content-Type": "application/json",
            'Accept': 'application/json'
        }

    def get_view_data(self, view_id: str) -> List[Dict[str, Any]]:
        url = f"{self.BASE_URL}/views/{view_id}/records"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error fetching data from Gridly: {str(e)}")

    def update_view(self, view_id: str, data: List[Dict[str, Any]]):
        url = f"{self.BASE_URL}/views/{view_id}/records"
        try:
            self.delete_all_records(view_id)
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error updating data in Gridly: {str(e)}")

    def delete_all_records(self, view_id: str):
        url = f"{self.BASE_URL}/views/{view_id}/records"
        try:
            records = requests.get(url, headers=self.headers).json()
            record_ids = [record['id'] for record in records]

            if record_ids:
                requests.delete(url, headers=self.headers, json={"ids": record_ids}).raise_for_status()
                print("Successfully deleted requested records.")
            else:
                print("No records to delete.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error deleting records in Gridly: {str(e)}")