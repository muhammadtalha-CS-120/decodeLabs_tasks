USE DecodeLabs_Project3;

SELECT
    Product,
    SUM(TotalPrice) AS TotalSales
FROM [Dataset_for_Data_Analytics]
GROUP BY Product
ORDER BY TotalSales DESC;


SELECT
    Date,
    SUM(TotalPrice) AS DailySales
FROM [Dataset_for_Data_Analytics]
GROUP BY Date
ORDER BY Date;

SELECT
    Product,
    SUM(Quantity) AS TotalQuantity
FROM [Dataset_for_Data_Analytics]
GROUP BY Product
ORDER BY TotalQuantity DESC;

SELECT Product, SUM(Quantity) AS AverageSales FROM [Dataset_for_Data_Analytics] GROUP BY Product ORDER BY AverageSales DESC;

SELECT PRODUCT, COUNT(OrderID) AS NumberofOrders FROM [Dataset_for_Data_Analytics] GROUP BY Product ORDER BY NumberOfOrders DESC;

SELECT Count(OrderID) AS TotalOrders, SUM(Quantity) AS TotalQuantity, SUM(TotalPrice) AS TotalSales, AVG(TotalPrice) AS AverageOrderValue FROM [Dataset_for_Data_Analytics]