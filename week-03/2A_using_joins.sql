USE northwind;
-- Create a single query to list the product id, product name, unit price and category
-- name of all products. Order by category name and within that, by product name
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products p
JOIN categories c
	ON p.CategoryID = c.CategoryID
	ORDER BY c.CategoryName, p.ProductName;
    
-- Create a single query to list the product id, product name, unit price and supplier
-- name of all products that cost more than $75. Order by product name
SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM products p
JOIN suppliers s
	ON p.SupplierID = s.SupplierID
    WHERE p.UnitPrice > 75
    ORDER BY p.ProductName;

-- Create a single query to list the product id, product name, unit price, category name,
-- and supplier name of every product. Order by product name
SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM products p
JOIN categories c
ON p.CategoryID = c.CategoryID
JOIN supplliers s
ON p.SuppliersID = s.SupplierID
ORDER BY p.ProductName;

-- Create a single query to list the order id, ship name, ship address, and shipping
-- company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
-- shipped to
SELECT o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName AS Shipper
FROM orders o
JOIN shippers s
ON o.ShipVia = s.ShipperID 
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper, o.ShipName;

-- Start from the same query as above (#4), but omit OrderID and add logic to group by
-- ship name, with a count of how many orders were shipped for that ship name

SELECT o.ShipName, o.ShipAddress, s.CompanyName AS Shipper, COUNT(*) AS OrderCount
FROM orders o JOIN shippers s ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName, o.ShipAddress, s.CompanyName
ORDER BY Shipper, o.ShipName;

-- Create a single query to list the order id, order date, ship name, ship address of all
-- orders that included Sasquatch Ale.
-- ∗ Hint: You will need to join on three tables to accomplish this. (One of these tables
-- has a sneaky space in the name, so you will need to surround it with backticks, like
-- this: `table name`)
SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM orders o
JOIN `order details` od
ON o.OrderID = od.OrderID
JOIN products p ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';

