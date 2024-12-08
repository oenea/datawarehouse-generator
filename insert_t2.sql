
USE CompanyDatabase;
GO

BULK INSERT Complaint FROM 'G:\datawarehouse-generator/output/Complaints_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnProcessing FROM 'G:\datawarehouse-generator/output/ReturnProcessing_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnsTable FROM 'G:\datawarehouse-generator/output/Returns_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ProductCatalogue FROM 'G:\datawarehouse-generator/output/ProductCatalogue_t2.csv' WITH (fieldterminator=',',rowterminator='\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')

GO
