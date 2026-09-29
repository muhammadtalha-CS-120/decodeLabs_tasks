USE Decodelabs_project3;

SELECT* FROM [Dataset_for_Data_Analytics];

SELECT* FROM  [Dataset_for_Data_Analytics] WHERE Quantity>2;

SELECT * FROM [Dataset_for_Data_Analytics] ORDER BY TotalPrice DESC;

SELECT Product,COUNT(*) As TotalOrders FROM [Dataset_for_Data_Analytics] Group By Product;

SELECT COUNT(*) AS TotalOrders FROM [Dataset_for_Data_Analytics];

SELECT SUM(TotalPrice) AS TotalSales FROM [Dataset_for_Data_Analytics];

SELECT AVG(TotalPrice) AS AveragePrice FROM [Dataset_for_Data_Analytics];