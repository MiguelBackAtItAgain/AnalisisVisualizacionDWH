import pandas as pd

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE TIMES')

def run(db_context):
    route = 'CSVs\\'
    times = pd.read_csv(route + 'times.csv')
    times = times.rename(columns={'DAY_NUMBER_IN_WEEK': 'DAY_INTEGER_IN_WEEK',
                'DAY_NUMBER_IN_MONTH': 'DAY_INTEGER_IN_MONTH',
                'CALENDAR_WEEK_NUMBER': 'CALENDAR_WEEK_INTEGER',
                'CALENDAR_MONTH_NUMBER': 'CALENDAR_MONTH_INTEGER'})
    times['CALENDAR_MONTH_NAME'] = ''
    times.to_sql('TIMES', db_context, if_exists='append', index=False)