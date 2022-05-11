from .fetch import fetch_papers
from .preprocess import preprocess_raw_papers
from .sort import sort_df


class Database:
    def __init__(
        self, credential_fname: str = "credentials.json", top_pct: float = 0.1
    ):

        self.credential_fname = credential_fname
        self.top_pct = top_pct

    def _fetch_papers(self, credential_fname: str = None):

        if credential_fname is None:
            credential_fname = self.credential_fname

        self.raw_papers = fetch_papers(credential_fname)
        return self.raw_papers

    def fetch_papers(self, NOTION_KEY, DATABASE_ID):

        from plzread.fetch import _fetch_papers

        self.raw_papers = _fetch_papers(NOTION_KEY, DATABASE_ID)
        return self.raw_papers

    def to_dataframe(self, raw_papers: list = None):

        if raw_papers is None:
            raw_papers = self.raw_papers

        self.df = preprocess_raw_papers(raw_papers)
        return self.df

    def sort(self, df=None, top_pct: float = None):

        if df is None:
            df = self.df

        if top_pct is None:
            top_pct = self.top_pct

        self.sorted_df = sort_df(df)
        return self.sorted_df

    def run(self, NOTION_KEY, DATABASE_ID):

        raw_papers = self.fetch_papers(NOTION_KEY, DATABASE_ID)
        df = self.to_dataframe(raw_papers)
        sorted_df = self.sort(df)
        return sorted_df


if __name__ == "__main__":

    db = Database()
    print(db.run())
