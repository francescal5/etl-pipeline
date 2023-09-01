#This is our first version of building an exract-transform and load pipeline

import os
#you are importing the function called connect_to_redshift from the extract script
from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicated_data
from src.load_data_to_s3 import df_to_s3

#you need this library to read the passwords

#from dotenv import load_dotenv

#load_dotenv()

dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")


#extracting the data with some transformations
online_trans_cleaned = extract_transactional_data(dbname, host, port, user, password)
print("The shape of my data is:", online_trans_cleaned.shape)

#identify and remove the duplicates
online_trans_cleaned = identify_and_remove_duplicated_data(online_trans_cleaned)

#Loading the data to s3
s3_bucket = "july-bootcamp"
key = "etl_pipeline/docker/fqa_online_transactions_v2.pkl"

df_to_s3(online_trans_cleaned, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)
