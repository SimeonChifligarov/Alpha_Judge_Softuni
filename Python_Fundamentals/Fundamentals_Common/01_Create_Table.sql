CREATE TABLE IF NOT EXISTS students (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade DOUBLE,
    CONSTRAINT pk_students PRIMARY KEY (id)
);
