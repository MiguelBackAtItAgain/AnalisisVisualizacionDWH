from util import config as cf

def load_customers(stg_db_context, sor_db_context, load_iteration):
    customers = cf.get_table_regs(table_name='CUSTOMERS_TRANSF', cols=['CUST_ID', 'CUST_FIRST_NAME', 'CUST_LAST_NAME', 'CUST_GENDER',
    'CUST_YEAR_OF_BIRTH', 'CUST_MARITAL_STATUS', 'CUST_STREET_ADDRESS', 'CUST_POSTAL_CODE', 'CUST_CITY', 'CUST_STATE_PROVINCE',
    'COUNTRY_ID', 'CUST_MAIN_PHONE_INTEGER', 'CUST_INCOME_LEVEL', 'CUST_CREDIT_LIMIT', 'CUST_EMAIL'],
    iteration=load_iteration, db_context= stg_db_context)
    customers_countries = cf.get_keys(table_name='COUNTRIES', cols=['COUNTRY_ID'], db_context=sor_db_context)
    customers['COUNTRY_ID'] = customers['COUNTRY_ID'].apply(lambda x: customers_countries[x])
    cf.upsert(table_name='CUSTOMERS', cols=['CUST_ID'], df=customers, db_context=sor_db_context)