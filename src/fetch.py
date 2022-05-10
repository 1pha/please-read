import json
import requests
import pandas as pd

with open("credentials.json", "r") as f:
    credentials = json.load(f)

NOTION_KEY = credentials["integration_token"]
DATABASE_ID = credentials["table_id"]
NOTION_URL = 'https://api.notion.com/v1/databases'
NOTION_VERSION = "2022-02-22"

HEADER = {"Authorization": f"Bearer {NOTION_KEY}",
                "Content-Type": "application/json",
                "Notion-Version": NOTION_VERSION}

body = {"sorts": []}

def fetch_papers():
    papers = []
    while True:

        url = f"{NOTION_URL}/{DATABASE_ID}/query"
        result = requests.post(url, data=json.dumps(body), headers=HEADER).json()
        papers.extend(result["results"])

        if result["has_more"]:
            body = {"sorts": [], "start_cursor": result["next_cursor"]}
        else:
            break

    return pd.DataFrame(papers)