import unittest
from unittest.mock import patch, MagicMock
from src.gridly_client import GridlyClient
import os

class TestGridlyClient(unittest.TestCase): 
    @patch.dict(os.environ, {"GRIDLY_API_KEY": "fake_api_key", "GRIDLY_VIEW_ID": "fake_view_id"})
    @patch("src.gridly_client.requests.get")
    def test_get_view_data_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                'id': 'Accept_Button',
                'cells': [
                    {'columnId': 'column1', 'value': 'None'},
                    {'columnId': 'column2', 'sourceStatus': 'readyForTranslation', 'value': 'Принять'},
                    {'columnId': 'column3', 'dependencyStatus': 'upToDate', 'value': 'Accept'},
                    {'columnId': 'column4', 'value': '0'},
                    {'columnId': 'column5', 'value': '1'},
                    {'columnId': 'column6', 'value': 'None'}
                ],
                'lastModifiedBy': 'peekknuf@gmail.com',
                'path': 'Static Texts'
            }
        ]
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        api_key = os.getenv("GRIDLY_API_KEY")
        view_id = os.getenv("STATIC_VIEW_ID")
        gridly_client = GridlyClient(api_key=api_key)

        data = gridly_client.get_view_data(view_id)

        expected_first_record = {
            'id': 'Accept_Button',
            'cells': [
                {'columnId': 'column1', 'value': 'None'},
                {'columnId': 'column2', 'sourceStatus': 'readyForTranslation', 'value': 'Принять'},
                {'columnId': 'column3', 'dependencyStatus': 'upToDate', 'value': 'Accept'},
                {'columnId': 'column4', 'value': '0'},
                {'columnId': 'column5', 'value': '1'},
                {'columnId': 'column6', 'value': 'None'}
            ],
            'lastModifiedBy': 'peekknuf@gmail.com',
            'path': 'Static Texts'
        }

        self.assertEqual(data[0], expected_first_record)
        mock_get.assert_called_once_with(
            f"https://api.gridly.com/v1/views/{view_id}/records",
            headers={
                "Authorization": f"ApiKey {api_key}",
                "Content-Type": "application/json"
            }
        )

if __name__ == "__main__":
    unittest.main()
