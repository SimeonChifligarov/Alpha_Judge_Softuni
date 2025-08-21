CREATE TABLE IF NOT EXISTS countries (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS customers (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  first_name VARCHAR(25) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  gender CHAR(1) CHECK (gender IN ('M','F')),
  age INT NOT NULL CHECK (age > 0),
  phone_number CHAR(10) NOT NULL,
  country_id INT NOT NULL,
  CONSTRAINT customers_country_fk FOREIGN KEY (country_id)
    REFERENCES countries (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS products (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(25) NOT NULL,
  description VARCHAR(250),
  recipe TEXT,
  price NUMERIC(10,2) NOT NULL CHECK (price > 0)
);

CREATE TABLE IF NOT EXISTS feedbacks (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  description VARCHAR(255),
  rate NUMERIC(4,2) CHECK (rate >= 0 AND rate <= 10),
  product_id INT NOT NULL,
  customer_id INT NOT NULL,
  CONSTRAINT feedbacks_product_fk FOREIGN KEY (product_id)
    REFERENCES products (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT feedbacks_customer_fk FOREIGN KEY (customer_id)
    REFERENCES customers (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS distributors (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(25) NOT NULL UNIQUE,
  address VARCHAR(30) NOT NULL,
  summary VARCHAR(200) NOT NULL,
  country_id INT NOT NULL,
  CONSTRAINT distributors_country_fk FOREIGN KEY (country_id)
    REFERENCES countries (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ingredients (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  description VARCHAR(200),
  country_id INT NOT NULL,
  distributor_id INT NOT NULL,
  CONSTRAINT ingredients_country_fk FOREIGN KEY (country_id)
    REFERENCES countries (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT ingredients_distributor_fk FOREIGN KEY (distributor_id)
    REFERENCES distributors (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS products_ingredients (
  product_id INT NOT NULL,
  ingredient_id INT NOT NULL,
  CONSTRAINT products_ingredients_pk PRIMARY KEY (product_id, ingredient_id),
  CONSTRAINT products_ingredients_product_fk FOREIGN KEY (product_id)
    REFERENCES products (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT products_ingredients_ingredient_fk FOREIGN KEY (ingredient_id)
    REFERENCES ingredients (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);
