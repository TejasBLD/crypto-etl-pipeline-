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

1.Clone the repository:
```bash
git clone https://github.com/TejasBLD/crypto-etl-pipeline-.git
cd crypto-etl-pipeline-
```
2.Install dependencies:
```bash
pip install -r requirements.txt
```
3.Create and configure .env:
```bash
cp .env.example .env
```
4.Update the .env file with your own database credentials.

5.Usage

Run the ETL pipeline:
```bash
python load.py
```
Fetches, transforms, and loads the data into your PostgreSQL database.
Check the table crypto_prices to verify the data.
