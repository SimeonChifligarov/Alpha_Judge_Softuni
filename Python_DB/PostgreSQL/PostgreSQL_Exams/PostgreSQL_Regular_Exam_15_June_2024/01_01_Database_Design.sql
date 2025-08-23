CREATE TABLE IF NOT EXISTS accounts (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  username VARCHAR(30) NOT NULL UNIQUE,
  password VARCHAR(30) NOT NULL,
  email VARCHAR(50) NOT NULL,
  gender CHAR(1) NOT NULL,
  age INT NOT NULL,
  job_title VARCHAR(40) NOT NULL,
  ip VARCHAR(30) NOT NULL,
  CONSTRAINT accounts_gender_chk CHECK (gender IN ('M','F'))
);

CREATE TABLE IF NOT EXISTS addresses (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  street VARCHAR(30) NOT NULL,
  town VARCHAR(30) NOT NULL,
  country VARCHAR(30) NOT NULL,
  account_id INT NOT NULL,
  CONSTRAINT addresses_account_fk FOREIGN KEY (account_id)
    REFERENCES accounts (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS photos (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  description TEXT,
  capture_date TIMESTAMP NOT NULL,
  views INT NOT NULL DEFAULT 0,
  CONSTRAINT photos_views_chk CHECK (views >= 0)
);

CREATE TABLE IF NOT EXISTS comments (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  content VARCHAR(255) NOT NULL,
  published_on TIMESTAMP NOT NULL,
  photo_id INT NOT NULL,
  CONSTRAINT comments_photo_fk FOREIGN KEY (photo_id)
    REFERENCES photos (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS accounts_photos (
  account_id INT NOT NULL,
  photo_id INT NOT NULL,
  CONSTRAINT accounts_photos_pk PRIMARY KEY (account_id, photo_id),
  CONSTRAINT accounts_photos_account_fk FOREIGN KEY (account_id)
    REFERENCES accounts (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT accounts_photos_photo_fk FOREIGN KEY (photo_id)
    REFERENCES photos (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS likes (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  photo_id INT NOT NULL,
  account_id INT NOT NULL,
  CONSTRAINT likes_photo_fk FOREIGN KEY (photo_id)
    REFERENCES photos (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT likes_account_fk FOREIGN KEY (account_id)
    REFERENCES accounts (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);
