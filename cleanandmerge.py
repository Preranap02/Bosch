import pandas as pd
from datetime import datetime

# === Load DataFrames ===
shipments = pd.read_csv("/home/zadmin/temp/shipments.csv")         # Contains: shipment_id, ship_date, delivery_date, product_id, origin_warehouse
delivery_logs = pd.read_csv("/home/zadmin/temp/delivery_logs.csv") # Contains: delivery_id, shipment_id, status, delivery_duration_days, etc.
claims = pd.read_csv("/home/zadmin/temp/claims.csv")               # Contains: claim_id, delivery_id, claim_date, resolved_date, etc.
inventory = pd.read_csv("/home/zadmin/temp/inventory (1).csv")         # Contains: warehouse_id, product_id, stock_level, reorder_threshold

# === Clean & Parse Dates ===
for df in [shipments, claims]:
    for col in ['ship_date', 'delivery_date', 'claim_date', 'resolved_date']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

# === Merge Shipments ←→ Delivery Logs ===
merged = pd.merge(delivery_logs, shipments, on='shipment_id', how='left')

# === Merge with Claims ===
merged = pd.merge(merged, claims, on='delivery_id', how='left')

# === Merge with Inventory ===
merged = pd.merge(
    merged,
    inventory,
    how='left',
    left_on=['origin_warehouse', 'product_id'],
    right_on=['warehouse_id', 'product_id']
)

# === Compute Metrics ===

# 1. Delay duration (in days)
merged['calculated_delay'] = (merged['delivery_date'] - merged['ship_date']).dt.days

# 2. Reorder flag: stock_level < reorder_threshold
merged['reorder_flag'] = merged['stock_level'] < merged['reorder_threshold']

# 3. Claim aging
today = pd.Timestamp(datetime.today().date())
merged['claim_age'] = merged.apply(
    lambda row: (row['resolved_date'] - row['claim_date']).days if pd.notnull(row['resolved_date'])
    else (today - row['claim_date']).days if pd.notnull(row['claim_date'])
    else None,
    axis=1
)

# === Optional: Clean output ===
final_cols = [
    'shipment_id', 'delivery_id', 'claim_id',
    'ship_date', 'delivery_date', 'calculated_delay',
    'stock_level', 'reorder_threshold', 'reorder_flag',
    'claim_date', 'resolved_date', 'claim_age',
    'reason', 'amount_claimed', 'claim_status'
]

result = merged[final_cols]

# === Export or View ===
result.to_csv("/home/zadmin/temp/output.csv", index=False)
print(result.head())