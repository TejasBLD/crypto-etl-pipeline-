# Crypto ETL Pipeline

A simple Python ETL (Extract, Transform, Load) pipeline that fetches cryptocurrency data from the CoinGecko API, transforms it, and loads it into a PostgreSQL database.

---

## Features

- Fetches live cryptocurrency data for selected coins (e.g., Bitcoin, Ethereum).  
- Transforms data to keep only relevant columns: `id`, `symbol`, `current_price`, `market_cap`, `last_updated`.  
- Loads data into a PostgreSQL table (`crypto_prices`).  
- Uses `.env` for database credentials (example provided as `.env.example`).  

---

## Installation

1. Clone the repository:
git clone https://github.com/TejasBLD/crypto-etl-pipeline-.git
cd crypto-etl-pipeline-
2. Install dependencies:
pip install -r requirements.txt
3.Create a .env file (copy .env.example):
cp .env.example .env
4.Update your database credentials in .env.
