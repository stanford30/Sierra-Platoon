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

-- SELECT AVG(credits) AS avg_credits
-- FROM classes;

SELECT students.first_name, students.last_name, enrollments.grade FROM students
JOIN enrollments ON students.id = enrollments.student_id WHERE enrollments.grade = 'A';