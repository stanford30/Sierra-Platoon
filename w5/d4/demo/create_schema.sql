DROP TABLE IF EXISTS user_accounts;
CREATE TABLE user_accounts(
  id serial PRIMARY KEY,
  username varchar NOT NULL,
  password varchar NOT NULL,
  last_login_date date
);
DROP TABLE IF EXISTS user_profiles;
CREATE TABLE user_profiles(
  id serial PRIMARY KEY,
  user_id integer,
  profile_photo_url varchar,
  about_me varchar,
  personal_quote varchar
);
DROP TABLE IF EXISTS posts;
CREATE TABLE posts(
  id serial PRIMARY KEY,
  content varchar,
  user_id integer
);
DROP TABLE IF EXISTS comments;
CREATE TABLE comments (
  id serial PRIMARY KEY,
  content varchar,
  user_id integer,
  post_id integer
);
DROP TABLE IF EXISTS reaction_types;
CREATE TABLE reaction_types (id serial PRIMARY KEY, type varchar)