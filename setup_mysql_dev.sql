-- script that prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creating user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'Godwin242?';

-- OR
-- CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'Godwin242?';

-- granting user privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant select privilege
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
