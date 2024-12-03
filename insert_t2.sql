
USE CompanyDatabase;
GO

BULK INSERT Products FROM 'C:\Users\oenea\Downloads\DataWarehouse-generator/output/Products_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Complaint FROM 'C:\Users\oenea\Downloads\DataWarehouse-generator/output/Complaints_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnProcessing FROM 'C:\Users\oenea\Downloads\DataWarehouse-generator/output/ReturnProcessing_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnsTable FROM 'C:\Users\oenea\Downloads\DataWarehouse-generator/output/Returns_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ProductCatalogue FROM 'C:\Users\oenea\Downloads\DataWarehouse-generator/output/ProductCatalogue_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')

GO
