CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, UPDATE, DELETE ON database_name.* TO 'username'@'localhost';
REVOKE SELECT, INSERT, UPDATE, DELETE ON database_name.* FROM 'username'@'localhost';
DROP USER 'username'@'localhost';
