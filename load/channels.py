from util import config as cf

def load_channels(stg_db_context, sor_db_context, load_iteration):
    channels = cf.get_table_regs(table_name='CHANNELS_TRANSF', cols=['CHANNEL_ID', 'CHANNEL_DESC', 'CHANNEL_CLASS', 'CHANNEL_CLASS_ID'],
    iteration=load_iteration, db_context= stg_db_context)
    cf.upsert(table_name='CHANNELS', cols=['CHANNEL_ID'], df=channels, db_context=sor_db_context)