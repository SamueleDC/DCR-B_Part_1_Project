DROP SCHEMA IF exists search_facility;
CREATE SCHEMA search_facility;
use search_facility;
DROP TABLE IF EXISTS S_FILES;
CREATE TABLE  S_FILES (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FULL_PATH_NAME VARCHAR(255),
    FILE_NAME VARCHAR(255),
    FILE_TYPE CHAR(30),
    CONTENT LONGTEXT,
    DEPTH INT,
    SIZE INT
);
