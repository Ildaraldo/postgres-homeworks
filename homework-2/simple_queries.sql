-- Напишите запросы, которые выводят следующую информацию:
-- 1. "имя контакта" и "город" (contact_name, country) из таблицы customers (только эти две колонки)
SELECT contact_name, country
FROM customers;

-- 2. идентификатор заказа и разницу между датами формирования (order_date) заказа и его отгрузкой (shipped_date) из таблицы orders
SELECT order_id, (shipped_date - order_date) AS shipment_period
FROM orders;

-- 3. все города без повторов, в которых зарегистрированы заказчики (customers)
SELECT city
FROM customers
GROUP BY city;

-- 4. количество заказов (таблица orders)
SELECT COUNT(*) AS orders_count
FROM orders;

-- 5. количество стран, в которые отгружался товар (таблица orders, колонка ship_country)
SELECT COUNT(ship_country) AS all_ship_country
FROM (
		SELECT ship_country
		FROM orders
		GROUP BY ship_country
) AS ship_countries;

