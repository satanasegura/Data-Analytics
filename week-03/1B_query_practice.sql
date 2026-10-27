SELECT OrderID,
	OrderDate,
    ShipName,
    ShipCountry
FROM orders
LIMIT 50;

SELECT ProductID, ProductName, UnitPrice
	FROM products;
 
 SELECT ProductID, ProductName, UnitPrice
	FROM products
	WHERE UnitPrice <= 7.50;

SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
	FROM products
    WHERE UnitsInStock = 0 
    AND UnitsOnOrder > 0;
    
    SELECT ProductID, ProductName, CategoryID
		FROM products;
	
    SELECT *
    FROM categories;
    
    SELECT p.ProductID,
		   p.ProductName,
           c.CategoryName
           FROM products p
           JOIN categories c
			ON p.CategoryID = c.CategoryID
			WHERE c.CategoryName = 'Seafood';
	
    SELECT * FROM suppliers;
    
    SELECT SupplierID, CompanyName
		FROM suppliers
        WHERE CompanyName = 'Tokyo Traders';
        
        SELECT productID, ProductName, SupplierID
			FROM products
            WHERE SupplierID = 4;
            
		SELECT COUNT(*) AS EmployeeCount
        FROM employees;
        
        SELECT EmployeeID, FirstName, LastName, Title
        FROM employees
        WHERE Title LIKE '%manager%';
        
        
    
    