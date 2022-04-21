select * from users;

select * from friendships;

SELECT users.id, users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name, users2.id as friend_id FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
where users.id = 8;

select * from messages where recipient_id = 7;

update 