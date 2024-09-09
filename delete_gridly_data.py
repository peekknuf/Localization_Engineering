import os
import logging
from src.gridly_client import GridlyClient

def main():
    """
    If, for whatever reason, there's a need to drop all records for a specific view in Gridly.
    Feels unnecessary, the UI is super nice, but it's here just in case.
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    api_key = os.getenv("GRIDLY_API_KEY")
    view_id = os.getenv("GAME_VIEW_ID")
    
    if not api_key:
        raise ValueError("API key not provided. Please set GRIDLY_API_KEY in your environment variables.")
    if not view_id:
        raise ValueError("View ID not provided. Please set GRIDLY_VIEW_ID in your environment variables.")

    gridly_client = GridlyClient(api_key=api_key)

    try:
        logger.info(f"Attempting to delete all records from view: {view_id}")
        gridly_client.delete_all_records(view_id)
        logger.info("All records deleted successfully.")
    except RuntimeError as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
