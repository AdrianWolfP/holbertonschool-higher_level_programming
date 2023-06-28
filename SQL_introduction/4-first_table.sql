-- sql script that creates a table called first_table in the current database in your MySQL
-- description: first_table with, id INT, name VARCHAR(256)
CREATE table if NOT EXISTS first_table (
    id INT,
    name VARCHAR(150)
);