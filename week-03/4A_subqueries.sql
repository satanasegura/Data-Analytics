USE northwind;

SELECT ProductName, UnitPrice
FROM northwind.products
WHERE UnitPrice = (
SELECT MAX(UnitPrice)
FROM northwind.products);

SELECT p.ProductName, c.CategoryName, p.UnitPrice
FROM northwind.products p
INNER JOIN northwind.categories c
ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = ( SELECT MIN(UnitPrice) 
FROM northwind.products );

SELECT OrderID, ShipName, ShipAddress
FROM northwind.orders
WHERE ShipVia = (
SELECT ShipperID
FROM  northwind.shippers
WHERE CompanyName = 'Federal Shipping'
);

SELECT OrderID
FROM northwind.`order details`
WHERE ProductID = (
SELECT ProductID
FROM northwind.products 
WHERE ProductName = 'Sasquatch Ale'
);

SELECT FirstName, LastName
FROM northwind.employees
WHERE EmployeeID = (
SELECT EmployeeID
FROM northwind.orders
WHERE OrderID = 10266);