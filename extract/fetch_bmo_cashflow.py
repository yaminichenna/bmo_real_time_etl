import requests
import pandas as pd
from datetime import datetime

# 🔐 Replace with your real API key
API_KEY = "VqgAtfq8fXBukPUe75LglS131kmX4GDh"
TICKER = "BMO"
LIMIT = 5  # How many years of data

url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{TICKER}?limit={LIMIT}&apikey={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df["fetched_at"] = datetime.now()

    # Save to CSV
    filename = f"{TICKER}_cashflow_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Cash flow data saved to {filename}")
else:
    print(f"❌ Failed to fetch data: {response.status_code} - {response.text}")
