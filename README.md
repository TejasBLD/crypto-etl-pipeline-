# Crypto ETL Pipeline

A simple Python ETL (Extract, Transform, Load) pipeline that fetches cryptocurrency data from the CoinGecko API, transforms it, and loads it into a PostgreSQL database.

---

## Features

- Fetches live cryptocurrency data for selected coins (e.g., Bitcoin, Ethereum).  
- Transforms data to keep only relevant columns: `id`, `symbol`, `current_price`, `market_cap`, `last_updated`.  
- Loads data into a PostgreSQL table (`crypto_prices`).  
- Uses `.env` for database credentials (example provided as `.env.example`).  

---

## Dependencies

Install the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
