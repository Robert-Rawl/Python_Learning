
SELECT * FROM authors;
INSERT INTO authors( name, created_at, updated_at)
VALUES("Johnny Rocket", NOW(), NOW());
SELECT * FROM authors;
UPDATE books_schema.authors SET
name = 'Velvet Bear'
WHERE id = 2;
DELETE FROM authors
WHERE id =3;
