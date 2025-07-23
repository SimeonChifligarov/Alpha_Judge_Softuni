CREATE TABLE mountains (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) -- NOT NULL UNIQUE
);

CREATE TABLE peaks (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50), -- NOT NULL,
    mountain_id INTEGER, -- NOT NULL,
    CONSTRAINT fk_peaks_mountains
        FOREIGN KEY (mountain_id)
        REFERENCES mountains(id)
        -- ON DELETE CASCADE
        -- ON UPDATE CASCADE
);

-- CREATE INDEX idx_peaks_mountain_id ON peaks(mountain_id);
