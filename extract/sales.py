import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE SALES')

def run(db_context):
    channels = pd.read_csv('sales.csv')
    channels.to_sql('SALES', db_context, if_exists='append', index=False)