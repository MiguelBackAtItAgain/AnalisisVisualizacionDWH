from util import config as cf

def load_products(stg_db_context, sor_db_context, load_iteration):
    products = cf.get_table_regs(table_name='PRODUCTS_TRANSF', cols=['PROD_ID', 'PROD_NAME', 'PROD_DESC', 'PROD_CATEGORY',
    'PROD_CATEGORY_ID', 'PROD_CATEGORY_DESC', 'PROD_WEIGHT_CLASS', 'SUPPLIER_ID', 'PROD_STATUS', 'PROD_LIST_PRICE', 'PROD_MIN_PRICE'],
    iteration=load_iteration, db_context= stg_db_context)
    cf.upsert(table_name='PRODUCTS', cols=['PROD_ID'], df=products, db_context=sor_db_context)