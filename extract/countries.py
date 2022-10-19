import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE COUNTRIES')

def run(db_context):
    countries = pd.read_csv('countries.csv')
    countries.to_sql('COUNTRIES', db_context, if_exists='append', index=False)

