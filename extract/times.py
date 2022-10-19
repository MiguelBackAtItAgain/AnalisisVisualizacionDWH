import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE TIMES')

def run(db_context):
    channels = pd.read_csv('times.csv')
    channels.to_sql('TIMES', db_context, if_exists='append', index=False)