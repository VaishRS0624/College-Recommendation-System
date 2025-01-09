
delimiter //
CREATE PROCEDURE CreateAndInsertDynamicTable(IN tableName VARCHAR(255), IN sourceTableName VARCHAR(255))
BEGIN
    -- Create the dynamic table
    SET @createQuery = CONCAT('CREATE TABLE ', tableName, ' AS SELECT CHOICECODE,INSTITUTE_CODE FROM ', sourceTableName);
    PREPARE createStmt FROM @createQuery;
    EXECUTE createStmt;
    DEALLOCATE PREPARE createStmt;
END //