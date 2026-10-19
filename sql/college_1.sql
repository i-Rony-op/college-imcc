DESC Staff;

DESC Department;

ALTER TABLE Staff  ADD CONSTRAINT PRIMARY KEY(staff_id);

ALTER TABLE Department ADD CONSTRAINT FOREIGN KEY (dept_id) REFERENCES Staff (staff_id);

ALTER TABLE Department ADD PRIMARY KEY (dept_id);

ALTER TABLE Staff ADD CONSTRAINT fk_staff_dept FOREIGN KEY (dept_id) REFERENCES Department (dept_id);

select * from Staff;

SHOW CREATE TABLE Department;

ALTER TABLE Staff RENAME staff;

ALTER TABLE staff RENAME Staff;

DESC Staff;

ALTER TABLE Staff RENAME COLUMN first_name TO First_name;

DROP TABLE Department;

DROP TABLE Staff;


