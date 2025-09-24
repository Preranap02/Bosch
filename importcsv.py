import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv('home/zadmin/temp/shipments.csv')

# Replace with your MySQL credentials
username = 'root'
password = 'Pass@123'
host = 'localhost'  # or your server IP
port = 3306  # default MySQL port
database = 'Local instance 3306'

# Create engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Insert data into 'shipments' table
try:
    df.to_sql('shipments', con=engine, if_exists='append', index=False)
    print("Data inserted successfully!")
except Exception as e:
    print("Error:", e)