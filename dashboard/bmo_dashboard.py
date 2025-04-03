import streamlit as st
import pandas as pd
import psycopg2

# 🔐 Redshift connection settings
REDSHIFT_HOST = "bmo-etl-wg.715841364680.us-east-1.redshift-serverless.amazonaws.com"
REDSHIFT_PORT = "5439"
REDSHIFT_DB = "dev"
REDSHIFT_USER = "admin"
REDSHIFT_PASSWORD = "Mastan19"

# 🚀 Connect to Redshift
def get_data():
    conn = psycopg2.connect(
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT,
        dbname=REDSHIFT_DB,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD
    )
    query = "SELECT * FROM bmo_cashflow ORDER BY date DESC;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# 🖥️ Streamlit UI
st.set_page_config(page_title="BMO Cash Flow Dashboard", layout="wide")
st.title("💵 BMO Cash Flow Dashboard")

# 📊 Load data
df = get_data()

# 📋 Show summary stats
st.subheader("📈 Key Financial Metrics")
latest = df.iloc[0]

col1, col2, col3 = st.columns(3)
col1.metric("Net Income", f"${latest['net_income']:,}")
col2.metric("Free Cash Flow", f"${latest['free_cashflow']:,}")
col3.metric("Dividends Paid", f"${latest['dividends_paid']:,}")

# 📉 Chart: Free Cash Flow over time
st.subheader("📉 Free Cash Flow Over Time")
df["date"] = pd.to_datetime(df["date"])
df_chart = df[["date", "free_cashflow"]].sort_values("date")
st.line_chart(df_chart.set_index("date"))

# 📄 Show full table
st.subheader("📋 Full Cash Flow Table")
st.dataframe(df)
