import csv
import uuid
import random
import os
from faker import Faker
from datetime import datetime, timedelta, date
from randomtimestamp import randomtimestamp
import faker_commerce

output = 'output'

fake = Faker("pl_PL")
fake.add_provider(faker_commerce.Provider)

# number of records
num_material = 100
num_productCatalogue = 100
num_employees = 500
num_products = 1000
num_returns = 100000
num_complaints = 10000

num_products_b = 1000
num_returns_b = 100
num_complaints_b = 1000
employees = []
products = []

def random_date(start_year, end_year):
    return fake.date_between(start_date=date(start_year, 1, 1), end_date=date(end_year, 12, 31))

def generate_first_period():
    # generate Employee
    
    for _ in range(num_employees):
        employees.append({
            'id': str(uuid.uuid4()),
            'name': fake.name(),
            'birth_year': random_date(1960, 2005).strftime('%Y-%m-%d %H:%M:%S'),
            'employment_start': random_date(2000, 2024).strftime('%Y-%m-%d %H:%M:%S')
        })

    # generate Products
    for _ in range(num_products):
        products.append({
            'id': str(uuid.uuid4()),
            'name': fake.ecommerce_name().capitalize(),
            'issue_year': random.randint(2000, 2022),
            'main_building_material': fake.random_element(['Metal', 'Plastic PBT', 'Plastic POM', 'Plastic ABS', 'Wood', 'Glass Fiber', 'Steel', 'Aluminum', 'Glass', 'Fiber'])
        })

    # generate Returns
    returns = []
    for _ in range(num_returns):
        product = random.choice(products)
        employee = random.choice(employees)
        status = fake.random_element(['Pending', 'In Progress', 'Completed', 'Canceled'])
        processing_start = random_date(2000, 2024)
        processing_finished = processing_start + timedelta(days=random.randint(1, 30)) if status == 'Completed' else None
        returns.append({
            'id': str(uuid.uuid4()),
            'product_id': product['id'],
            'status': status,
            'employee_id': employee['id'],
            'company_cost': round(random.uniform(50, 500), 2),
            'description': fake.sentence(),
            'processing_started': processing_start.strftime('%Y-%m-%d %H:%M:%S'),
            'processing_finished': processing_finished.strftime('%Y-%m-%d %H:%M:%S') if processing_finished else ''
        })

    # generate ReturnProcessing
    return_processing = []
    for _ in range(num_returns):
        ret = random.choice(returns)
        return_processing.append({
            'employee_id': ret['employee_id'],
            'return_id': ret['id']
        })

    # generate Complaints
    complaints = []
    for _ in range(num_complaints):
        ret = random.choice(returns)
        issue_date = random_date(2000, 2022)
        resolve_date = issue_date + timedelta(days=random.randint(1, 10))
        complaints.append({
            'id': str(uuid.uuid4()),
            'return_id': ret['id'],
            'issue_date': issue_date.strftime('%Y-%m-%d %H:%M:%S'),
            'resolve_date': resolve_date.strftime('%Y-%m-%d %H:%M:%S'),
            'complaint': fake.sentence()
        })

    material = []
    for _ in range(num_material):
        material.append({
            'id' : str(uuid.uuid4()),
            'material_type' : fake.sentence(),
            'material' :  fake.sentence()
        })

    productCatalogue = []
    for _ in range(num_productCatalogue):
        ret_material = random.choice(material)
        productCatalogue.append({
            'id' : str(uuid.uuid4()),
            'name' : fake.sentence(),
            'catalogue_price' : random.randint(3, 100),
            'category' : fake.sentence(),
            'material_id' : ret_material['id'],
            'introduction_date' : random_date(2000, 2022)
        })
    
    period = 't1'
    save_to_csv(employees, f'{output}/Employee_{period}.csv', ['id', 'name', 'birth_year', 'employment_start'])
    save_to_csv(products, f'{output}/Products_{period}.csv', ['id', 'name', 'issue_year', 'main_building_material'])
    save_to_csv(returns, f'{output}/Returns_{period}.csv', ['id', 'product_id', 'status', 'employee_id', 'company_cost', 'description', 'processing_started', 'processing_finished'])
    save_to_csv(return_processing, f'{output}/ReturnProcessing_{period}.csv', ['employee_id', 'return_id'])
    save_to_csv(complaints, f'{output}/Complaints_{period}.csv', ['id', 'return_id', 'issue_date', 'resolve_date', 'complaint'])
    save_to_csv(material, f'{output}/Material_{period}.csv', ['id', 'material_type', 'material'])
    save_to_csv(productCatalogue, f'{output}/ProductCatalogue_{period}.csv', ['id', 'name', 'catalogue_price', 'category', 'material_id', 'introduction_date'])

def generate_second_period():
    # generate Products
    products_new = []
    for _ in range(num_products_b):
        products_new.append({
            'id': str(uuid.uuid4()),
            'name': fake.ecommerce_name().capitalize(),
            'issue_year': random.randint(2023, 2024),
            'main_building_material': fake.random_element(['Metal', 'Plastic ABS', 'Wood', 'Glass Fiber', 'Steel'   , 'Fiber'])
        })

    # generate Returns
    returns = []
    for _ in range(num_returns//3):
        for product in products:
            if product['main_building_material'] == 'Plastic ABS' and (product['issue_year'] == 2021 or product['issue_year'] == 2022 or product['issue_year'] == 2023 or product['issue_year'] == 2024):
                employee = random.choice(employees)
                status = fake.random_element(['Pending', 'In Progress', 'Completed', 'Canceled'])
                processing_start = random_date(2023, 2024)
                processing_finished = processing_start + timedelta(days=random.randint(1, 30)) if status == 'Completed' else None
                returns.append({
                    'id': str(uuid.uuid4()),
                    'product_id': product['id'],
                    'status': status,
                    'employee_id': employee['id'],
                    'company_cost': round(random.uniform(50, 5000), 2),
                    'description': fake.sentence(),
                    'processing_started': processing_start.strftime('%Y-%m-%d %H:%M:%S'),
                    'processing_finished': processing_finished.strftime('%Y-%m-%d %H:%M:%S') if processing_finished else ''
                })
    print(len(returns))

    for _ in range(num_returns_b):
        product = random.choice(products_new)
        employee = random.choice(employees)
        status = fake.random_element(['Pending', 'In Progress', 'Completed', 'Canceled'])
        processing_start = random_date(2023, 2024)
        processing_finished = processing_start + timedelta(days=random.randint(1, 30)) if status == 'Completed' else None
        returns.append({
            'id': str(uuid.uuid4()),
            'product_id': product['id'],
            'status': status,
            'employee_id': employee['id'],
            'company_cost': round(random.uniform(150, 500), 2),
            'description': fake.sentence(),
            'processing_started': processing_start.strftime('%Y-%m-%d %H:%M:%S'),
            'processing_finished': processing_finished.strftime('%Y-%m-%d %H:%M:%S') if processing_finished else ''
        })

    # generate ReturnProcessing
    return_processing = []
    for _ in range(num_returns_b):
        ret = random.choice(returns)
        return_processing.append({
            'employee_id': ret['employee_id'],
            'return_id': ret['id']
        })

    # generate Complaints
    complaints = []
    for _ in range(num_complaints_b):
        ret = random.choice(returns)
        issue_date = random_date(2023, 2024)
        resolve_date = issue_date + timedelta(days=random.randint(1, 10))
        complaints.append({
            'id': str(uuid.uuid4()),
            'return_id': ret['id'],
            'issue_date': issue_date.strftime('%Y-%m-%d %H:%M:%S'),
            'resolve_date': resolve_date.strftime('%Y-%m-%d %H:%M:%S'),
            'complaint': fake.sentence()
        })

    employee = []

    period = 't2'
    save_to_csv(employees, f'{output}/Employee_{period}.csv', ['id', 'name', 'birth_year', 'employment_start'])
    save_to_csv(products, f'{output}/Products_{period}.csv', ['id', 'name', 'issue_year', 'main_building_material'])
    save_to_csv(returns, f'{output}/Returns_{period}.csv', ['id', 'product_id', 'status', 'employee_id', 'company_cost', 'description', 'processing_started', 'processing_finished'])
    save_to_csv(return_processing, f'{output}/ReturnProcessing_{period}.csv', ['employee_id', 'return_id'])
    save_to_csv(complaints, f'{output}/Complaints_{period}.csv', ['id', 'return_id', 'issue_date', 'resolve_date', 'complaint'])

def save_to_csv(data, filename, fieldnames, mode='w'):
    with open(filename, mode=mode, newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def indent_csv(filename):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        file.write("# new data \n\n")


def write_sql_to_files():
    base_path = os.getcwd() + '/' + output
    sql_template = f"""
USE CompanyDatabase;
GO

BULK INSERT Employee FROM '{base_path}/Employee_t1.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Products FROM '{base_path}/Products_t1.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Complaint FROM '{base_path}/Complaints_t1.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnProcessing FROM '{base_path}/ReturnProcessing_t1.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnsTable FROM '{base_path}/Returns_t1.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Material FROM '{base_path}/Material_t1.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ProductCatalogue FROM '{base_path}/ProductCatalogue_t1.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
GO
"""
    with open("insert_t1.sql", "w") as file:
        file.write(sql_template)
    print(f"SQL file has been written to 'insert_t1.sql' in {base_path}")

    sql_template2 = f"""
USE CompanyDatabase;
GO

BULK INSERT Employee FROM '{base_path}/Employee_t2.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Products FROM '{base_path}/Products_t2.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT Complaint FROM '{base_path}/Complaints_t2.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnProcessing FROM '{base_path}/ReturnProcessing_t2.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnsTable FROM '{base_path}/Returns_t2.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
GO
"""

    with open("insert_t2.sql", "w") as file:
        file.write(sql_template2)

    print(f"SQL file has been written to 'insert_t2.sql' in {base_path}")

def main():
    generate_first_period()
    generate_second_period()
    print("database data generated.")
    write_sql_to_files()

if __name__ == "__main__":
    main()
