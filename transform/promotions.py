import pandas as pd
import datetime as dt

def transform_promotions(stg_db_context, transf_iteration):
    extracted_promotions = pd.read_sql(sql='promotions', con=stg_db_context)
    if not extracted_promotions.empty:
        extracted_promotions['PROMO_ID'] = extracted_promotions['PROMO_ID'].astype(int)
        extracted_promotions['PROMO_COST'] = extracted_promotions['PROMO_COST'].astype(float)
        extracted_promotions['PROMO_BEGIN_DATE'] = extracted_promotions['PROMO_BEGIN_DATE'].apply(lambda x : dt.datetime.strptime(x, '%d-%b-%y'))
        extracted_promotions['PROMO_END_DATE'] = extracted_promotions['PROMO_END_DATE'].apply(lambda x : dt.datetime.strptime(x, '%d-%b-%y'))
        extracted_promotions['ETL_PROCESS_ID'] = transf_iteration
        extracted_promotions.to_sql(name='PROMOTIONS_TRANSF', con=stg_db_context, if_exists='append', index=False)
        print("Success when transforming promotions.")
    else:
        print("Error when recovering promotions.")