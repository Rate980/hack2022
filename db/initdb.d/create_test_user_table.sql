CREATE TABLE test_user (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(128) NOT NULL,
    passwd_hash CHAR(64) NOT NULL,
    salt CHAR(4) NOT NULL,
    point INT DEFAULT 0 NOT NULL,
    PRIMARY KEY (id)
);

