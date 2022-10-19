-- Выбрать все заказы, отсортировать по required_date (по убыванию)
-- и отсортировать по дате отгрузке (по возрастанию)

SELECT *
FROM orders
ORDER BY required_date DESC;

SELECT *
FROM orders
ORDER BY shipped_date;

-- Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA

SELECT ship_country,
AVG(shipped_date - order_date) as avg
FROM orders
WHERE ship_country = 'USA'
GROUP BY ship_country;

--Найти сумму, на которую имеется товаров (количество * цену)
-- причём таких, которые не сняты с продажи (см. на поле discontinued)

SELECT SUM(unit_price * units_in_stock)
FROM products
WHERE discontinued = 0;