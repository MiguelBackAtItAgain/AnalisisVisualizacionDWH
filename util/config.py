from jproperties import Properties

class StorageConfig():
    
    def config_storage():
        config = Properties()
        with open('properties/storage.properties', 'rb') as config_file_for_storage:
            config.load(config_file_for_storage)
        params ={
            'HOST' : config["DB_HOST"].data,
            'SCHEMA' : config["DB_SCHEMA"].data,
            'USER' : config["DB_USER"].data,
            'PORT' : config["DB_PORT"].data,
            'TYPE' : config["DB_TYPE"].data,
            'PSWD' : config["DB_PSWD"].data
        }
        return params

class SorConfig():
    
    def config_sor():
        config = Properties()
        with open('properties/sor.properties', 'rb') as config_file_for_sor:
            config.load(config_file_for_sor)
        params ={
            'HOST' : config["DB_HOST"].data,
            'SCHEMA' : config["DB_SCHEMA"].data,
            'USER' : config["DB_USER"].data,
            'PORT' : config["DB_PORT"].data,
            'TYPE' : config["DB_TYPE"].data,
            'PSWD' : config["DB_PSWD"].data
        }
        return params

