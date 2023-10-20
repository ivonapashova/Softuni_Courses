CREATE TABLE mountains (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE peaks (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    mountain_id integer 
	CONSTRAINT fk_mountain_id
	REFERENCES mountains(id) ON DELETE CASCADE
);
