-- Wrtie a srcipt that creates table second_table in the database hbtn_0c_c  in your Mysql server and add muliples row.

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table ('id', 'name', 'score')
VALUES (1, 'John', 10),
        (2, 'Alex', 3),
        (3, 'Bob', 14),
        (4, 'George', 8);