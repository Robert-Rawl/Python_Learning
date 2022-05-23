INSERT INTO
users (first_name, last_name)
VALUES
('Rob','Rawl'), ('Brandon','Rawl'), ('Chloe','Yang'), ('Natalie', 'Dehn'),('Jason', 'Rusedorf'),('Cheslyn','Dilbek');
SELECT *
FROM users;
INSERT INTO friendships
(user_id,friend_id)
VALUES
(1,2),(1,4),(1,6),
(2,1),(2,3),(2,5),
(3,2),(3,5),
(4,3),
(5,1),(5,6),
(6,2),(6,3);

SELECT users.first_name, users.last_name,
users2.first_name AS friend_first_name, users2.last_name AS friend_last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS users2 ON users2.id = friendships.friend_id;

SELECT users2.first_name AS first_name, users2.last_name AS last_name, users.first_name AS friends_with
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS users2 ON users2.id = friendships.friend_id
WHERE users.id = 1;

SELECT COUNT(*) AS numm_of_friendships 
FROM friendships;

SELECT user_id, users.first_name, users.last_name, count(user_id) AS num_of_friends
FROM friendships
JOIN users ON users.id = friendships.user_id
GROUP BY user_id
ORDER BY num_of_friends DESC
LIMIT 1;

SELECT users2.first_name AS first_name, users2.last_name AS last_name, users.first_name AS friends_with
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS users2 on users2.id = friendships.friend_id
WHERE users.id = 3
ORDER BY first_name;