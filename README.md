# Localization Engineering

## Overview

It's a project focused on synchronizing the data from your Google Sheets account into your Gridly account AND the other way around if need be. Orchestrated with a simple cron job to run at 6 PM everyday. Fit for small and quick localization batches. 
Streaming could be another option but is vastly an overkill for localization purposes. Complex orchestrations and custom pipelines are equally not worth it.
For anything major, large scale consider other options, for anything small and silly, regular cron sync is enough.

This one was made purely out of challenge it supposed.
Unless you're completely mental just use the already established:
[Gridly Client library for Python](https://github.com/gridly-spreadsheet-CMS/gridly-python-sdk)

## Features


- **Feature 1**: Synchronization of data between Google Sheets and Gridly accounts
- **Feature 2**: Support for multiple spreadsheets and worksheets within a single project
- **Feature 3**: Error handling for failed synchronizations
- **Feature 4**: Integration with the cron job system to automate syncs

## Usage

To use this project, you need to install the following dependencies:

1. [Python](https://www.python.org/) (version 3.8 or higher)
2. [venv](https://docs.python.org/3/library/venv.html)
3. [Google Sheets API client library for Python](https://developers.google.com/sheets/api/quickstart/python)

```bash
pip install -r requirements.txt
```

Here’s how you could use this project:

1. **Step 1**: Prepare all the necessary environment variables at the very least you need 
- `SPREADSHEET_NAME`
- `WORKSHEET_NAME`
- `GRIDLY_API_KEY`
- `VIEW_ID`
2. **Step 2**: Get the credentials.json from Google Sheets' API, it might be tedious and tricky and is probably the most annoying step
- `GOOGLE_CREDENTIALS_FILE`
3. **Step 3**: Adjust the code specific to your needs, you might not want to sync just a single view(though I like the granularity of it), but instead make a huge sync of all the views with a lot of sheets, let's say once a day/week or whatever.
4. **Step 4**: Use the sync python script according to your needs, briefly speaking, you'll set up the clients with your credentials, get your data one one specific SPREADSHIT and only one speicifc WORKSHEET(for the granularity purposes), process it, reformat into acceptable format for the other platform and fire up a happy notification if everything is successful, a sad one if something's wrong with the error message.

