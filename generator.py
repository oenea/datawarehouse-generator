import csv
import uuid
import random
import os
from faker import Faker
from datetime import datetime, timedelta, date
from randomtimestamp import randomtimestamp
import faker_commerce

fake = Faker("pl_PL")
fake.add_provider(faker_commerce.Provider)
output = 'output'

# number of records
num_material = 100
num_productCatalogue = 1000
num_employees = 50
num_products = 1000
num_returns = 1000
num_complaints = 100

num_products_b = 100
num_returns_b = 100
num_complaints_b = 100
employees = []
products = []
productCatalogue = []

material_types = {
    'plastic': ['PVC', 'PE', 'PC'],
    'wood' : ['Oak', 'Pine', 'Teak'],
    'metal' : ['Aluminium', 'Steel', 'Copper']
}

category_names = [
    'Tools', 'Plumbing', 'Outdoor', 'Kitchen', 'Flooring', 'Storage'
]

num_products = 100  # Number of products
num_months = 12     # Number of months to simulate data for
material = []
products = []
complaints = []
returns = []
return_processing = []

def generate_spreadsheets():
    sheet1_data = []
    sheet2_data = []
    sheet1_data_filename = 'Sheet1_Product_Sales_Info.csv'

    for month in range(1, num_months + 1):
        for product in products:
            catalogue_id = product['catalogue_id']
            catalogue_ = [item for item in productCatalogue if str(item["id"]) == catalogue_id][0]
            insertion_date = catalogue_['introduction_date']
            price = round(random.uniform(5, 100), 2)
            discound_applied = random.randint(1, 40)
            random_days_after_insertion = random.randint(1, 28)
            sale_date = (insertion_date + timedelta(days=random_days_after_insertion)).strftime('%Y-%m-%d')

            sheet1_data.append({
                'id' : str(uuid.uuid4()),
                'product_id' : product['id'],
                'price' : price,
                'discount_applied' : discound_applied,
                'sale_date' : sale_date
            })
            
    with open(sheet1_data_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'product_id', 'price', 'discount_applied', 'sale_date'])
        writer.writeheader()
        writer.writerows(sheet1_data)
        print(f"Sheet1_data written to {'Sheet1_Product_Sales_Info.csv'}")

    #with open('Sheet2_Individual_Product_Sales.csv', mode='w', newline='', encoding='utf-8') as file:
    #    writer = csv.DictWriter(file, fieldnames=['Product name', 'Number of units sold', 'Price of a single unit', 'Date'])
    #    writer.writeheader()
    #    writer.writerows(sheet1_data)

    print("Sales data generated.")
def random_date(start_year, end_year):
    return fake.date_between(start_date=date(start_year, 1, 1), end_date=date(end_year, 12, 31))

def generate_first_period():

    for material_type, materials in material_types.items():
        for material_ in materials:
            material.append({
                'id' : str(uuid.uuid4()),
                'material_type' : material_type,
                'material' : material_
            })

    for _ in range(num_employees):
        employees.append({
            'id': str(uuid.uuid4()),
            'name_': fake.name(),
            'birth_year': random_date(1960, 2005).strftime('%Y-%m-%d %H:%M:%S'),
            'career_stage' : fake.random_element(['Intern', 'Junior', 'Mid', 'Senior', 'Principal']),
            'employment_start': random_date(2000, 2024).strftime('%Y-%m-%d %H:%M:%S')
        })
    
    for _ in range(num_productCatalogue):
        ret_material = random.choice(material)
        productCatalogue.append({
            'id' : str(uuid.uuid4()),
            'name_' : fake.ecommerce_name().capitalize() + 
                      "_" + str(fake.pyint(0, 1000)), # too little ecomerce_name to be unique
            'catalogue_price' : random.randint(3, 100),
            'category' : fake.random_element(category_names),
            'material_id' : ret_material['id'],
            'introduction_date' : random_date(2000, 2022)
        })

    for _ in range(num_products):
        ret_productCatalogue = random.choice(productCatalogue)
        products.append({
            'id': str(uuid.uuid4()),
            'catalogue_id' : ret_productCatalogue['id'],
            'serial_number' : str(uuid.uuid4())
        })

    for _ in range(num_returns):
        product = random.choice(products)
        employee = random.choice(employees)
        status = fake.random_element(['Pending', 'In Progress', 'Completed', 'Canceled'])
        processing_start = random_date(2000, 2024)
        processing_finished = processing_start + timedelta(days=random.randint(1, 30))
        returns.append({
            'id': str(uuid.uuid4()),
            'product_id': product['id'],
            'status_': status,
            'employee_id': employee['id'],
            'company_cost': round(random.uniform(50, 500), 2),
            'description_': fake.sentence(),
            'processing_started': processing_start.strftime('%Y-%m-%d %H:%M:%S'),
            'processing_finished': processing_finished.strftime('%Y-%m-%d %H:%M:%S')
        })

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

    for _ in range(num_returns):
        ret = random.choice(returns)
        return_processing.append({
            'employee_id': ret['employee_id'],
            'return_id': ret['id']
        })

    period = 't1'    
    save_to_csv(material, f'{output}/Material_{period}.csv', ['id', 'material_type', 'material'])
    save_to_csv(employees, f'{output}/Employee_{period}.csv', ['id', 'name_', 'birth_year', 'career_stage', 'employment_start'])
    save_to_csv(complaints, f'{output}/Complaints_{period}.csv', ['id', 'return_id', 'issue_date', 'resolve_date', 'complaint'])
    save_to_csv(productCatalogue, f'{output}/ProductCatalogue_{period}.csv', ['id', 'name_', 'catalogue_price', 'category', 'material_id', 'introduction_date'])
    save_to_csv(products, f'{output}/Products_{period}.csv', ['id', 'catalogue_id', 'serial_number'])
    save_to_csv(returns, f'{output}/Returns_{period}.csv', ['id', 'product_id', 'status_', 'employee_id', 'company_cost', 'description_', 'processing_started', 'processing_finished'])
    save_to_csv(return_processing, f'{output}/ReturnProcessing_{period}.csv', ['employee_id', 'return_id'])

def generate_second_period():

    for _ in range(num_employees):
        employees.append({
            'id' : str(uuid.uuid4()),
            'name_' : fake.name(),
            'birth_year' : random_date(1960, 2005).strftime('%Y-%m-%d %H:%M:%S'),
            'career_stage' : fake.random_element(['Intern', 'Junior', 'Mid', 'Senior', 'Principal']),
            'employment_start' : random_date(2000, 2024).strftime('%Y-%m-%d %H:%M:%S')
        })
    
    productCatalogue = []
    for _ in range(num_productCatalogue):
        ret_material = random.choice(material)
        productCatalogue.append({
            'id' : str(uuid.uuid4()),
            'name_' : fake.ecommerce_name().capitalize() + 
                      "_" + str(fake.pyint(0, 1000)), # too little ecomerce_name to be unique
            'catalogue_price' : random.randint(10, 200),
            'category' : fake.random_element(category_names),
            'material_id' : ret_material['id'],
            'introduction_date' : random_date(2000, 2022)
        })

    products = []
    for _ in range(num_products_b):
        ret_productCatalogue = random.choice(productCatalogue)
        products.append({
            'id': str(uuid.uuid4()),
            'catalogue_id' : ret_productCatalogue['id'],
            'serial_number' : str(uuid.uuid4())
        })

    returns = []
    for _ in range(num_returns_b):
        product = random.choice(products)
        employee = random.choice(employees)
        status = fake.random_element(['Pending', 'In Progress', 'Completed', 'Canceled'])
        processing_start = random_date(2000, 2024)
        processing_finished = processing_start + timedelta(days=random.randint(1, 30))
        returns.append({
            'id': str(uuid.uuid4()),
            'product_id': product['id'],
            'status_': status,
            'employee_id': employee['id'],
            'company_cost': round(random.uniform(50, 500), 2),
            'description_': fake.sentence(),
            'processing_started': processing_start.strftime('%Y-%m-%d %H:%M:%S'),
            'processing_finished': processing_finished.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    complaints = []
    for _ in range(num_complaints_b):
        ret = random.choice(returns)
        issue_date = random_date(2000, 2022)
        resolve_date = issue_date + timedelta(days=random.randint(1, 10))
        complaints.append({
            'id' : str(uuid.uuid4()),
            'return_id' : ret['id'],
            'issue_date' : issue_date.strftime('%Y-%m-%d %H:%M:%S'),
            'resolve_date' : resolve_date.strftime('%Y-%m-%d %H:%M:%S'),
            'complaint' : fake.sentence()
        })

    returns = []
    for _ in range(num_returns_b):
        for product_ in products:
            catalogue_id = product_['catalogue_id']
            catalogue_ = [item for item in productCatalogue if str(item["id"]) == catalogue_id][0]
            #print(catalogue)
            material_id = catalogue_['material_id']
            #print(material_id)
            material_ = [item for item in material if str(item["id"]) == material_id][0]

            #print(material_['material_type'])
            if material_['material_type'] == 'metal' and catalogue_['introduction_date'].year >= 2023:
                product = product_
                employee = random.choice(employees)
                status = fake.random_element(['Pending', 'In Progress', 'Completed', 'Canceled'])
                processing_start = random_date(2024, 2024)
                processing_finished = processing_start + timedelta(days=random.randint(1, 30)) if status == 'Completed' and status == 'Canceled' else None
                returns.append({
                    'id' : str(uuid.uuid4()),
                    'product_id' : product['id'],
                    'status_' : status,
                    'employee_id' : employee['id'],
                    'company_cost' : round(random.uniform(50, 500), 2),
                    'description_' : fake.sentence(),
                    'processing_started' : processing_start.strftime('%Y-%m-%d %H:%M:%S'),
                    'processing_finished' : processing_finished.strftime('%Y-%m-%d %H:%M:%S') if processing_finished else ''
                })

    for _ in range(num_returns_b // 3):
        for product_ in products:
            product = product_
            employee = random.choice(employees)
            status = fake.random_element(['Pending', 'In Progress', 'Completed', 'Canceled'])
            processing_start = random_date(2024, 2024)
            processing_finished = processing_start + timedelta(days=random.randint(1, 30)) if status == 'Completed' else None
            returns.append({
                'id' : str(uuid.uuid4()),
                'product_id' : product['id'],
                'status_' : status,
                'employee_id' : employee['id'],
                'company_cost' : round(random.uniform(50, 500), 2),
                'description_' : fake.sentence(),
                'processing_started' : processing_start.strftime('%Y-%m-%d %H:%M:%S'),
                'processing_finished' : processing_finished.strftime('%Y-%m-%d %H:%M:%S') if processing_finished else ''
            })

    return_processing = []
    for _ in range(num_returns):
        ret = random.choice(returns)
        return_processing.append({
            'employee_id' : ret['employee_id'],
            'return_id' : ret['id']
        })

    period = 't2'
    save_to_csv(employees, f'{output}/Employee_{period}.csv', ['id', 'name_', 'birth_year', 'career_stage', 'employment_start'])
    save_to_csv(complaints, f'{output}/Complaints_{period}.csv', ['id', 'return_id', 'issue_date', 'resolve_date', 'complaint'])
    save_to_csv(productCatalogue, f'{output}/ProductCatalogue_{period}.csv', ['id', 'name_', 'catalogue_price', 'category', 'material_id', 'introduction_date'])
    save_to_csv(returns, f'{output}/Returns_{period}.csv', ['id', 'product_id', 'status_', 'employee_id', 'company_cost', 'description_', 'processing_started', 'processing_finished'])
    save_to_csv(return_processing, f'{output}/ReturnProcessing_{period}.csv', ['employee_id', 'return_id'])

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

BULK INSERT Complaint FROM '{base_path}/Complaints_t2.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnProcessing FROM '{base_path}/ReturnProcessing_t2.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ReturnsTable FROM '{base_path}/Returns_t2.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')
BULK INSERT ProductCatalogue FROM '{base_path}/ProductCatalogue_t2.csv' WITH (fieldterminator=',',rowterminator='\\n', DATAFILETYPE = 'widechar', CODEPAGE = '65001')

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
    generate_spreadsheets()

if __name__ == "__main__":
    main()
