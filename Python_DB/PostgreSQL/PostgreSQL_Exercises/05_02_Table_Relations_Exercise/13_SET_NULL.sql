CREATE TABLE IF NOT EXISTS customers (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS contacts (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    contact_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    customer_id INT,
    FOREIGN KEY (customer_id)
        REFERENCES customers(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

INSERT INTO customers (customer_name)
VALUES
    ('BlueBird Inc'),
    ('Dolphin LLC');

INSERT INTO contacts (contact_name, phone, email, customer_id)
VALUES
    ('John Doe', '(408)-111-1234', 'john.doe@bluebird.dev', 1),
    ('Jane Doe', '(408)-111-1235', 'jane.doe@bluebird.dev', 1),
    ('David Wright', '(408)-222-1234', 'david.wright@dolphin.dev', 2);

DELETE FROM customers WHERE id = 1;
