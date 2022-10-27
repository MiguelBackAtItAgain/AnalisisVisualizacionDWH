from util import config as cf

def load_promotions(stg_db_context, sor_db_context, load_iteration):
    promotions = cf.get_table_regs(table_name='PROMOTIONS_TRANSF', cols=['PROMO_ID', 'PROMO_NAME', 'PROMO_COST', 'PROMO_BEGIN_DATE', 'PROMO_END_DATE'],
    iteration=load_iteration, db_context= stg_db_context)
    cf.upsert(table_name='PROMOTIONS', cols=['PROMO_ID'], df=promotions, db_context=sor_db_context)