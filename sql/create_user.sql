CREATE USER 'maths_dev'@'localhost' IDENTIFIED BY 'maths_dev_pwd';
GRANT ALL PRIVILEGES ON maths_dev_db.* TO 'maths_dev'@'localhost';
FLUSH PRIVILEGES;
