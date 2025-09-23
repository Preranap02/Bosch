import pandas as pd
import mysql.connector

csv_file = "/home/zadmin/temp/claims.csv"
table_name = "Claims"

columns = [
    "claim_id",
    "delivery_id",
    "reason",
    "amount_claimed",
    "claim_status",
    "claim_date",
    "resolved_date"
]


df = pd.read_csv(csv_file)


conn = mysql.connector.connect(
    host="localhost",
    user="",        
    password= " ",   
    database=  "" 
)
cursor = conn.cursor()


sql = f"""
INSERT INTO {table_name} ({', '.join(columns)})
VALUES (%s, %s, %s, %s, %s, %s, %s)
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
            row["claim_id"],
            row["delivery_id"],
            row["reason"],
            float(row["amount_claimed"]),
            row["claim_status"],
            row["claim_date"],
            row["resolved_date"]
        )
        cursor.execute(sql, data)
    except mysql.connector.Error as err:
        print(f"❌ Error inserting row for claim '{row['claim_id']}' and product '{row['delivery_id']}': {err}")


conn.commit()
cursor.close()
conn.close()

print(" Data inserted successfully!")

