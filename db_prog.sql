-- CREATE TABLE organiser (
-- 	org_id SERIAL,
-- 	org_name VARCHAR(100) NOT NULL,
-- 	PRIMARY KEY (org_id)
-- )

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
-- 	prj_flight pro_choice NOT NULL,
-- 	prj_house pro_choice NOT NULL,
-- 	prj_food pro_choice NOT NULL,
-- 	prj_bus pro_choice NOT NULL,
-- 	org_id INTEGER NOT NULL,
-- 	PRIMARY KEY (prj_id),
-- 	FOREIGN KEY (org_id) REFERENCES organiser (org_id)
-- )


-- -- SELECT * FROM project

-- CREATE TABLE volunteer(
-- 	vol_id SERIAL,
-- 	vol_fname VARCHAR (100) NOT NULL,
-- 	vol_lname VARCHAR (100) NOT NULL,
-- 	vol_country VARCHAR (100) NOT NULL,
-- 	vol_city VARCHAR (100) NOT NULL,
-- 	vol_date_start DATE NOT NULL,
-- 	vol_date_end DATE NOT NULL,
-- 	vol_job VARCHAR (30),
-- 	vol_skill VARCHAR (30),
-- 	vol_phone VARCHAR (15) NOT NULL,
-- 	vol_mail VARCHAR (50) NOT NULL,
-- 	vol_flight vtl_choice NOT NULL,
-- 	vol_house vtl_choice NOT NULL,
-- 	vol_food vtl_choice NOT NULL,
-- 	vol_bus vtl_choice NOT NULL,
-- 	prj_id INTEGER NOT NULL,
-- 	PRIMARY KEY (vol_id),
-- 	FOREIGN KEY (prj_id) REFERENCES project (prj_id)
-- )

-- ALTER TABLE volunteer  
-- DROP COLUMN prj_id;
SELECT * FROM volunteer







