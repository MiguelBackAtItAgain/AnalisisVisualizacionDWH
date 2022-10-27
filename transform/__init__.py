from . import (channels as cnn, countries as cnt, customers as cst, products as prd, 
                promotions as prm, sales as sls, times as tms)

def transform_channels(stg_db_context, transf_iteration):
    cnn.transform_channels(stg_db_context, transf_iteration)

def transform_countries(stg_db_context, transf_iteration):
    cnt.transform_countries(stg_db_context, transf_iteration)

def transform_customers(stg_db_context, transf_iteration):
    cst.transform_customers(stg_db_context, transf_iteration)

def transform_products(stg_db_context, transf_iteration):
    prd.transform_products(stg_db_context, transf_iteration)   

def transform_promotions(stg_db_context, transf_iteration):
    prm.transform_promotions(stg_db_context, transf_iteration)

def transform_times(stg_db_context, transf_iteration):
    tms.transform_times(stg_db_context, transf_iteration)

def transform_sales(stg_db_context, transf_iteration):
    sls.transform_sales(stg_db_context, transf_iteration)