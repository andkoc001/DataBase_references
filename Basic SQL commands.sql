/* comment */
#######
-- MySQL Workbench
#######
## -- To import database in MySQL Workbench: From Database in the menu select "Connect to Database..." (make sure proper user name is used)
## -- To import a database from a SQL file: From Server in the manu select "Import Data"

#######
-- Terminal
#######

## -- To start MySQL from terminal
  mysql - u < user_name > - p < password > # add (import) a database from a .sql file (no semicolon at end?)
  SOURCE file.sql eg.SOURCE / home / ak / Desktop / _Moje_linux / _nauka / GMIT / 031_2020 - 01_Applied_Databases / 02 / school.sql #######

## -- To start
  MySQL
  and import a database mysql - u < user_name > - p < password > < file.sql #######
  SQL Query Commands #######

## -- shows available databases
  SHOW databases;

## -- activate a database
  USE school;

## -- deselects (de-use) the current working database
  DROP database school;

## -- show what table are in the database
  SHOW tables;

## -- look at a table schema (structure)
  describe < table_name >;

## -- to show all details, you can specify each column names or use '*'
SELECT * FROM subject;

## -- conditional selection of data, example:
SELECT Name FROM subject WHERE OnLeavingCert = 1;

## -- list unique values in a column
SELECT DISTINCT <column_name> FROM <table_name>;

## -- list data which contains certain string of characters
SELECT Name FROM subject WHERE Teacher LIKE 'Mr.%' #-- list data which does not contains certain string of characters

SELECT Name FROM subject WHERE Teacher NOT LIKE "Mr%";

## -- use the NOT LIKE operator to find records that do not match the pattern you specify.
SELECT name FROM people WHERE name NOT LIKE 'A%';

## -- lists names that do not start with 'A'
## -- list data from a column containing date excluding month January or February
SELECT * FROM <column_name> WHERE month(< name_of_column_of_date >) != 1
  AND month(< name_of_column_of_date >) != 2;

## -- listing in a specific order(s) - if more than one thern by priority
SELECT * FROM <column_name>
ORDER BY month(<name_of_column_of_date>), year(<name_of_column_of_date>);

## -- limit listing to a specific number of rows
SELECT * FROM <column_name> LIMIT 4;

## -- limit listing to a specific number of rows, begining from a specific row(exclusive)
SELECT * FROM <column_name> LIMIT 4, 2;

## -- list 2 rows starting from row 5
## -- limit data from a range (WHERE IN)
SELECT * FROM <column_name> WHERE age IN (24, 25, 26);

#####
-- Queries from multiple tables
#####

## -- table.column
## -- uwaga! trzeba podac relacje miedzy tabelami
SELECT klienci.imie, klienci.nazwiski, zamowienia.status
FROM zamowienia, klienci
WHERE
  klienci.idklienta = zamowienia.idklienta

##-- z aliasami
SELECT k.imie, k.nazwiski, z.status
FROM zamowienia AS z, klienci AS w
WHERE
  k.idklienta = w.idkli;

## -- tabela nie musi nazywac sie tak samo
## -- przyklad zlozony
SELECT klienci.imie, klienci.nazwisko
FROM klienci, zamowienia
WHERE
  zamowienia.idksiazki = 2 AND zamowienia.idklienta = klient.idklienta; # --Jakie ksiazki (tutul i autor) zamowila osoba Jan Nowak (idklienta = 2)?

SELECT ksiazki.tytul, ksiazki.autor, klienci.idklienta
FROM ksiazki, zamowienia
WHERE
  klienci.idklienta = 2 AND zamowienia.idksiazki = ksiazki.idksiazki;
  
#####
-- JOIN
#####

SELECT e.emp_no, first_name, last_name FROM employees e INNER JOIN salaries s ON e.emp_no = s.emp_no WHERE s.salary BETWEEN 30000 AND 40000;

SELECT e.emp_no, first_name, last_name FROM employees e WHERE e.emp_no IN (SELECT s.emp_no FROM salaries s WHERE s.salary BETWEEN 30000 AND 40000);

SELECT e.emp_no, first_name, last_name FROM employees e LEFT JOIN salaries s ON e.emp_no = s.emp_no;

SELECT e.emp_no, first_name, last_name FROM employees e RIGHT JOIN salaries s ON e.emp_no = s.emp_no;

-- You can check for NULL values using the expression IS NULL. For example, to count the number of missing birth dates in the people table:
SELECT COUNT(*) FROM people WHERE birthdate IS NULL;

## -- To filter out missing values so you only get results which are not NULL, you can use the IS NOT NULL operator.
SELECT name FROM people WHERE birthdate IS NOT NULL;

#######
-- Database manipulation
#######

## -- Look into a table structure
SHOW CREATE table driver \G

## -- to create a new table
  CREATE TABLE < new_table_name > (
    name VARCHAR(20) NOT NULL,
    dob DATE,
    sex ENUM('M', 'F') DEFAULT 'M',
    PRIMARY KEY(personID)
  );

#####
## -- INSERT ## -- to update record
#####

UPDATE klienci SET nazwisko = "Kowalski" WHERE idklienta = 4;

UPDATE klienci SET nazwisko = "Kowalski" WHERE nazwiski = "Nowak";

## -- dla wszystkich Nowakow!
UPDATE ksiazki SET cena = ROUND(cena * 1.1, 2);

## -- zwiekszenie ceny o 10%
UPDATE ksiazki SET cena = cena -10 ORDER BY cena DESC LIMIT = 1;

## -- obniz cene najd;rozszej ksiazki
UPDATE klienci SET imie = "Joanna", nazwiski = "Dostojewska" WHERE idklienta = 5;

#####
## -- INSERT ## -- to add a new record
#####

## -- dla wszystkie atrybutøw (kolumn) w domyslnej kolejnosci, ale nie trzba tych z auto_increment -> wtedy NULL
INSERT INTO kliencu VALUES (NULL, "Franciszek", "Janowski", "Warszawa");

## -- w innej kolejnosci
INSERT INTO zamowienia (idksiazki, status, idklienta, idksiaki) VALUE (NULL, "oczekiwanie", 6, 4);

## -- dwa rekordy w jednym poleceniu
INSERT INTO klienci 
VALUES
  (NULL, "John", "Doe", "Los Angeles"),
  (NULL, "John", "Smith", "Los Angeles") # -- z uzyciem SET

INSERT INTO klienci SET idklienta = NULL, imie = "Steve", nazwisko "McQuinn", adress = "San Francisco"
  
#####
## -- DELETE ## -- to delete a record from a single table (not related to any other table
#####

DELETE FROM <table> #-- deletes entire table -> the table will become an empty set (schema remains intact)
DELETE FROM <table> WHERE <condition> #-- deletes if condition is met

DELETE FROM person WHERE personID = 6;

DELETE FROM person WHERE sex = "M" AND isStudent AND age > 20;

## -- to delete a record from a related table (two or more tables linked by FOREIGN KEY)
## -- behavior to be set during the schema definintion
## -- ON DELETE RESTRICT    # default (does not need to be specified), prevents from deleting if there is a link to another table
## -- ON DELETE CASCADE     # delete also record from other linked tables
## -- ON DELETE SET NULL    # records from other linked tables are set to null

#######
## -- Functions
#######

###### -- String functions, more: https://dev.mysql.com/doc/refman/8.0/en/string-functions.html

UPPER() # -- Returns an uppercase version of a string
SELECT   UPPER(name) from SUBJECT;
  
STRCMP() # -- Compares two strings and returns: 0 if str1=str2; -1 if str1<str2; 1 if str1>str2
SELECT STRCMP("MySQL", "Database"); #--> 1

ASCII() # Returns the ASCII value of the first character in a string
SELECT ASCII("M") #--> 77

REPLACE(string, from_string, to_string) #-- Replaces all occurrences of a substring within a string, with a new substring: A) string – The original string B) from_string – The substring to be replaced, C) to_string – The new replacement string
SELECT tid, REPLACE(name, "Ms", "Mrs") FROM teacher;

SUBSTR(string, start, length) #-- Extract a substring from a string: A) string – The string to extract from, B) start – The start position within the string, C) length – The number of characters to be extracted
SELECT tid, SUBSTR(name, 1, 3) FROM teacher;

## -- Numeric functions, more: https://dev.mysql.com/doc/refman/8.0/en/numeric-functions.html
  ROUND(number, decimals) #-- Rounds a number to a specified number of decimal places
SELECT ROUND(engingeSize, 1) FROM car;

## -- Date funtioncs, more: https://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html
  DATEDIFF(date1, date2) #-- Returns the number of days between 2 dates
SELECT DATEFIF("2001-01-01", "2000-01-01");

DATE_FORMAT(date, format) #-- Formats a date
SELECT DATE_FORMAT(dob, "%y-%m-%d") FROM teacher
WHERE tid = 5

## -- Aggregate Functions  An aggregate function performs a calculation on a set of values and returns a single value.

AVG()
SELECT AVG(experience) FROM teacher;

MIN() MAX()
SELECT COUNT(*) FROM teacher WHERE level = "l";

## -- number of rows
SELECT COUNT(subject) FROM teacher;

## -- number of non-missing values in given column
SELECT MAX(budget) AS max_budget, MAX(duration) AS max_duration FROM films;

## -- this would generate a new table with results and columns names as per aliases
SELECT title, (gross_profit - budget) AS net_profit FROM films;


GROUP BY() #-- The GROUP BY statement is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.
SELECT level, AVG(experience) FROM teacher GROUP BY level;

SELECT model, ROUND(AVE(milage)) AS "km" FROM car WHERE milage > 50000 GROUP BY model HAVING milage > 200000;

## -- The HAVING clause applies a filter condition to each group ofrows. The WHERE clause applies the filter condition to each individual row.

## -- number of unique values (non-missing) in a column
SELECT COUNT(DISTINCT birthdate) FROM people;

## -- MySQL Information Functions
  DATABASE() USER()
  
#######
##--MySQL Control Flow Functions
#######

## -- IF(condition, value_if_true, value_if_false); <condition> - Value to Test, value_if_true – Value to return if condition is True value_if_false – Value to return if condition is False

SELECT IF (1 > 2, Yes, No) #--> No

SELECT *, IF(experience >= 20 AND experience <= 45, "Y", "") AS "Payrise Due" FROM teacher;

## -- CASE WHEN condition 1 THEN result 1 WHEN condition 2 THEN result 2 WHEN condition n THEN result n ELSE result END

SELECT name, dob
CASE
  WHERE MONTH(dob) IN (2, 3, 4) THEN "Spring" ELSE ""
  END AS Season
FROM person;

#######
##-- MySQL Stored Routines
#######

## -- create a new function
CREATE FUNCTION add2Nums(num1 integer, num2 integer) RETURNS integer
DETERMINISTIC
BEGIN
RETURN num1 + num2
END;

SELCT add2Nums(2, 5);

CREATE FUNCTION discount(age INT(11)) RETURNS VARCHAR(3)
DETERMINISTIC
BEGIN
  IF age < 15 THEN RETURN "0%";
  ELSEIF age < 30 THEN RETURN "10%";
  ELSEIF age < 50 THEN RETURN "20%";
  ELSE RETURN "30%";
  END IF;
END

SELECT discount(67);


SELECT name, age, discount(age) "Discount" FROM person;

#######
## --  MySQL Stored Procedures # (procedure > function)
#######

##-- FUNCTIONS Return a single value Only SELECT. Can ’ t use Stored Procedures Does not support Transactions

##-- PROCEDURES Return 0 or more values SELECT, INSERT, UPDATE, DELETE Can use Stored Functions Supports Transactions

CREATE PROCEDURE make_milage(mk VARCHAR(20), ml int(11)
DETERMINISTIC
BEGIN
  SELECT * FROM car
  WHERE
  make LIKE mk AND milage < ml ORDER BY milage;
END;

CALL make_milage("Ford", 40000);

CALL make_milage("%", 20000);

## -- Listing all functions and procedures in the database
SELECT routine_name, routine_type FROM information_schema.routines
  WHERE routine_name IN ("add2Nums", "discount", "make_milage");

## -- What is in a Function or Procedure (script viewing)
  SHOW CREATE FUNCTION add2Nums;

## -- Delete a Function or Procedure
  DROP FUNCTION add2Nums;

