SELECT *
FROM dojos;
INSERT INTO dojos
(name)
VALUES
('Coding'), ('Fighting'), ('Meditatins');

SET SQL_SAFE_UPDATES = 0;

delete FROM dojos;

INSERT INTO dojos
(name)
VALUES
('Minneapolis'), ('Chicago'), ('Dallas');

INSERT INTO ninjas
(first_name, last_name, age, dojo_id)
VALUES
('Chuck', 'Norris', 25, 4),
('Steven', 'Segal', 21, 4),
('Bruce', 'Lee', 18, 4);

INSERT INTO ninjas
(first_name, last_name, age, dojo_id)
VALUES
('Rob', 'Rawl', 40, 5),
('Brandon', 'Rawl', 39, 5),
('Chloe', 'Yang', 31, 5);

INSERT INTO ninjas
(first_name, last_name, age, dojo_id)
VALUES
('Dak', 'Prescott', 26, 6),
('CeeDee', 'Lamb', 23, 6),
('Micah', 'Parsons', 22, 6);

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 4;

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 6;

SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);