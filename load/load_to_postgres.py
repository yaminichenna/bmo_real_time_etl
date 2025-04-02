import pandas as pd
import psycopg2

# Update this path with your actual cleaned file
CSV_FILE = r"C:\Users\yams2\PycharmProjects\bmo_real_time_etl\transform\transform\BMO_cashflow_cleaned_20250329_023105.csv"

# Load cleaned CSV
df = pd.read_csv(CSV_FILE)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="bmo_etl",
    user="postgres",
    password="Mastan@16",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Insert each row into the table
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO bmo_cashflow (
            date,
            net_income,
            depreciation,
            operating_cashflow,
            capital_expenditure,
            free_cashflow,
            dividends_paid,
            fetched_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row.get("date"),
        row.get("netIncome"),
        row.get("depreciationAndAmortization"),
        row.get("operatingCashFlow"),
        row.get("capitalExpenditure"),
        row.get("freeCashFlow"),
        row.get("dividendsPaid"),
        row.get("fetched_at")
    ))

conn.commit()
cur.close()
conn.close()

print("✅ Data loaded successfully into PostgreSQL!")
