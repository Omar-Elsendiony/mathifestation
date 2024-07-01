-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS MATHS_test_db;
CREATE USER IF NOT EXISTS 'MATHS_test'@'localhost' IDENTIFIED BY 'MATHS_test_pwd';
GRANT ALL PRIVILEGES ON `MATHS_test_db`.* TO 'MATHS_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'MATHS_test'@'localhost';
FLUSH PRIVILEGES;
