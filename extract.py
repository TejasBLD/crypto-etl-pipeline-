import pandas as pd
import requests
import schedule
import time
from datetime import datetime,timezone
import os

def fetching_data():
    print(f"fetching data at {datetime.now(timezone.utc)}...")
    try:
        
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params={
            "vs_currency":"inr",
            "ids":"Bitcoin,ethereum"
    }
        response=requests.get(url,params=params)
        response.raise_for_status()
        data=response.json()
        df=pd.DataFrame(data)
        cols=["id","symbol","current_price","market_cap","total_volume","last_updated"]
        df=df[cols]
        df["fetched_at"]=datetime.now(timezone.utc)
    
        header= not os.path.exists('crypto_price.csv')
        df.to_csv("crypto_price.csv", index=False,mode="a",header=header)
        print(f"Data saved to crypto_price.csv")
    except Exception as e:
        print(f"ERROR in TRANSFORMING & LOADING JOB :{e}")
if __name__=="__main__":
    schedule.every(5).minutes.do(fetching_data)
    print("Extractor started. Will run every 5 minutes.")
    
    fetching_data()
    while True:
        schedule.run_pending()
        time.sleep(1)
    
        