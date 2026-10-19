CREATE DATABASE User;

USE User;

CREATE TABLE customer(Custid int , custname VARCHAR(15) , City VARCHAR(10), product VARCHAR(15), Price INT);

desc customer;

ALTER TABLE customer Add CONSTRAINT PRIMARY KEY(Custid);
INSERT INTO customer VALUES(1, "John", "Pune", "Keyboard", 1500);
INSERT INTO customer VALUES(2, "Carl", "JSR", "Mouse", 1200);
INSERT INTO customer VALUES(3, "George", "Nashik", "Mobile", 25000);

SELECT custname , product from customer;

CREATE TABLE CustClone as SELECT * FROM customer;
SELECT * FROM CustClone;

DROP TABLE CustClone;

SELECT custname , product from customer WHERE Custid = 3;

SELECT custname , product, Price from customer WHERE Price < 1500;

SELECT * from customer WHERE Price < 1500;

SELECT custname , product from customer WHERE Custid =1;

SELECT * from customer WHERE City = "Nashik";


SELECT * from customer ORDER BY Price;

SELECT * from customer ORDER BY Price DESC;

SELECT * from customer ORDER BY Custid DESC;

SELECT * from customer ORDER BY City DESC , Price ASC;

SELECT UPPER(custname) , LOWER(product) from customer WHERE Custid < 3;

ALTER TABLE customer ADD COLUMN LastName VARCHAR(30);

UPDATE customer set LastName = "Deo" WHERE custid = 1;
UPDATE customer set LastName = "Bush" WHERE custid = 2;
UPDATE customer set LastName = "Johnson" WHERE custid = 3;


SELECT CONCAT(custname , " ",lastname)  as FullName FROM customer;

SELECT SUBSTR(custname ,1, 3)   FROM customer;

SELECT INSTR(custname ,"o") as position FROM customer;


