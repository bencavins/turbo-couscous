expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""


avg_hire_age = """
SELECT AVG(HireDate - BirthDate)
FROM Employee;
"""


ten_most_expensive = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier
	ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
"""

largest_category = """
SELECT Category.CategoryName, COUNT(Product.Id) as product_count
FROM Product
JOIN Category
	ON Product.CategoryId = Category.Id
GROUP BY Category.CategoryName
ORDER BY product_count DESC
LIMIT 1;
"""