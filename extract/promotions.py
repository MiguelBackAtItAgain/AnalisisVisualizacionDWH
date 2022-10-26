import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE PROMOTIONS')

def run(db_context):
    promotions = pd.read_csv('CSVs\promotions.csv')
    promotions.to_sql('PROMOTIONS', db_context, if_exists='append', index=False)