from sqlalchemy import create_engine
from transform import transform_data
from extract import fetching_data
from dotenv import load_dotenv
import os
import schedule
import time
import pandas as pd

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
csv_file_path='crypto_price.csv'

def etl_job():
    try:
        if not os.path.exists(csv_file_path) or os.path.getsize(csv_file_path)==0:
            print("CSV file is empty or does not exists.Skipping")
            return
        raw_df=pd.read_csv(csv_file_path)
        transformed_df= transform_data(raw_df)
        transformed_df.to_sql('crypto_prices',engine,if_exists='append',index=False)
        print(f"Successfully loaded {len(transformed_df)} rows to the database")
        
        os.remove(csv_file_path)
        print("Cleared crypto_price.csv for the next batch.")
    except pd.errors.EmptyDataError:
        print("CSV file is empty.Nothing to process.")
    except Exception as e:
        print(f"Error in transform & load job :{e}")
if __name__=="__main__":
    schedule.every(5).minutes.do(etl_job)
    print("Transform-load process started. Will run every 5 minutes")
    while True:
        schedule.run_pending()
        time.sleep(1)