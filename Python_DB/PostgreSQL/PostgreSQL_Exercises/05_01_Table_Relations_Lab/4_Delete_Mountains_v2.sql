CREATE TABLE mountains(
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(50)
);

CREATE TABLE peaks(
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(50),
    mountain_id int,
    CONSTRAINT fk_mountain_id
        FOREIGN KEY (mountain_id)
            REFERENCES mountains(id)
                ON DELETE CASCADE
);
