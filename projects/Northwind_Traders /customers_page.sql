-- Посчитать количество заказчиков
SELECT
COUNT (*)
FROM customers;

-- Выбрать все уникальные сочетания городов и стран,
-- в которых "зарегестрированы" заказчики
SELECT
customers.city,
customers.country
FROM customers
GROUP BY customers.city, customers.country;

-- Найти заказчиков и обслуживающих их заказы сотрудников,
-- таких, что и заказчики и сотрудники из города London,
-- а доставка идёт компанией Speedy Express.
-- Вывести компанию заказчика и ФИО сотрудника.
SELECT
customers.company_name,
employees.last_name,
employees.first_name
FROM orders LEFT JOIN customers ON customers.customer_id = orders.customer_id
LEFT JOIN employees ON employees.employee_id = orders.employee_id
LEFT JOIN shippers ON shippers.shipper_id = orders.ship_via
WHERE customers.city = 'London' and employees.city = 'London'
  and shippers.company_name = 'Speedy Express';

--Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
SELECT company_name, orders.order_id
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
WHERE customers.customer_id NOT IN (SELECT customer_id FROM orders);
