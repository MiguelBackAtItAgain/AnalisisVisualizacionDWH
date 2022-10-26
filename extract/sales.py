import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE SALES')

def run(db_context):
    sales = pd.read_csv('CSVs\sales.csv')
    sales.to_sql('SALES', db_context, if_exists='append', index=False)