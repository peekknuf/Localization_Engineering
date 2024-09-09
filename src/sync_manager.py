import logging
from src.google_sheets_client import SheetsClient
from src.gridly_client import GridlyClient

class SyncManager:
    def __init__(self, sheets_client: SheetsClient, gridly_client: GridlyClient):
        self.sheets_client = sheets_client
        self.gridly_client = gridly_client
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def sync_sheets_to_gridly(self, spreadsheet_name: str, worksheet_name: str, view_id: str):
        try:
            self.logger.info(f"Starting sync from Sheets to Gridly: {spreadsheet_name}/{worksheet_name} -> {view_id}")
            sheets_data = self.sheets_client.get_worksheet_data(spreadsheet_name, worksheet_name)
            gridly_data = self.transform_sheets_data_to_gridly(sheets_data)
            self.gridly_client.update_view(view_id, gridly_data)
            self.logger.info("Sync from Sheets to Gridly completed successfully")
        except Exception as e:
            self.logger.error(f"Error during sync from Sheets to Gridly: {str(e)}")
            raise

    def sync_gridly_to_sheets(self, view_id: str, spreadsheet_name: str, worksheet_name: str):
        try:
            self.logger.info(f"Starting sync from Gridly to Sheets: {view_id} -> {spreadsheet_name}/{worksheet_name}")
            gridly_data = self.gridly_client.get_view_data(view_id)
            sheets_data = transform_gridly_data_to_sheets(gridly_data)
            self.sheets_client.update_worksheet(spreadsheet_name, worksheet_name, sheets_data)
            self.logger.info("Sync from Gridly to Sheets completed successfully")
        except Exception as e:
            self.logger.error(f"Error during sync from Gridly to Sheets: {str(e)}")
            raise


    def transform_sheets_data_to_gridly(self, sheets_data):
        """
        
        Пожалуй самый душный момент всего задания — преобразование данных из формата Sheets в формат Gridly.
        
        """
        column_mapping = {
            "Character": "column1",
            "Russian": "column2",
            "English (United States)": "column3",
            "Character limit": "column4",
            "Version": "column5",
            "NarrativeComment": "column6"
        }
        
        column_order = [v for k, v in column_mapping.items()]
        
        if not isinstance(sheets_data, list):
            sheets_data = [sheets_data]
        
        transformed_records = []
        
        for record in sheets_data:
            transformed_record = {
                'id': record.get("Record ID", ""),
                'cells': []
            }
            
            cell_dict = {}
            
            for key, value in record.items():
                column_id = column_mapping.get(key)
                if column_id:
                    cell_value = str(value) if not isinstance(value, str) else value
                    cell = {'columnId': column_id, 'value': cell_value}
                    
                    if column_id == "column2":
                        cell['sourceStatus'] = 'readyForTranslation'
                    elif column_id == "column3":
                        cell['dependencyStatus'] = 'upToDate'
                    
                    cell_dict[column_id] = cell
            
            for column_id in column_order:
                if column_id in cell_dict:
                    transformed_record['cells'].append(cell_dict[column_id])
            
            transformed_records.append(transformed_record)
        
        return transformed_records


def transform_gridly_data_to_sheets(gridly_data):
    def get_value_from_column(cells, column_id):
        for cell in cells:
            if cell['columnId'] == column_id:
                return cell.get('value', None)
        return None

    transformed_data = []

    for record in gridly_data:
        transformed_record = {
            "Record ID": record.get('id'),
            "Character": get_value_from_column(record['cells'], 'column1'),
            "Russian": get_value_from_column(record['cells'], 'column2'),
            "English (United States)": get_value_from_column(record['cells'], 'column3'),
            "Character limit": int(get_value_from_column(record['cells'], 'column4')),
            "Version": int(get_value_from_column(record['cells'], 'column5')),
            "NarrativeComment": get_value_from_column(record['cells'], 'column6'),
        }
        transformed_data.append(transformed_record)

    return transformed_data
