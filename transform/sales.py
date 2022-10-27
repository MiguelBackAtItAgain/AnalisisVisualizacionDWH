import pandas as pd
import datetime as dt

def transform_sales(stg_db_context, transf_iteration):
    extracted_sales = pd.read_sql(sql='sales', con=stg_db_context)
    if not extracted_sales.empty:
        extracted_sales.loc[:,['PROD_ID', 'CUST_ID', 'CHANNEL_ID', 'PROMO_ID']] = extracted_sales.loc[:,['PROD_ID', 'CUST_ID', 'CHANNEL_ID', 'PROMO_ID']].astype(int)
        extracted_sales.loc[:,['QUANTITY_SOLD', 'AMOUNT_SOLD']] = extracted_sales.loc[:,['QUANTITY_SOLD', 'AMOUNT_SOLD']].astype(float)
        extracted_sales['TIME_ID'] = extracted_sales['TIME_ID'].apply(lambda x : dt.datetime.strptime(x, '%d-%b-%y'))
        extracted_sales['ETL_PROCESS_ID'] = transf_iteration
        extracted_sales.to_sql('SALES_TRANSF', con=stg_db_context, if_exists='append', index=False)
        print("Success when transforming sales.")
    else:
        print("Error when recovering sales.")
