
USE CompanyDatabase;
GO

BULK INSERT Employee FROM 'C:\Users\oenea\Downloads\datawarehouse-generator/output/Employee_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Products FROM 'C:\Users\oenea\Downloads\datawarehouse-generator/output/Products_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Complaint FROM 'C:\Users\oenea\Downloads\datawarehouse-generator/output/Complaints_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnProcessing FROM 'C:\Users\oenea\Downloads\datawarehouse-generator/output/ReturnProcessing_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnsTable FROM 'C:\Users\oenea\Downloads\datawarehouse-generator/output/Returns_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Material FROM 'C:\Users\oenea\Downloads\datawarehouse-generator/output/Material_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ProductCatalogue FROM 'C:\Users\oenea\Downloads\datawarehouse-generator/output/ProductCatalogue_t1.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
GO
