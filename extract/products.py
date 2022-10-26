import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE PRODUCTS')

def run(db_context):
    products = pd.read_csv('CSVs\products.csv')
    products.to_sql('PRODUCTS', db_context, if_exists='append', index=False)