SHOW DATABASES;
CREATE DATABASE College;
USE College;
CREATE TABLE Employee(EmpID INT, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10));
DESC Employee;
INSERT INTO Employee VALUES (1, "r0ny" , "Wane", 20 , "East");
SELECT * FROM Employee;

INSERT INTO Employee VALUES (2, "John" , "Deo", 24 , "West"),
                            (3, "John" , "Wick", 19 , "North"),
                            (4, "Sam" , "Altman", 26 , "South"),
                            (5, "Sam" , null, 26 , null);

INSERT INTO Employee (EmpID , FirstName , LastName) VALUES (6, null , "Wane");
SELECT * FROM Employee;
UPDATE Employee SET LastName = "Crook" WHERE EmpID = 5;
UPDATE Employee SET EmpZone = "East" WHERE EmpID = 5;
UPDATE Employee SET EmpZone = "South" WHERE EmpID = 6;
UPDATE Employee SET EmpAge = 27,  FirstName = "Bruce" WHERE EmpID = 6;

UPDATE Employee
SET EmpAge = 29, FirstName = 'John'
WHERE EmpID IN (4, 6);

DELETE FROM Employee WHERE EmpID = 6;

TRUNCATE TABLE Employee;
DROP TABLE Employee;


DROP DATABASE CompanyDB;
CREATE DATABASE CompanyDB;
use CompanyDB;
CREATE TABLE Employee(EmpID INT NOT NULL, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10));
INSERT INTO Employee VALUES ( 1 , "Jim", "Morman", 40 , "East");
CREATE TABLE Employee1(EmpID INT NOT NULL UNIQUE, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10));
ALTER TABLE Employee1 ADD CONSTRAINT PRIMARY KEY(EmpID);
INSERT INTO Employee1 VALUES ( 2 , "Jim", "Carrie", 40 , "East");
SELECT * FROM Employee1;
CREATE TABLE Employee2(EmpID INT NOT NULL UNIQUE, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10) , CHECK(EmpAge>22));
SELECT * FROM Employee2;
INSERT INTO Employee2 VALUES ( 1 , "Jim", "Carrie", 19 , "East");
INSERT INTO Employee2 VALUES ( 1 , "Jim", "Carrie", 23 , "East");
ALTER TABLE Employee2 ADD COLUMN EmpSalary INT CHECK(EmpSalary > 5000);
INSERT INTO Employee2 VALUES ( 1 , "Jim", "Carrie", 23 , "East", 4000);
INSERT INTO Employee2 VALUES ( 2 , "Jim", "Carrie", 23 , "East", 5100);
CREATE TABLE Employee3(EmpID INT NOT NULL UNIQUE, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , Empzone varchar(10) );
ALTER TABLE Employee3 ADD COLUMN EmpSalary INT;
ALTER TABLE Employee3 ADD CONSTRAINT chk_EmpAge_Salary CHECK(EmpAge >22 and EmpSalary > 5000);
INSERT INTO Employee3 VALUES ( 1 , "Jim", "Carrie", 20 , "East", 5000);
INSERT INTO Employee3 VALUES ( 1 , "Jim", "Carrie", 24 , "East", 5200);
ALTER TABLE Employee3 DROP CHECK chk_EmpAge_Salary;
SHOW  CREATE TABLE  Employee;
CREATE TABLE Employee4(EmpID INT NOT NULL UNIQUE, FirstName VARCHAR(10) , LastName VARCHAR(10), EmpAge int , EmpDept varchar(10) Default "Operations" );
INSERT INTO Employee4 ( EmpID, FirstName , LastName, EmpAge ) VALUES ( 2 , "Jim", "Carrie", 23 );
SELECT * FROM Employee4;












