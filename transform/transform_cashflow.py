import pandas as pd
from datetime import datetime
import os

RAW_FILE = r"C:\Users\yams2\PycharmProjects\bmo_real_time_etl\extract\BMO_cashflow_20250329_013501.csv"
CLEANED_FILE = f"transform/BMO_cashflow_cleaned_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Make sure the 'transform' directory exists
os.makedirs("transform", exist_ok=True)

# Load the raw CSV
df = pd.read_csv(RAW_FILE)

# Columns to keep
columns_to_keep = [
    "date",
    "netIncome",
    "depreciationAndAmortization",
    "operatingCashFlow",
    "capitalExpenditure",
    "freeCashFlow",
    "stockRepurchase",
    "dividendsPaid",
    "fetched_at"
]

existing_columns = [col for col in columns_to_keep if col in df.columns]
df_cleaned = df[existing_columns]

# Save the cleaned file
df_cleaned.to_csv(CLEANED_FILE, index=False)
print(f"✅ Cleaned data saved to: {CLEANED_FILE}")
print("📄 Columns in raw file:")
print(df.columns.tolist())
