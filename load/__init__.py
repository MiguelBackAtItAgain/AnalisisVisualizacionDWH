from . import (channels as cnn, countries as cnt, customers as cst, products as prd, 
                promotions as prm, sales as sls, times as tms)

def load_channels(stg_db_context, sor_db_context, transf_iteration):
    cnn.load_channels(stg_db_context, sor_db_context, transf_iteration)

def load_countries(stg_db_context, sor_db_context, transf_iteration):
    cnt.load_countries(stg_db_context, sor_db_context, transf_iteration)

def load_customers(stg_db_context, sor_db_context, transf_iteration):
    cst.load_customers(stg_db_context, sor_db_context, transf_iteration)

def load_products(stg_db_context, sor_db_context, transf_iteration):
    prd.load_products(stg_db_context, sor_db_context, transf_iteration)   

def load_promotions(stg_db_context, sor_db_context, transf_iteration):
    prm.load_promotions(stg_db_context, sor_db_context, transf_iteration)

def load_times(stg_db_context, sor_db_context, transf_iteration):
    tms.load_times(stg_db_context, sor_db_context, transf_iteration)

def load_sales(stg_db_context, sor_db_context, transf_iteration):
    sls.load_sales(stg_db_context, sor_db_context, transf_iteration)
