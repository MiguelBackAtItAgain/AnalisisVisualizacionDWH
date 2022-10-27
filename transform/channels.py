import pandas as pd

def transform_channels(stg_db_context, transf_iteration):
    extracted_channels = pd.read_sql(sql='channels', con=stg_db_context)
    if not extracted_channels.empty:
        extracted_channels.loc[:,['CHANNEL_ID', 'CHANNEL_CLASS_ID']] = extracted_channels.loc[:,['CHANNEL_ID', 'CHANNEL_CLASS_ID']].astype(int)
        extracted_channels['ETL_PROCESS_ID'] = transf_iteration
        extracted_channels.to_sql(name='CHANNELS_TRANSF', con=stg_db_context, if_exists='append', index=False)
        print("Success when transforming channels.")
    else:
        print("Error when recovering channels.")
