import pandas as pd

def transform_products(stg_db_context, transf_iteration):
    extracted_products = pd.read_sql(sql='products', con=stg_db_context)
    if not extracted_products.empty:
        extracted_products.loc[:,['PROD_ID', 'PROD_CATEGORY_ID', 'PROD_WEIGHT_CLASS',
        'SUPPLIER_ID']] = extracted_products.loc[:,['PROD_ID', 'PROD_CATEGORY_ID', 'PROD_WEIGHT_CLASS', 'SUPPLIER_ID']].astype(int)
        extracted_products.loc[:,['PROD_LIST_PRICE', 'PROD_MIN_PRICE']] = extracted_products.loc[:,['PROD_LIST_PRICE', 'PROD_MIN_PRICE']].astype(float)
        extracted_products['ETL_PROCESS_ID'] = transf_iteration
        extracted_products.to_sql(name='PRODUCTS_TRANSF', con=stg_db_context, if_exists='append', index=False)
        print("Success when transforming products.")
    else:
        print("Error when recovering products.")
