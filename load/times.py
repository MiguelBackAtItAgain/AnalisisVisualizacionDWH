from util import config as cf

def load_times(stg_db_context, sor_db_context, load_iteration):
    times = cf.get_table_regs(table_name='TIMES_TRANSF', cols=['TIME_ID', 'DAY_NAME', 'DAY_INTEGER_IN_WEEK', 'DAY_INTEGER_IN_MONTH',
    'CALENDAR_WEEK_INTEGER', 'CALENDAR_MONTH_INTEGER','CALENDAR_MONTH_DESC', 'END_OF_CAL_MONTH', 'CALENDAR_MONTH_NAME',
    'CALENDAR_QUARTER_DESC', 'CALENDAR_YEAR'], iteration=load_iteration, db_context= stg_db_context)
    cf.upsert(table_name='TIMES', cols=['TIME_ID'], df=times, db_context=sor_db_context)