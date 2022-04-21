select * from books;

select * from favorites;

select * from authors;

select name, books.title, favorites.book_id, favorites.author_id from authors
left join favorites on authors.id = favorites.author_id
left join books on favorites.book_id = books.id;


select * from authors 
left join favorites on authors.id = favorites.author_id 
left join books on books.id = favorites.book_id
where author_id = 4; 

SELECT * FROM books 
LEFT JOIN favorites ON books.id = favorites.book_id 
LEFT JOIN authors ON authors.id = favorites.author_id 
WHERE books.id = 1;


