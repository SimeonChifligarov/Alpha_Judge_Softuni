CREATE TABLE mountains(
    id SERIAL PRIMARY KEY,
    name varchar(50)
);

CREATE TABLE peaks(
    id SERIAL PRIMARY KEY,
    name varchar(50),
    mountain_id int,
    CONSTRAINT fk_peaks_mountains FOREIGN KEY (mountain_id) REFERENCES mountains(id)
);
