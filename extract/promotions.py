import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE PROMOTIONS')

def run(db_context):
    channels = pd.read_csv('promotions.csv')
    channels.to_sql('PROMOTIONS', db_context, if_exists='append', index=False)