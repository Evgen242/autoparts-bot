CREATE TABLE IF NOT EXISTS auto_parts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    car_brand VARCHAR(100) NOT NULL,
    car_model VARCHAR(100) NOT NULL,
    part_number VARCHAR(100),
    quantity INTEGER DEFAULT 0,
    price DECIMAL(10,2),
    location VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
