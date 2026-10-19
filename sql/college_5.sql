CREATE DATABASE CompanyDB;
USE CompanyDB;
SHOW DATABASES;

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Salary DECIMAL(10,2),
    JoinDate DATE
);
DESCRIBE Employees;

CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);
DESCRIBE Departments;

ALTER TABLE Employees ADD Email VARCHAR(100);
DESCRIBE Employees;

ALTER TABLE Departments ADD dept_location VARCHAR(100);
DESCRIBE Departments;

ALTER TABLE Employees ADD Phone VARCHAR(15);
ALTER TABLE Employees MODIFY Phone VARCHAR(15) NOT NULL;
DESCRIBE Employees;

ALTER TABLE Employees MODIFY EmpName VARCHAR(100);
DESCRIBE Employees;

ALTER TABLE Departments DROP PRIMARY KEY;
DESCRIBE Departments;

ALTER TABLE Departments ADD PRIMARY KEY (DeptID);
ALTER TABLE Employees ADD DeptID INT;
ALTER TABLE Employees
    ADD CONSTRAINT fk_emp_dept FOREIGN KEY (DeptID) REFERENCES Departments(DeptID);
SHOW CREATE TABLE Employees;

ALTER TABLE Employees RENAME COLUMN EmpName TO EmployeeName;
DESCRIBE Employees;

ALTER TABLE Employees ADD Age INT;
ALTER TABLE Employees ADD CONSTRAINT chk_age CHECK (Age >= 18);
ALTER TABLE Employees ADD CONSTRAINT chk_salary CHECK (Salary > 0);
SHOW CREATE TABLE Employees;

ALTER TABLE Employees DROP COLUMN Phone;
DESCRIBE Employees;

RENAME TABLE Employees TO EmployeeDetails;
SHOW TABLES;

ALTER TABLE EmployeeDetails DROP CHECK chk_age;
ALTER TABLE EmployeeDetails DROP CHECK chk_salary;
SHOW CREATE TABLE EmployeeDetails;

ALTER TABLE EmployeeDetails DROP FOREIGN KEY fk_emp_dept;
DROP TABLE Departments;
SHOW TABLES;

DROP DATABASE CompanyDB;
SHOW DATABASES;