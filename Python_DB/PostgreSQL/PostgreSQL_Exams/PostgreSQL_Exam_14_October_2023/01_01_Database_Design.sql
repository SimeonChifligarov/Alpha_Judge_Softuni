CREATE TABLE IF NOT EXISTS towns (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS stadiums (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(45) NOT NULL,
  capacity INT NOT NULL,
  town_id INT NOT NULL,
  CONSTRAINT stadiums_capacity_chk CHECK (capacity > 0),
  CONSTRAINT stadiums_town_fk FOREIGN KEY (town_id)
    REFERENCES towns (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS teams (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(45) NOT NULL,
  established DATE NOT NULL,
  fan_base INT NOT NULL DEFAULT 0,
  stadium_id INT NOT NULL,
  CONSTRAINT teams_fan_base_chk CHECK (fan_base >= 0),
  CONSTRAINT teams_stadium_fk FOREIGN KEY (stadium_id)
    REFERENCES stadiums (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS coaches (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  first_name VARCHAR(10) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  salary NUMERIC(10,2) NOT NULL DEFAULT 0,
  coach_level INT NOT NULL DEFAULT 0,
  CONSTRAINT coaches_salary_chk CHECK (salary >= 0),
  CONSTRAINT coaches_level_chk CHECK (coach_level >= 0)
);

CREATE TABLE IF NOT EXISTS skills_data (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  dribbling INT NOT NULL DEFAULT 0,
  pace INT NOT NULL DEFAULT 0,
  "passing" INT NOT NULL DEFAULT 0,
  shooting INT NOT NULL DEFAULT 0,
  speed INT NOT NULL DEFAULT 0,
  strength INT NOT NULL DEFAULT 0,
  CONSTRAINT skills_dribbling_chk CHECK (dribbling >= 0),
  CONSTRAINT skills_pace_chk CHECK (pace >= 0),
  CONSTRAINT skills_passing_chk CHECK ("passing" >= 0),
  CONSTRAINT skills_shooting_chk CHECK (shooting >= 0),
  CONSTRAINT skills_speed_chk CHECK (speed >= 0),
  CONSTRAINT skills_strength_chk CHECK (strength >= 0)
);

CREATE TABLE IF NOT EXISTS players (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  first_name VARCHAR(10) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  age INT NOT NULL DEFAULT 0,
  "position" CHAR(1) NOT NULL,
  salary NUMERIC(10,2) NOT NULL DEFAULT 0,
  hire_date TIMESTAMP,
  skills_data_id INT NOT NULL,
  team_id INT,
  CONSTRAINT players_age_chk CHECK (age >= 0),
  CONSTRAINT players_salary_chk CHECK (salary >= 0),
  CONSTRAINT players_skills_fk FOREIGN KEY (skills_data_id)
    REFERENCES skills_data (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT players_team_fk FOREIGN KEY (team_id)
    REFERENCES teams (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS players_coaches (
  player_id INT NOT NULL,
  coach_id INT NOT NULL,
  CONSTRAINT players_coaches_pk PRIMARY KEY (player_id, coach_id),
  CONSTRAINT players_coaches_player_fk FOREIGN KEY (player_id)
    REFERENCES players (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT players_coaches_coach_fk FOREIGN KEY (coach_id)
    REFERENCES coaches (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);
