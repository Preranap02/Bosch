CREATE TABLE Shipments (
    shipment_id VARCHAR(50) PRIMARY KEY,
    origin_warehouse VARCHAR(255),
    destination_city VARCHAR(255) ,
    ship_date DATE,
    delivery_date DATE,
    product_id VARCHAR(255) NOT NULL,
    quantity INT,
    freight_cost DECIMAL(10,2)
);
CREATE TABLE Inventory (
    warehouse_id VARCHAR(255) ,
    product_id VARCHAR(255) ,
    stock_level INT ,
    reorder_threshold INT ,
    last_restock_date DATE,
    next_restock_due DATE
);
CREATE TABLE Vendors (
    vendor_id VARCHAR(255) PRIMARY KEY,
    vendor_name VARCHAR(255),
    product_id VARCHAR(255),
    contract_start DATE,
    contract_end DATE,
    vendor_rating DECIMAL(3,2),
    country VARCHAR(100)
);
CREATE TABLE Delivery_Logs (
    delivery_id VARCHAR(255) PRIMARY KEY,
    shipment_id VARCHAR(255),
    carrier VARCHAR(255),
    status VARCHAR(50),
    delivery_duration_days INT,
    damage_flag BOOLEAN,
    proof_of_delivery_status VARCHAR(50),
    CONSTRAINT fk_shipment FOREIGN KEY (shipment_id) REFERENCES Shipments(shipment_id)
);
CREATE TABLE Claims (
    claim_id VARCHAR(255) PRIMARY KEY,
    delivery_id VARCHAR(255) ,
    reason VARCHAR(255),
    amount_claimed DECIMAL(10,2),
    claim_status VARCHAR(50),
    claim_date DATE,
    resolved_date DATE,
    CONSTRAINT fk_delivery FOREIGN KEY (delivery_id) REFERENCES Delivery_Logs(delivery_id)
);
