import requests
import json
from datetime import datetime

# --- YOUR CREDENTIALS ---
# Paste your master API key between the quotes below:
NOTION_TOKEN = "YOUR_NOTION_API_KEY_HERE"

# Your specific Database ID is already injected:
DATABASE_ID = "39c446c172508061b66ed08949f6ae7d"

# --- THE DATA YOU WANT TO LOG ---
activity_name = "Python Coding & API Practice"
hours_spent = 2.5
current_date = datetime.now().strftime("%Y-%m-%d")

# --- THE API SETUP ---
url = "https://api.notion.com/v1/pages"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# --- THE JSON PAYLOAD (Formatting for Notion) ---
data = {
    "parent": {"database_id": DATABASE_ID},
    "properties": {
        "Activity": {
            "title": [
                {
                    "text": {
                        "content": activity_name
                    }
                }
            ]
        },
        "Hours": {
            "number": hours_spent
        },
        "Date": {
            "date": {
                "start": current_date
            }
        }
    }
}

# --- SEND THE REQUEST ---
response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("SUCCESS! Check your Notion Database.")
else:
    print(f"FAILED. Error Code: {response.status_code}")
    print(response.text)
