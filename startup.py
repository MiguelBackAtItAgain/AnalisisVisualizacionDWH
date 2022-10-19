from util.config import StorageConfig as sc
from util.db_connection import Db_Connection
from extract import extract, truncate

db_context = Db_Connection(
    'mysql', sc.config_storage().get('HOST'), sc.config_storage().get('PORT'), sc.config_storage().get('USER'), 
    sc.config_storage().get('PSWD'), sc.config_storage().get('USER')
)

