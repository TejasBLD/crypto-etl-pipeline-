from sqlalchemy import create_engine
from transform import transform_data
from extract import fetching_data
from dotenv import load_dotenv
import os

load_dotenv()  

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def load_data(df):

    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    df.to_sql('crypto_prices',engine,if_exists='append',index=False)
    print("Data loaded successfully !")
    
if __name__=="__main__":
    raw_df = fetching_data()
    df=transform_data(raw_df)
    load_data(df)