SELECT * FROM posts 
JOIN users ON posts.user_id = users.user_id 
WHERE posts.likes > 8;
