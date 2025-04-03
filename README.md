# 💵 BMO Real-Time ETL Pipeline & Dashboard (AWS + Python)

This project demonstrates a full-stack **ETL pipeline** using real-time financial data for **Bank of Montreal (BMO)**. It extracts, transforms, loads, and visualizes **cash flow statements** using modern data engineering tools and services.

> 🔥 Built for interviews, portfolio, and production-like hands-on learning.

---

## 🧱 Project Architecture

```plaintext
[Financial Modeling Prep API] 
         ↓
   Python Extract Script
         ↓
      CSV Files
         ↓
[Transform with Pandas]
         ↓
Cleaned Data → PostgreSQL → S3 → Redshift
                                ↓
                          Streamlit Dashboard (Hosted on EC2)


---

## ⚙️ Tech Stack

- **Python 3.12**
- **PostgreSQL** (staging DB)
- **AWS S3** (cloud storage)
- **Amazon Redshift Serverless** (data warehouse)
- **Streamlit** (dashboarding)
- **AWS EC2** (dashboard hosting)
- **Git & GitHub** (version control)

---

## 📈 Features

- ✅ Real-time cash flow data ingestion from BMO via public API
- ✅ Data cleaning with Python & Pandas
- ✅ Data loaded into PostgreSQL and Redshift
- ✅ Files uploaded to AWS S3 (raw & cleaned)
- ✅ Dashboard hosted on EC2 using Streamlit
- ✅ Redshift Serverless integration with IAM + S3 access
- ✅ Secure architecture using VPC and security groups

---

## 🗃️ Folder Structure

bmo_real_time_etl/
│
├── extract/              # Extracts data from API
│   └── fetch_bmo_cashflow.py
│
├── transform/            # Cleans and formats raw data
│   └── transform_cashflow.py
│
├── load/                 # Loads into PostgreSQL
│   └── load_to_postgres.py
│
├── cloud/                # Uploads to S3
│   └── upload_to_s3.py
│
├── dashboard/            # Streamlit UI
│   └── bmo_dashboard.py
│
├── README.md
└── requirements.txt

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/yaminichenna/bmo_real_time_etl.git
cd bmo_real_time_etl
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python extract/fetch_bmo_cashflow.py
python transform/transform_cashflow.py
streamlit run dashboard/bmo_dashboard.py

🌍 Hosted Version
This dashboard is deployed on an AWS EC2 instance:

📍 http://<your-ec2-public-ip>:8501

🔒 Security
IAM roles with limited S3/Redshift access

Redshift secured via VPC & inbound rules

EC2 firewall configured to expose only required ports

✨ What I Learned
Building a real-time ETL pipeline with cloud tools

Hosting dashboards and connecting to cloud databases

Working with IAM, S3, Redshift, PostgreSQL, and EC2

Writing clean, modular, and reusable Python code

📌 Future Enhancements
 Add Airflow for scheduling & orchestration

 Add Docker support for full containerization

 Add more KPIs and visualizations

 Add anomaly detection or alerting

📫 Contact
Yamini Chenna
🌐 https://github.com/yaminichenna
