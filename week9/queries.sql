1.CREATE TABLE Languages(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   language VARCHAR(30),
   answer VARCHAR(50),
   answered INTEGER,
   guide VARCHAR(150))


2.INSERT INTO Languages (language, answer, answered, guide)
     VALUES
	('Python', 'google', 0, 'A folder named Python was created. Go there and fight with program.py'),
	('Go', '200 OK', 0, 'A folder named Go was created. Go there and try to make Google Go run.'),
	('Java', 'object oriented programming', 0, 'A folder named Java was created. Can you handle the class?'),
	('Haskell', 'Lambda', 0, 'Something pure has landed. Go to Haskell folder and see it!'),
	('C#', 'NDI=', 0, 'Do you see sharp? Go to the C# folder and check out.'),
	('Ruby', 'https://www.ruby-lang.org/bg/', 0, 'Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!'),
	('C++', 'header files', 0, 'Here be dragons! It''s C++ time. Go to the C++ folder.'),
	('JavasSript', 'Douglas Crockford', 0, 'NodeJS time. Go to JavaScript folder and Node your way!')


3.UPDATE languages
	SET language = 'JavaScript'
    WHERE id = 8


4.ALTER TABLE Languages
    ADD rating INTEGER
        CHECK (rating => 1 AND rating <= 9)


5.UPDATE Languages
   SET rating = CASE language
                      WHEN 'Python' THEN  9
                      WHEN 'Go' THEN 8
                      WHEN 'Java' THEN 2
                      WHEN 'Haskell' THEN 5
                      WHEN 'C#' THEN 2
                      WHEN 'Ruby' THEN 7
                      WHEN 'C++' THEN 3
                      WHEN 'JavaScript' THEN 9
                      END
   WHERE Language IN('Python', 'Go', 'Java', 'Haskell', 'C#', 'Ruby', 'C++', 'JavaScript');


6.UPDATE Languages
   SET answered = CASE language
                      WHEN 'Python' THEN  1
                      WHEN 'Go' THEN 1
                      END
   WHERE Language IN('Python', 'Go');


7.SELECT *
	FROM Languages
	WHERE answer = '200 OK' or answer = 'Lambda';