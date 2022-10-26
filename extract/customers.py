import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE CUSTOMERS')

def run(db_context):
    customers = pd.read_csv('CSVs\customers.csv')
    customers = customers.rename(columns={'CUST_MAIN_PHONE_NUMBER': 'CUST_MAIN_PHONE_INTEGER'})
    customers.to_sql('CUSTOMERS', db_context, if_exists='append', index=False)