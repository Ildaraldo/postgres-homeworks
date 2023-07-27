-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    employee_id bigserial PRIMARY KEY NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    title text,
    birth_date date,
    notes text
);

CREATE TABLE customers
(
    customer_id VARCHAR(50) PRIMARY KEY NOT NULL,
    company_name VARCHAR(200),
    contact_name VARCHAR(100)
);


CREATE TABLE orders
(
    order_id bigserial PRIMARY KEY NOT NULL,
    customer_id VARCHAR(50) REFERENCES customers(customer_id),
    employee_id bigserial REFERENCES employees(employee_id),
    order_date date,
    ship_city VARCHAR(100)
);

