-- CREATE TABLE organiser (
-- 	org_id SERIAL,
-- 	org_fname VARCHAR(100) NOT NULL,
-- 	org_lname VARCHAR (100) NOT NULL,
-- 	PRIMARY KEY (org_id)
-- )

-- CREATE TYPE prj_choice AS ENUM ('yes','no');

-- CREATE TABLE project (
-- 	prj_id SERIAL,
-- 	prj_name VARCHAR (20) NOT NULL,
-- 	prj_description TEXT NOT NULL,
-- 	prj_country VARCHAR (20) NOT NULL,
-- 	prj_city VARCHAR (20) NOT NULL,
-- 	prj_date_start DATE NOT NULL,
-- 	prj_date_end DATE NOT NULL,
-- 	prj_skills VARCHAR (200),
-- 	prj_job VARCHAR (30),
-- 	prj_flight prj_choice NOT NULL,
-- 	prj_house prj_choice NOT NULL,
-- 	prj_food prj_choice NOT NULL,
-- 	prj_bus prj_choice NOT NULL,
-- 	org_id INTEGER NOT NULL,
-- 	PRIMARY KEY (prj_id),
-- 	FOREIGN KEY (org_id) REFERENCES organiser (org_id)
-- )

-- CREATE TYPE vol_choice AS ENUM ('yes','no','i dont care');

-- SELECT * FROM project

-- CREATE TABLE volunteer(
-- 	vol_id SERIAL,
-- 	vol_fname VARCHAR (100) NOT NULL,
-- 	vol_lname VARCHAR (100) NOT NULL,
-- 	vol_job VARCHAR (30),
-- 	vol_skill VARCHAR (30),
-- 	vol_phone VARCHAR (15) NOT NULL,
-- 	vol_mail VARCHAR (50) NOT NULL,
-- 	vol_flight vol_choice NOT NULL,
-- 	vol_house vol_choice NOT NULL,
-- 	vol_food vol_choice NOT NULL,
-- 	vol_bus vol_choice NOT NULL,
-- 	prj_id INTEGER NOT NULL,
-- 	PRIMARY KEY (vol_id),
-- 	FOREIGN KEY (prj_id) REFERENCES project (prj_id)
-- )

-- SELECT * FROM volunteer







