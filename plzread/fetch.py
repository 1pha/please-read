import json

import requests
from typing import Tuple

NOTION_VERSION = "2022-02-22"


def _get_credentials(credential_fname: str = "credentials.json") -> Tuple[str, str]:

    try:
        with open(credential_fname, "r") as f:
            credentials = json.load(f)

        NOTION_KEY = credentials["integration_token"]
        DATABASE_ID = credentials["table_id"]
    except:
        print(f"Failed to load {credential_fname} json file. Manually give keys please")
        NOTION_KEY = input("Give Integration token starting with `secret_`")
        DATABASE_ID = input("Give DATABASE url without between notion.so/~ and ?v=...")

    return NOTION_KEY, DATABASE_ID


def fetch_papers(NOTION_KEY: str = None, DATABASE_ID: str = None) -> list:

    if NOTION_KEY is None and DATABASE_ID is None:
        # Use default credential.json
        NOTION_KEY, DATABASE_ID = _get_credentials()

    body = {"sorts": []}
    NOTION_URL = "https://api.notion.com/v1/databases"
    HEADER = {
        "Authorization": f"Bearer {NOTION_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }
    papers = []
    while True:

        url = f"{NOTION_URL}/{DATABASE_ID}/query"
        result = requests.post(url, data=json.dumps(body), headers=HEADER).json()
        papers.extend(result["results"])

        if result["has_more"]:
            body = {"sorts": [], "start_cursor": result["next_cursor"]}
        else:
            break

    return papers


if __name__ == "__main__":

    NOTION_KEY, DATABASE_ID = _get_credentials()
    print(fetch_papers(NOTION_KEY, DATABASE_ID))
