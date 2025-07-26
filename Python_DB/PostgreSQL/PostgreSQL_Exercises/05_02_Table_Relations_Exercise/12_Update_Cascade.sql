ALTER TABLE countries_rivers DROP CONSTRAINT IF EXISTS countries_rivers_country_id_fkey;
ALTER TABLE countries_rivers DROP CONSTRAINT IF EXISTS countries_rivers_river_id_fkey;

ALTER TABLE countries_rivers
ADD CONSTRAINT fk_countries_rivers_countries
FOREIGN KEY (country_code)
REFERENCES countries(country_code)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE countries_rivers
ADD CONSTRAINT fk_countries_rivers_rivers
FOREIGN KEY (river_id)
REFERENCES rivers(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
