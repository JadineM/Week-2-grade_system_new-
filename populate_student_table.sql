load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\input.csv' 
into table student 
fields terminated by ',' 
lines terminated by '\n' 
IGNORE 1 lines;

SELECT * FROM student;