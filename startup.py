from util.config import StorageConfig as stc
from util.config import SorConfig as soc

from util.db_connection import Db_Connection
from extract import extract, truncate
from load import *
from transform import *

stg_db_context = Db_Connection(
    'mysql', stc.config_storage().get('HOST'), stc.config_storage().get('PORT'), stc.config_storage().get('USER'), 
    stc.config_storage().get('PSWD'), stc.config_storage().get('SCHEMA')
    ).start()

sor_db_context = Db_Connection(
    'mysql', soc.config_sor().get('HOST'), soc.config_sor().get('PORT'), soc.config_sor().get('USER'), 
     soc.config_sor().get('PSWD'), soc.config_sor().get('SCHEMA')
    ).start()

def transform_stg_data(stg_db_context, transf_iteration):
    transform_channels(stg_db_context, transf_iteration)
    transform_countries(stg_db_context, transf_iteration)
    transform_customers(stg_db_context, transf_iteration)
    transform_products(stg_db_context, transf_iteration)
    transform_promotions(stg_db_context, transf_iteration)
    transform_times(stg_db_context, transf_iteration)
    transform_sales(stg_db_context, transf_iteration)

def load_sor_data(stg_db_context, sor_db_context, transf_iteration):
    load_channels(stg_db_context, sor_db_context, transf_iteration)
    load_countries(stg_db_context, sor_db_context, transf_iteration)
    load_customers(stg_db_context, sor_db_context, transf_iteration)
    load_products(stg_db_context, sor_db_context, transf_iteration)
    load_promotions(stg_db_context, sor_db_context, transf_iteration)
    load_times(stg_db_context, sor_db_context, transf_iteration)
    load_sales(stg_db_context, sor_db_context, transf_iteration)

with stg_db_context.begin():
    truncate(stg_db_context)
    extract(stg_db_context)
    transf_iteration = stg_db_context.execute('INSERT INTO TRANSFORM_INTERATION VALUES ()').lastrowid
    transform_stg_data(stg_db_context, transf_iteration)
    load_sor_data(stg_db_context, sor_db_context, transf_iteration)