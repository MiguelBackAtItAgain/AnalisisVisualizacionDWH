import pandas as pd

def transform_countries(stg_db_context, transf_iteration):
    extracted_countries = pd.read_sql(sql='countries', con=stg_db_context)
    if not extracted_countries.empty:
        extracted_countries.loc[:,["COUNTRY_ID", "COUNTRY_REGION_ID"]] = extracted_countries.loc[:,["COUNTRY_ID", "COUNTRY_REGION_ID"]].astype(int)
        extracted_countries['ETL_PROCESS_ID'] = transf_iteration
        extracted_countries.to_sql(name='COUNTRIES_TRANSF', con=stg_db_context, if_exists='append', index=False)
        print("Success when transforming countries.")
    else:
        print("Error when recovering countries.")