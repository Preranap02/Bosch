import csv
import mysql.connector

# MySQL connection config
config = {
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'host': 'localhost',
    'database': 'your_database_name',
    'raise_on_warnings': True
}

# Path to your CSV file
csv_file_path = 'shipments.csv'

try:
    # Connect to MySQL
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Open the CSV file
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # assumes first row is header

        # Prepare the insert query (adjust columns based on your CSV/table)
        insert_query = """
        INSERT INTO Shipments 
        (origin_warehouse, destination_city, ship_date, delivery_date, product_id, quantity, freight_cost) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Loop through CSV rows and insert into table
        for row in reader:
            data = (
                int(row['origin_warehouse']),
                row['destination_city'],
                row['ship_date'],       # expects YYYY-MM-DD format in CSV
                row['delivery_date'],   # can be None or empty string, handle if needed
                int(row['product_id']),
                int(row['quantity']),
                float(row['freight_cost'])
            )
            cursor.execute(insert_query, data)

    # Commit all inserts
    conn.commit()
    print("Data inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    conn.close()
