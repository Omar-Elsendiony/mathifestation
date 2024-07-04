CREATE USER 'maths_dev'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON maths_dev_db.* TO 'maths_dev'@'localhost';
FLUSH PRIVILEGES;
