import pandas as pd
import requests

def fetching_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params={
        "vs_currency":"inr",
        "ids":"Bitcoin,ethereum"
    }
    response=requests.get(url,params=params)
    data=response.json()
    df=pd.DataFrame(data)
    return df
if __name__=="__main__":
    df=fetching_data()
    print(df.head())
    
        