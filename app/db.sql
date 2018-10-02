CREATE DATABASE IF NOT EXISTS fitnessdb;

-- User
CREATE TABLE IF NOT EXISTS fitnessdb.user (
  id BIGINT,
  first_name CHAR(25) NOT NULL,
  last_name CHAR(25),
  username CHAR(25) NOT NULL,
  password CHAR(25) NOT NULL,
  UNIQUE KEY(username),
  PRIMARY KEY(id)
);

-- Exercise
CREATE TABLE IF NOT EXISTS fitnessdb.exercise (
  id BIGINT,
  name CHAR(25) NOT NULL,
  PRIMARY KEY(id)
);

-- Workout History
CREATE TABLE IF NOT EXISTS fitnessdb.workout_history (
  user_id BIGINT NOT NULL,
  exercise_id BIGINT NOT NULL,
  utc_datetime DATETIME NOT NULL,
  weight FLOAT,
  reps INT,
  duration TIME,
  FOREIGN KEY(user_id)
    REFERENCES user(id),
  FOREIGN KEY(exercise_id)
    REFERENCES exercise(id),
  PRIMARY KEY(user_id, exercise_id, utc_datetime)
);
