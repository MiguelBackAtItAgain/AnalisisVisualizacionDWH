import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE CUSTOMERS')

def run(db_context):
    channels = pd.read_csv('customers.csv')
    channels.to_sql('CUSTOMERS', db_context, if_exists='append', index=False)