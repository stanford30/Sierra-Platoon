DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
  id serial PRIMARY KEY,
  first_name varchar(255) NOT NULL,
  last_name varchar(255) NOT NULL,
  birthdate date NOT NULL,
  address_id integer,
  CONSTRAINT FK_addresses_students FOREIGN KEY(address_id) REFERENCES addresses(id)
);
DROP TABLE IF EXISTS addresses CASCADE;
CREATE TABLE addresses (
  id serial PRIMARY KEY,
  line_1 varchar(255) NOT NULL,
  city varchar(255) NOT NULL,
  state varchar(255) NOT NULL,
  zipcode varchar
);
DROP TABLE IF EXISTS classes CASCADE;
CREATE TABLE classes (
  id serial PRIMARY KEY,
  name varchar(255) NOT NULL,
  credits integer NOT NULL
);
DROP TABLE IF EXISTS enrollments CASCADE;
CREATE TABLE enrollments (
  id serial PRIMARY KEY,
  student_id integer,
  class_id integer,
  grade varchar,
  CONSTRAINT FK_enrollments_classes FOREIGN KEY(class_id) REFERENCES classes(id),
  CONSTRAINT FK_enrollments_students FOREIGN KEY(student_id) REFERENCES students(id)
);