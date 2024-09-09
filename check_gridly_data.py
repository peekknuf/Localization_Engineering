from src.gridly_client import GridlyClient
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    """
    Checking if the method even works + getting the shape of the data for further development
    """
    api_key = os.getenv("GRIDLY_API_KEY")
    view_id = os.getenv("GAME_VIEW_ID")
    if not api_key:
        raise ValueError("API key not provided. Please set GRIDLY_API_KEY in your environment variables.")

    gridly_client = GridlyClient(api_key=api_key)

    try:
        data = gridly_client.get_view_data(view_id)

        print("Data retrieved from Gridly:")
        for record in data:
            print(record)
            print()

    except RuntimeError as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
