from util import config as cf

def load_countries(stg_db_context, sor_db_context, load_iteration):
    countries = cf.get_table_regs(table_name='COUNTRIES_TRANSF', cols=['COUNTRY_ID', 'COUNTRY_NAME', 'COUNTRY_REGION', 'COUNTRY_REGION_ID'],
    iteration=load_iteration, db_context= stg_db_context)
    cf.upsert(table_name='COUNTRIES', cols=['COUNTRY_ID'], df=countries, db_context=sor_db_context)