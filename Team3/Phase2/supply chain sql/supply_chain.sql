CREATE DATABASE IF NOT EXISTS supply_chain;
USE supply_chain;

CREATE TABLE IF NOT EXISTS shipments (
    shipment_id VARCHAR(20) PRIMARY KEY,
    origin_warehouse VARCHAR(20) NOT NULL,
    destination_city VARCHAR(100) NOT NULL,
    ship_date DATE NOT NULL,
    delivery_date DATE NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    freight_cost DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS vendors (
    vendor_id VARCHAR(20) PRIMARY KEY,
    vendor_name VARCHAR(100) NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    contract_start DATE NOT NULL,
    contract_end DATE NOT NULL,
    vendor_rating DECIMAL(3,1) NOT NULL,
    country VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS inventory (
    warehouse_id VARCHAR(15) NOT NULL,
    product_id VARCHAR(15) NOT NULL,
    stock_level INT NOT NULL,
    reorder_threshold INT NOT NULL,
    last_restock_date DATE,
    next_restock_due DATE
);

CREATE TABLE IF NOT EXISTS delivery_logs (
    delivery_id VARCHAR(50) NOT NULL PRIMARY KEY,
    shipment_id VARCHAR(50) NOT NULL,
    carrier VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL ,
    delivery_duration_days INT,
    damage_flag TINYINT,
    proof_of_delivery_status VARCHAR(50),
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);



CREATE TABLE IF NOT EXISTS claims (
    claim_id VARCHAR(20) PRIMARY KEY,
    delivery_id VARCHAR(20) NOT NULL,
    reason TEXT NOT NULL,
    amount_claimed DECIMAL(10,2) NOT NULL,
    claim_status VARCHAR(50) DEFAULT 'PENDING',
    claim_date DATE NOT NULL,
    resolved_date DATE,
    FOREIGN KEY (delivery_id) REFERENCES delivery_logs(delivery_id) ON DELETE CASCADE
);
show tables;
