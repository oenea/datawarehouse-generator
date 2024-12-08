
USE CompanyDatabase;
GO

BULK INSERT Employee FROM 'G:\datawarehouse-generator/output/Employee_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Products FROM 'G:\datawarehouse-generator/output/Products_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Complaint FROM 'G:\datawarehouse-generator/output/Complaints_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnProcessing FROM 'G:\datawarehouse-generator/output/ReturnProcessing_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnsTable FROM 'G:\datawarehouse-generator/output/Returns_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Material FROM 'G:\datawarehouse-generator/output/Material_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ProductCatalogue FROM 'G:\datawarehouse-generator/output/ProductCatalogue_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
GO
