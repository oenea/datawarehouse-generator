CREATE DATABASE CompanyDatabase;
GO

USE CompanyDatabase;
GO

CREATE TABLE Material (
    id UNIQUEIDENTIFIER PRIMARY KEY,
	material_type VARCHAR(255),
	material VARCHAR(255)
);

CREATE TABLE Employee (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    name_ VARCHAR(255) NOT NULL,
    birth_year DATE,
    career_stage VARCHAR(255),
    employment_start DATETIME
);

CREATE TABLE ProductCatalogue (
    id UNIQUEIDENTIFIER PRIMARY KEY,
	name_ VARCHAR(255),
	catalogue_price DECIMAL(18, 2),
	category VARCHAR(255),
	material_id UNIQUEIDENTIFIER,
	introduction_date DATETIME,
	FOREIGN KEY (material_id) REFERENCES Material(id)
);

CREATE TABLE Products (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    catalogue_id UNIQUEIDENTIFIER,
    serial_number UNIQUEIDENTIFIER,
    FOREIGN KEY (catalogue_id) REFERENCES ProductCatalogue(id)
);

CREATE TABLE ReturnsTable (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    product_id UNIQUEIDENTIFIER,
    status_ VARCHAR(50),
    employee_id UNIQUEIDENTIFIER,
    company_cost DECIMAL(18, 2),
    description_ VARCHAR(1000),
    processing_started DATETIME,
    processing_finished DATETIME,
    FOREIGN KEY (product_id) REFERENCES Products(id),
    FOREIGN KEY (employee_id) REFERENCES Employee(id)
);

CREATE TABLE Complaint (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    return_id UNIQUEIDENTIFIER,
    issue_date DATETIME,
    resolve_date DATETIME,
    complaint VARCHAR(1000)
    FOREIGN KEY (return_id) REFERENCES ReturnsTable(id)
);

CREATE TABLE ReturnProcessing (
    employee_id UNIQUEIDENTIFIER,
    return_id UNIQUEIDENTIFIER,
    FOREIGN KEY (employee_id) REFERENCES Employee(id),
    FOREIGN KEY (return_id) REFERENCES ReturnsTable(id)
);

GO