
CREATE DATABASE CompanyDB;
USE CompanyDB;


CREATE TABLE Employees (
  EmpID INT PRIMARY KEY,
  EmpName VARCHAR(50),
  Salary INT,
  JoinDate DATE
);


CREATE TABLE Departments (
  DeptID INT PRIMARY KEY,
  DeptName VARCHAR(50)
);


ALTER TABLE Employees ADD COLUMN Email VARCHAR(100);


ALTER TABLE Departments ADD COLUMN dept_location VARCHAR(50);


ALTER TABLE Employees ADD COLUMN Phone INT(10);

ALTER TABLE Employees MODIFY COLUMN Phone INT(10) NOT NULL;

ALTER TABLE Employees MODIFY COLUMN EmpName VARCHAR(100);


ALTER TABLE Employees ADD COLUMN DeptID INT;

ALTER TABLE Employees
  ADD CONSTRAINT fk_emp_dept
  FOREIGN KEY (DeptID) REFERENCES Departments (DeptID);

ALTER TABLE Employees DROP FOREIGN KEY fk_emp_dept;

DESC Employees;

ALTER TABLE Departments DROP PRIMARY KEY;

ALTER TABLE Employees RENAME COLUMN EmpName TO EmployeeName;


ALTER TABLE Employees DROP COLUMN Phone;


RENAME TABLE Employees TO EmployeeDetails;


DROP TABLE Departments;

INSERT INTO Departments (DeptID, DeptName, dept_location) VALUES
(1, 'HR', 'Pune'),
(2, 'Finance', 'Mumbai'),
(3, 'IT', 'Bangalore'),
(4, 'Sales', 'Delhi'),
(5, 'Operations', 'Chennai');

INSERT INTO Employees (EmpID, EmpName, Salary, JoinDate, Email, Phone, DeptID) VALUES
(101, 'Amit Sharma', 45000.00, '2022-03-15', 'amit@example.com', '987654321', 1),
(102, 'Priya Patil', 52000.00, '2021-07-01', 'priya@example.com', '987650123', 2),
(103, 'Rahul Verma', 60000.00, '2020-11-20', 'rahul@example.com', '912345678', 3),
(104, 'Sneha Kulkarni', 48000.00, '2023-01-10', 'sneha@example.com', '99887766', 4),
(105, 'Vikram Singh', 55000.00, '2019-09-05', 'vikram@example.com', '901234567', 5);

SELECT * FROM Employees;

SELECT * FROM Departments;


