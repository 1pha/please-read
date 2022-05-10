import pandas as pd

def status_numerizer(status: list):

    if status is None:
        return 4

    if "★" in status:
        return 1
    
    elif "Unread" in status:
        return 2

    else:
        return 3

def sort_df(df: pd.DataFrame, top_pct: float = 0.1):

    df["Status Priority"] = df["Status"].apply(status_numerizer)
    sorted_df = df.sort_values(by=["Status Priority", "Added on."], ascending=True)
    sorted_df = sorted_df.loc[:int(len(sorted_df) * top_pct)]
    return sorted_df