-- SELECT * FROM STUDENTS
-- WHERE birthdate<'1986-01-01'
-- AND LOWER(first_name) LIKE '%t%';

-- SELECT AVG(EXTRACT(year FROM age('2022-11-01', birthdate))) as avg_age FROM students;
-- SELECT * FROM addresses;

-- SELECT * FROM addresses WHERE city LIKE '% %';
-- 

-- SELECT students.first_name, students.last_name, 
-- addresses.line_1, addresses.city, addresses.state 
-- FROM students
-- INNER JOIN addresses ON students.address_id = addresses.id
-- WHERE addresses.city LIKE '% %';

-- SELECT * FROM classes;
