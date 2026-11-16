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
	
    
    