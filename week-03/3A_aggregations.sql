USE northwind;
SELECT MIN(UnitPrice) AS CheapestPrice
FROM northwind.products;

SELECT AVG(UnitPrice) as AveragePrice
FROM northwind.products;

SELECT MAX(UnitPrice) as MostExpensive
FROM northwind.products;

SELECT p.ProductName, s.CompanyName AS SupplierName, p.UnitPrice
FROM northwind.products p
INNER JOIN northwind.suppliers s
ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = 263.50;

SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM northwind.employees;

SELECT MAX(Salary) AS HighestSalary,
MIN(Salary) AS LowestSalary
FROM northwind.employees;

SELECT s.SupplierID, s.CompanyName AS SupplierName,
COUNT(p.ProductID) AS NumberOfItems
FROM northwind.suppliers s 
LEFT JOIN northwind.products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

SELECT c.CategoryName, ROUND(AVG(p.UnitPrice), 2) AS AveragePrice
FROM northwind.categories c
LEFT JOIN northwind.products p
ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, c.CategoryName;

SELECT s.CompanyName AS SupplierName,
COUNT(p.ProductID) AS NumberofItems
FROM northwind.suppliers s
INNER JOIN northwind.products p
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

SELECT ProductID, ProductName, ROUND(UnitPrice * UnitsInStock, 2) as InventoryValue
FROM northwind.products
WHERE UnitsInStock > 0 
ORDER BY InventoryValue DESC, ProductName ASC;
