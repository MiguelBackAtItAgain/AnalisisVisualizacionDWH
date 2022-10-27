from util import config as cf

def load_sales(stg_db_context, sor_db_context, load_iteration):
    sales = cf.get_table_regs(table_name='SALES_TRANSF', cols=['PROD_ID', 'CUST_ID', 'TIME_ID',
    'CHANNEL_ID', 'PROMO_ID', 'QUANTITY_SOLD', 'AMOUNT_SOLD'], iteration=load_iteration, db_context= stg_db_context)
    prod_key = cf.get_keys(table_name='PRODUCTS', cols=['PROD_ID'], db_context=sor_db_context)
    cust_key = cf.get_keys(table_name='CUSTOMERS', cols=['CUST_ID'], db_context=sor_db_context)
    times_key = cf.get_keys(table_name='TIMES', cols=['TIME_ID'], db_context=sor_db_context)
    cnn_key = cf.get_keys(table_name='CHANNELS', cols=['CHANNEL_ID'], db_context=sor_db_context)
    prm_key = cf.get_keys(table_name='PROMOTIONS', cols=['PROMO_ID'], db_context=sor_db_context)

    sales['PROD_ID'] = sales['PROD_ID'].apply(lambda x: prod_key[x])
    sales['CUST_ID'] = sales['CUST_ID'].apply(lambda x: cust_key[x])
    sales['TIME_ID'] = sales['TIME_ID'].apply(lambda x: times_key[x])
    sales['CHANNEL_ID'] = sales['CHANNEL_ID'].apply(lambda x: cnn_key[x])
    sales['PROMO_ID'] = sales['PROMO_ID'].apply(lambda x: prm_key[x])

    cf.upsert(table_name='SALES', cols=['PROD_ID', 'CUST_ID', 'TIME_ID', 'CHANNEL_ID', 'PROMO_ID'], df=sales, db_context=sor_db_context)