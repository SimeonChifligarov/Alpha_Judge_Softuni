CREATE TABLE IF NOT EXISTS gift_recipients (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  country_id INT NOT NULL,
  gift_sent BOOLEAN NOT NULL DEFAULT FALSE,
  CONSTRAINT gift_recipients_country_fk FOREIGN KEY (country_id)
    REFERENCES countries (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

INSERT INTO gift_recipients (name, country_id, gift_sent)
SELECT
  CONCAT_WS(' ', first_name, last_name),
  country_id,
  country_id IN (7, 8, 14, 17, 26)
FROM customers;
