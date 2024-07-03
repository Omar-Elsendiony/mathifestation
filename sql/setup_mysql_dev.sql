-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS maths_dev_db;
CREATE USER IF NOT EXISTS 'maths_dev'@'localhost' IDENTIFIED BY 'maths_dev_pwd';
GRANT ALL PRIVILEGES ON `maths_dev_db`.* TO 'maths_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'maths_dev'@'localhost';
FLUSH PRIVILEGES;
