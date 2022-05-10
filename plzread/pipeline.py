from plzread import fetch_papers, preprocess_raw_papers, sort_df

class Database:

    def __init__(self, credential_fname:str="credentials.json", top_pct:float=0.1):

        self.credential_fname = credential_fname
        self.top_pct = top_pct

    def fetch_papers(self, credential_fname:str=None):

        if credential_fname is None:
            credential_fname = self.credential_fname

        self.raw_papers = fetch_papers(credential_fname)
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

    def run(self):

        raw_papers = self.fetch_papers()
        df = self.to_dataframe(raw_papers)
        sorted_df = self.sort(df)
        return sorted_df

if __name__=="__main__":

    db = Database()
    print(db.run())