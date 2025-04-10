# 💵 BMO Real-Time ETL Pipeline & Dashboard (AWS + Python)

A full ETL project that extracts real-time cash flow data for **Bank of Montreal (BMO)** using public APIs, transforms it with Python, stores it in AWS Redshift, and visualizes it with a live dashboard built in Streamlit and hosted on AWS EC2.

---

## 📌 Project Overview

- 🔄 **Extract**: BMO cash flow data from Financial Modeling Prep API
- 🧹 **Transform**: Clean & format using Pandas
- 💾 **Load**: Into PostgreSQL → AWS S3 → Redshift
- 📊 **Dashboard**: Streamlit app hosted on EC2

---

## 🧱 Architecture

[Financial Modeling Prep API]
           ↓
    🐍 Python Extract Script
           ↓
      📄 Raw CSV File
           ↓
  🔍 Transform with Pandas
           ↓
      📄 Cleaned CSV File
           ↓
 PostgreSQL (local staging DB)
           ↓
          ⬇
 Upload raw & cleaned files → 🪣 AWS S3
           ↓
      COPY to Redshift Serverless
           ↓
 🔎 Streamlit Dashboard (on EC2)

![ETL Architecture](architecture.png)

---

## ⚙️ Tech Stack

- Python 3.12
- Pandas, psycopg2, boto3
- PostgreSQL (local)
- AWS S3, Redshift Serverless, EC2
- Streamlit
- Git & GitHub

---

## 🚀 How to Run This Project

```bash
git clone https://github.com/yaminichenna/bmo_real_time_etl.git
cd bmo_real_time_etl
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run ETL
python extract/fetch_bmo_cashflow.py
python transform/transform_cashflow.py
python load/load_to_postgres.py
python cloud/upload_to_s3.py

# Launch Dashboard
streamlit run dashboard/bmo_dashboard.py



