CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    date DATE
);

CREATE TABLE IF NOT EXISTS photos (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255),
    place VARCHAR(100),
    customer_id INT REFERENCES customers(id)
);

INSERT INTO customers (name, date)
VALUES
    ('Bella', '2022-03-25'),
    ('Philip', '2022-07-05');

INSERT INTO photos (url, place, customer_id)
VALUES
    ('bella_1111.com', 'National Theatre', 1),
    ('bella_1112.com', 'Largo', 1),
    ('bella_1113.com', 'The View Restaurant', 1),
    ('philip_1121.com', 'Old Town', 2),
    ('philip_1122.com', 'Rowing Canal', 2),
    ('philip_1123.com', 'Roman Theater', 2);
