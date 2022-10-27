import pandas as pd
import datetime as dt

def transform_times(stg_db_context, transf_iteration):
    extracted_times = pd.read_sql(sql='times', con=stg_db_context)
    if not extracted_times.empty:
        extracted_times.loc[:,['DAY_INTEGER_IN_WEEK','DAY_INTEGER_IN_MONTH', 'CALENDAR_WEEK_INTEGER',
        'CALENDAR_MONTH_INTEGER', 'CALENDAR_YEAR']] = extracted_times.loc[:,['DAY_INTEGER_IN_WEEK','DAY_INTEGER_IN_MONTH', 'CALENDAR_WEEK_INTEGER',
        'CALENDAR_MONTH_INTEGER', 'CALENDAR_YEAR']].astype(int) 
        extracted_times['TIME_ID'] = extracted_times['TIME_ID'].apply(lambda x : dt.datetime.strptime(x, '%d-%b-%y'))
        extracted_times['END_OF_CAL_MONTH'] = extracted_times['END_OF_CAL_MONTH'].apply(lambda x : dt.datetime.strptime(x, '%d-%b-%y'))
        extracted_times['ETL_PROCESS_ID'] = transf_iteration
        extracted_times.to_sql(name='TIMES_TRANSF', con=stg_db_context, if_exists='append', index=False)
        print("Success when transforming times.")
    else:
        print("Error when recovering times.")