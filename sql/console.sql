-- SQL console is the fastest and easiest way to explore and query your databases
SELECT id
FROM users;

SELECT *
FROM orders;

-- Will load everything from all those tables 
SELECT * 
FROM orders o
LEFT JOIN users u on u.id = o.user_id; 

SELECT o.name, u.name
FROM orders o 

SELECT COUNT(*) AS total_count 
FROM orders; 
