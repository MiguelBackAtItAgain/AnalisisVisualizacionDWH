import pandas as pd

def transform_customers(stg_db_context, transf_iteration):
    extracted_customers = pd.read_sql(sql='customers', con=stg_db_context)
    if not extracted_customers.empty:
        extracted_customers.loc[:,["CUST_ID","COUNTRY_ID","CUST_CREDIT_LIMIT"]] = extracted_customers.loc[:,["CUST_ID","COUNTRY_ID","CUST_CREDIT_LIMIT"]].astype(int)
        extracted_customers['ETL_PROCESS_ID'] = transf_iteration
        extracted_customers.to_sql(name='CUSTOMERS_TRANSF', con=stg_db_context, if_exists='append', index=False)
        print("Success when transforming customers.")
    else:
        print("Error when recovering customers.")