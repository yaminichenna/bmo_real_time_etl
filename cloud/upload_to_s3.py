import boto3
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = "bmo-etl-project-yamini"

# ✅ S3 folder structure
RAW_FOLDER = "raw/"
CLEANED_FOLDER = "processed/"

# ✅ Connect to AWS S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

print("📡 Connected to AWS S3")

# ✅ Upload raw files
raw_files = list(Path("extract").glob("*.csv"))
if not raw_files:
    print("⚠️ No raw .csv files found in 'extract/' folder.")
else:
    for file in raw_files:
        s3.upload_file(str(file), BUCKET_NAME, RAW_FOLDER + file.name)
        print(f"✅ Uploaded raw file: {file.name}")

# ✅ Upload cleaned files
cleaned_files = list(Path("transform").glob("*.csv"))
if not cleaned_files:
    print("⚠️ No cleaned .csv files found in 'transform/' folder.")
else:
    for file in cleaned_files:
        s3.upload_file(str(file), BUCKET_NAME, CLEANED_FOLDER + file.name)
        print(f"✅ Uploaded cleaned file: {file.name}")



