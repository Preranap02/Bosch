import pandas as pd
import mysql.connector
import math

csv_file = "/home/zadmin/temp/output.csv"
table_name = "Cleaned_and_Merged_Shipment_Delivery_Claims_Data"

columns = [
    "shipment_id",
    "delivery_id",
    "claim_id",
    "ship_date",
    "delivery_date",
    "calculated_delay",
    "stock_level",
    "reorder_threshold",
    "reorder_flag",
    "claim_date",
    "resolved_date",
    "claim_age",  # <-- comma added here
    "reason",
    "amount_claimed",
    "claim_status"
]

def nan_to_none(value):
    if isinstance(value, float) and math.isnan(value):
        return None
    return value

df = pd.read_csv(csv_file)

conn = mysql.connector.connect(
    host="localhost",
    user="root",        # Fill in your MySQL username
    password="Pass@123",    # Fill in your MySQL password
    database="bosch"     # Fill in your database name
)
cursor = conn.cursor()

sql = f"""
INSERT INTO {table_name} ({', '.join(columns)})
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    reason = VALUES(reason),
    amount_claimed = VALUES(amount_claimed),
    claim_status = VALUES(claim_status),
    claim_date = VALUES(claim_date),
    resolved_date = VALUES(resolved_date)
"""

for _, row in df.iterrows():
    try:
        data = (
            nan_to_none(row["shipment_id"]),
            nan_to_none(row["delivery_id"]),
            nan_to_none(row["claim_id"]),
            nan_to_none(row["ship_date"]),
            nan_to_none(row["delivery_date"]),
            nan_to_none(row["calculated_delay"]),
            nan_to_none(row["stock_level"]),
            nan_to_none(row["reorder_threshold"]),
            bool(row["reorder_flag"]),
            nan_to_none(row["claim_date"]),
            nan_to_none(row["resolved_date"]),
            nan_to_none(row["claim_age"]),
            nan_to_none(row["reason"]),
            float(row["amount_claimed"]) if not pd.isna(row["amount_claimed"]) else None,
            nan_to_none(row["claim_status"])
        )
        cursor.execute(sql, data)
    except mysql.connector.Error as err:
         print(f" Error inserting row ")

conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted successfully!")