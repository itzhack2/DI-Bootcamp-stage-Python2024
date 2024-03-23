-- );
-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');
-- SELECT * FROM FirstTab
-- (I did`t know that )

-- CREATE TABLE SecondTab (
--     id integer 
-- );
-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL);
-- -- SELECT * FROM SecondTab
-- my guess(5,NULL)

--SELECT COUNT(*) 
--FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- (I did`t know that )

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- -- (my-guess is 0 beacus we cant comper somthig with null

--  SELECT COUNT(*) 
--  FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- ('i did`t guess noting')