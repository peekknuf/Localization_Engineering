from src.sync_manager import SyncManager
class MockSheetsClient:
    pass
class MockGridlyClient:
    pass
def test_transform_sheets_data_to_gridly():
    sync_manager = SyncManager(sheets_client=MockSheetsClient(), gridly_client=MockGridlyClient())
    single_record = {
        "Record ID": "GameTip_16",
        "Character": "John",
        "Russian": "\u0417\u0430\u0432\u043e\u0434\u0438\u043c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c...",
        "English (United States)": "Starting the engine...",
        "Character limit": 50,
        "Version": 1,
        "NarrativeComment": "-"
    }

    list_of_records = [single_record]

    print("\nTesting list of records:")
    transformed_list = sync_manager.transform_sheets_data_to_gridly(list_of_records)
    print(transformed_list)
   
test_transform_sheets_data_to_gridly()
