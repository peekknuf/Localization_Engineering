# Localization Engineering

## Overview

It's a project focused on synchronizing the data from your Google Sheets account into your Gridly account AND the other way around if need be. Orchestrated with a simple cron job to run at 6 PM everyday. Fit for small and quick localization batches. For anything major consider other options.

## Features


- **Feature 1**: Synchronization of data between Google Sheets and Gridly accounts
- **Feature 2**: Support for multiple spreadsheets and worksheets within a single project
- **Feature 3**: Error handling for failed synchronizations
- **Feature 4**:Integration with the cron job system to automate syncs

## Usage

To use this project, you need to install the following dependencies:

1. [Python](https://www.python.org/) (version 3.8 or higher)
2. [Pipenv](https://pipenv.pypa.io/) (version 20.0 or higher)
3. [Google Sheets API client library for Python](https://developers.google.com/sheets/api/quickstart/python)
4. [Gridly Client library for Python](https://github.com/gridly-dev/gridly-python-sdk)

```bash
[pip install -r requirements.txt]
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

## MIT License

Copyright (c) 2024 Maksym Ionutsa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
