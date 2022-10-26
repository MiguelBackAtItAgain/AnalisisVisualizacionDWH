from . import (channels as cnn, countries as cnt, customers as cst, products as prd, 
                promotions as prm, sales as sls, times as tms)

def truncate(db_context):
    sls.truncate(db_context)
    cnn.truncate(db_context)
    cnt.truncate(db_context)
    cst.truncate(db_context)
    prd.truncate(db_context)
    prm.truncate(db_context)
    tms.truncate(db_context)

def extract(db_context):
    sls.run(db_context)
    cnn.run(db_context)
    cnt.run(db_context)
    cst.run(db_context)
    prd.run(db_context)
    prm.run(db_context)
    tms.run(db_context)
