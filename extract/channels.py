import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE CHANNELS')

def run(db_context):
    channels = pd.read_csv('channels.csv')
    channels.to_sql('CHANNELS', db_context, if_exists='append', index=False)