INSERT INTO authors
(first_name, last_name)
VALUES
('Jane', 'Austen'),
('Emily', 'Dickinson'),
('Fyodor', 'Dostoevsky'),
('William', 'Shakespeare'),
('Lau', 'Tzu');
SELECT *
FROM authors;
INSERT INTO books
(title)
VALUES
('C Sharp'), ('Java'),('Python'),('PHP'),('RUBY');
UPDATE books_schema.authors SET
first_name = 'Bill'
WHERE id = 4;

INSERT INTO favorites
(author_id,book_id)
VALUES
(1,1),(1,2),
(2,1),(2,2),(2,3),
(3,1),(3,2),(3,3),(3,4),
(4,1),(4,2),(4,3),(4,4),(4,5);

SELECT *
FROM books
JOIN favorites on books.id = favorites.book_id
JOIN authors on authors.id = favorites.author_id
WHERE books.id =3;

DELETE FROM favorites
WHERE book_id =3
AND author_id = 2;

INSERT INTO favorites
(author_id, book_id)
VALUES
(5,2);

SELECT *
FROM authors
JOIN favorites ON authors.id = favorites.author_id
JOIN books ON books.id = favorites.book_id
WHERE authors.id = 3;

SELECT *
FROM books
JOIN favorites ON books.id = favorites.book_id
JOIN authors ON authors.id = favorites.author_id
WHERE books.id = 5;



