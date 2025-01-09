use collegedatabase;

DELIMITER //

CREATE TRIGGER before_user_insert
BEFORE INSERT ON `user`
FOR EACH ROW
BEGIN
    -- Check if the username already exists
    IF EXISTS (SELECT 1 FROM `user` WHERE username = NEW.username) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Duplicate username. Please choose a different username.';
    END IF;
END;
//

DELIMITER ;

INSERT INTO `user` (`username`, `email`, `password`, `PERMISSION`)
VALUES ('new_username', 'new_email@example.com', 'password123', 1);
INSERT INTO `user` (`username`, `email`, `password`, `PERMISSION`)
VALUES ('new_username', 'new_email@example.com', 'password123', 1);

DELIMITER //

CREATE TRIGGER before_update_password
BEFORE UPDATE ON user
FOR EACH ROW
BEGIN
    -- Check if the password is being updated
    IF NEW.password <> OLD.password THEN
        -- Update the create_time timestamp to the current time
        SET NEW.create_time = CURRENT_TIMESTAMP;
    END IF;
END;
//

DELIMITER //

CREATE TRIGGER before_update_email
BEFORE UPDATE ON user
FOR EACH ROW
BEGIN
    -- Check if the email is being updated
    IF NEW.email <> OLD.email THEN
        -- Update the create_time timestamp to the current time
        SET NEW.create_time = CURRENT_TIMESTAMP;
    END IF;
END;
//

DELIMITER ;


DELIMITER ;
