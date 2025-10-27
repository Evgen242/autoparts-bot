CREATE TABLE IF NOT EXISTS autoparts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    car_brand VARCHAR(50),
    car_model VARCHAR(50),
    part_number VARCHAR(50),
    quantity INTEGER DEFAULT 0,
    price FLOAT,
    location VARCHAR(100),
    description VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
