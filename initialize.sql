CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    age INT
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    message TEXT NOT NULL,
    likes INT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, email, age) VALUES
(1, 'alice99', 'alice99@example.com', 22),
(2, 'bob_the_builder', 'bob.builder@example.com', 34),
(3, 'carla_j', 'carla.j@example.com', 28),
(4, 'dave_h', 'dave.h@example.com', 41),
(5, 'elena_r', 'elena.r@example.com', 19),
(6, 'frank_o', 'frank.o@example.com', 37),
(7, 'grace_k', 'grace.k@example.com', 25),
(8, 'henry_m', 'henry.m@example.com', 30),
(9, 'isla_p', 'isla.p@example.com', 23),
(10, 'jack_w', 'jack.w@example.com', 45);

INSERT INTO posts (post_id, user_id, message, likes, created_at) VALUES
(1, 1, 'Just getting started here!', 5, '2024-01-06 10:00:00'),
(2, 1, 'Went hiking up the trail near the lake.', 12, '2024-01-08 15:30:00'),
(3, 2, 'Building a birdhouse this weekend.', 8, '2024-01-11 09:00:00'),
(4, 2, 'My favorite tools for small builds.', 3, '2024-01-15 18:20:00'),
(5, 3, 'Homemade pasta is easier than you think.', 20, '2024-01-13 12:00:00'),
(6, 4, 'Notes from my database class this week.', 7, '2024-02-02 20:15:00'),
(7, 5, 'How I edit my landscape photos.', 15, '2024-02-16 08:50:00'),
(8, 6, 'Ran 15 miles this weekend, feeling great.', 10, '2024-02-22 07:30:00'),
(9, 7, 'Finally finished Dune, thoughts inside.', 6, '2024-03-02 21:00:00'),
(10, 8, 'Configuring my new dev environment.', 4, '2024-03-06 11:15:00'),
(11, 9, 'Tomatoes are finally coming in the garden.', 9, '2024-03-19 14:40:00'),
(12, 10, 'Sourdough starter progress report.', 11, '2024-04-03 09:25:00');
