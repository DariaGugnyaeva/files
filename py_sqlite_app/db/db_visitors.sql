CREATE TABLE IF NOT EXISTS visitors (
    id INTEGER PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    patr_name VARCHAR(20),
    num_reader_card INTEGER NOT NULL,
    address VARCHAR(20)
);
