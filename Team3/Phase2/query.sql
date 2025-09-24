use supply_chain;
show tables;
select * from inventory;
select * from delivery_logs;
select * from shipments;
select * from vendors;

SELECT s.shipment_id, s.origin_warehouse, s.destination_city, d.status AS delivery_status, c.claim_id, c.claim_status, c.amount_claimed FROM shipments s LEFT JOIN delivery_logs d ON s.shipment_id = d.shipment_id LEFT JOIN claims c ON d.delivery_id = c.delivery_id;

SELECT destination_city, SUM(freight_cost) AS total_freight_cost FROM shipments GROUP BY destination_city ORDER BY total_freight_cost DESC;
SELECT claim_status, AVG(amount_claimed) AS avg_claim_amount FROM claims GROUP BY claim_status;
SELECT d.carrier, COUNT(s.shipment_id) AS total_shipments, AVG(d.delivery_duration_days) AS avg_duration, SUM(c.amount_claimed) AS total_claims FROM shipments s JOIN delivery_logs d ON s.shipment_id = d.shipment_id LEFT JOIN claims c ON d.delivery_id = c.delivery_id GROUP BY d.carrier;
SELECT v.vendor_name, v.country, COUNT(s.shipment_id) AS shipments_supplied, AVG(v.vendor_rating) AS avg_rating, SUM(c.amount_claimed) AS total_claims FROM vendors v JOIN shipments s ON v.product_id = s.product_id LEFT JOIN delivery_logs d ON s.shipment_id = d.shipment_id LEFT JOIN claims c ON d.delivery_id = c.delivery_id GROUP BY v.vendor_name, v.country;
CREATE VIEW StockHealth AS SELECT i.warehouse_id, i.product_id, i.stock_level, i.reorder_threshold, CASE WHEN i.stock_level <= i.reorder_threshold THEN 'Reorder Needed' ELSE 'Healthy' END AS stock_status FROM inventory i;

CREATE VIEW UnresolvedClaims AS SELECT c.claim_id, c.delivery_id, c.reason, c.amount_claimed, c.claim_date, DATEDIFF(CURDATE(), c.claim_date) AS claim_age_days FROM claims c WHERE c.claim_status != 'Resolved'; 
select * from UnresolvedClaims;