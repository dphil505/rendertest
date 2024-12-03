from navigation import make_sidebar
import streamlit as st
import pandas as pd
from io import StringIO
make_sidebar()



import boto3
from dotenv import load_dotenv
import os

load_dotenv()
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
def upload_to_s3(df, bucket_name, file_name):
    # Convert DataFrame to CSV in memory
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name='us-west-1',
    )
    # Upload the CSV to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=csv_buffer.getvalue()
    )
    return f"s3://{bucket_name}/{file_name}"
# Configure session directly in code
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name="us-west-1"
)

s3 = session.resource('s3')
bucket_name = "ceegreentest"

obj = s3.Object(bucket_name, 'cgtest.csv')
response = obj.get()
# Read content to a DataFrame
df_from_s3 = pd.read_csv(StringIO(response['Body'].read().decode('utf-8')))
df_from_s3


edited_df = st.data_editor(df_from_s3, use_container_width=True)
# Button to download the edited DataFrame
if st.button("Save to S3"):
    file_name = "edited_dataframe.csv"
    try:
        s3_path = upload_to_s3(edited_df, bucket_name, file_name)
        st.success(f"File successfully uploaded to {s3_path}")
    except Exception as e:
        st.error(f"Error uploading file to S3: {e}")