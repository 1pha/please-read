from typing import Dict, List

import pandas as pd

HIER_INFO = {
    "Date Published": "start",
    "Added on.": None,
    "Keyword": "name",
    "Status": "name",
    "Authors": "plain_text",
    "From": "name",
    "URL": None,
    "Paper": "plain_text",  # text
}


def _process_features(
    feature: dict,
) -> List[Dict,]:

    processed_feature = {}
    for used_key, inner_key in HIER_INFO.items():

        key = [k for k in feature[used_key].keys() if k not in ["id", "type"]][0]
        current_feature = feature[used_key][key]
        if (
            isinstance(current_feature, list) and len(current_feature) == 0
        ) or current_feature is None:
            # If current key does not contain any value
            processed_feature[used_key] = None
            continue

        if inner_key is None:  # No hierarchy inside current feature
            processed_feature[used_key] = current_feature

        else:
            if isinstance(current_feature, list):
                processed_feature[used_key] = [c[inner_key] for c in current_feature]
            else:
                processed_feature[used_key] = current_feature[inner_key]

    return processed_feature


def preprocess_raw_papers(papers: list) -> pd.DataFrame:

    df = pd.DataFrame(map(_process_features, [p["properties"] for p in papers]))
    return df
