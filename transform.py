import pandas as pd
def transform_data(df):
    df=df[['id','symbol','current_price','market_cap','last_updated']].copy()
    df['last_updated']=pd.to_datetime(df['last_updated'])
    return df

if __name__=='__main__':
    import extract
    df=extract.fetching_data()
    df=transform_data(df)
    print(df.head())