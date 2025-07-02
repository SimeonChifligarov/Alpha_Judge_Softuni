CREATE TABLE minions_birthdays (
    id              SERIAL PRIMARY KEY,
    name            VARCHAR(50)     NOT NULL DEFAULT '',
    date_of_birth   DATE            NOT NULL,
    age             INTEGER         NOT NULL DEFAULT 0,
    present         VARCHAR(100)    NOT NULL DEFAULT '',
    party           TIMESTAMPTZ     NOT NULL
);
