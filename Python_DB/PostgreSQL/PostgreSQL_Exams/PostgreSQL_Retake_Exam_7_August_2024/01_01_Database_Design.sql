CREATE TABLE IF NOT EXISTS countries (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(40) NOT NULL UNIQUE,
  continent VARCHAR(40) NOT NULL,
  currency VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS categories (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS actors (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  birthdate DATE NOT NULL,
  height INT,
  awards INT NOT NULL DEFAULT 0,
  country_id INT NOT NULL,
  CONSTRAINT actors_awards_chk CHECK (awards >= 0),
  CONSTRAINT actors_country_fk FOREIGN KEY (country_id)
    REFERENCES countries (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS productions_info (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  rating NUMERIC(4,2) NOT NULL,
  duration INT NOT NULL,
  budget NUMERIC(10,2),
  release_date DATE NOT NULL,
  has_subtitles BOOLEAN NOT NULL DEFAULT FALSE,
  synopsis TEXT,
  CONSTRAINT productions_info_duration_chk CHECK (duration > 0)
);

CREATE TABLE IF NOT EXISTS productions (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  title VARCHAR(70) NOT NULL UNIQUE,
  country_id INT NOT NULL,
  production_info_id INT NOT NULL UNIQUE,
  CONSTRAINT productions_country_fk FOREIGN KEY (country_id)
    REFERENCES countries (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT productions_info_fk FOREIGN KEY (production_info_id)
    REFERENCES productions_info (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS productions_actors (
  production_id INT NOT NULL,
  actor_id INT NOT NULL,
  CONSTRAINT productions_actors_pk PRIMARY KEY (production_id, actor_id),
  CONSTRAINT productions_actors_production_fk FOREIGN KEY (production_id)
    REFERENCES productions (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT productions_actors_actor_fk FOREIGN KEY (actor_id)
    REFERENCES actors (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS categories_productions (
  category_id INT NOT NULL,
  production_id INT NOT NULL,
  CONSTRAINT categories_productions_pk PRIMARY KEY (category_id, production_id),
  CONSTRAINT categories_productions_category_fk FOREIGN KEY (category_id)
    REFERENCES categories (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT categories_productions_production_fk FOREIGN KEY (production_id)
    REFERENCES productions (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);
