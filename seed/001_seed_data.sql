USE smart_crm_mekong_mobile;

INSERT IGNORE INTO staff_users
    (staff_id, full_name, username, password_hash, role)
VALUES
    (1, 'Nhan vien tiep nhan', 'staff_demo', 'DEMO_HASH_NOT_FOR_LOGIN', 'STAFF');

INSERT IGNORE INTO issue_types
    (issue_type_id, name, description, default_sla_hours)
VALUES
    (1, 'POWER', 'Su co nguon dien', 24),
    (2, 'SOFTWARE', 'Su co phan mem', 72),
    (3, 'HARDWARE', 'Su co phan cung', 120);

INSERT IGNORE INTO priorities
    (priority_id, name, level, description)
VALUES
    (1, 'CAO', 1, 'Uu tien cao'),
    (2, 'TRUNG_BINH', 2, 'Uu tien trung binh'),
    (3, 'THAP', 3, 'Uu tien thap');

INSERT IGNORE INTO customers
    (customer_id, full_name, phone, email, address)
VALUES
    (1, 'Nguyen Van A', '0901234567', 'demo@example.com', 'Ho Chi Minh City');

INSERT IGNORE INTO devices
    (device_id, customer_id, device_type, brand, model,
     serial_number, purchase_date, warranty_end_date)
VALUES
    (1, 1, 'Smartphone', 'DemoBrand', 'Demo X1',
     'IMEI123456789', '2026-01-15', '2027-01-15');
