
USE CompanyDatabase;
GO

BULK INSERT Employee FROM '/mnt/c/Users/oenea/Downloads/DataWarehouse-generator/output/Employee_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Products FROM '/mnt/c/Users/oenea/Downloads/DataWarehouse-generator/output/Products_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Complaint FROM '/mnt/c/Users/oenea/Downloads/DataWarehouse-generator/output/Complaints_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnProcessing FROM '/mnt/c/Users/oenea/Downloads/DataWarehouse-generator/output/ReturnProcessing_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnsTable FROM '/mnt/c/Users/oenea/Downloads/DataWarehouse-generator/output/Returns_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Material FROM '/mnt/c/Users/oenea/Downloads/DataWarehouse-generator/output/Material_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ProductCatalogue FROM '/mnt/c/Users/oenea/Downloads/DataWarehouse-generator/output/ProductCatalogue_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
GO
