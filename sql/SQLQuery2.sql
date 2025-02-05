USE BikeStores;

CREATE TABLE production.trainer (
	id INT IDENTITY(1, 1) PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	char_id INT NOT NULL,
	FOREIGN KEY (char_id)
		REFERENCES production.characters(id)
		ON DELETE CASCADE ON UPDATE CASCADE
);