create DATABASE TCL;

use TCL;

CREATE TABLE orders(order_id int PRIMARY KEY , customer_name VARCHAR(100), status VARCHAR(50));
desc orders;

set autocommit = 0 ;
INSERT INTO orders VALUES(101, "John","Approved");
INSERT INTO orders VALUES(102, "Shawn","Pending");
INSERT INTO orders VALUES(103, "Billy","Approved");
INSERT INTO orders VALUES(104, "Harvard","Pending");
TRUNCATE TABLE orders;
SELECT * FROM orders;
ROLLBACK;
COMMIT;
INSERT INTO orders VALUES(106, "Scott","Pending");
INSERT INTO orders VALUES(107, "Snappy","Approved");

UPDATE orders SET status = "Approved" where order_id = 105;
UPDATE orders SET status = "Pending" where order_id = 107;

SAVEPOINT SP1;

UPDATE orders SET status = "Approved" where order_id = 107;

SAVEPOINT SP2;


ROLLBACK to SAVEPOINT SP1;

ROLLBACK to SAVEPOINT SP2;

