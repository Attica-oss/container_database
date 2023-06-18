'covert_to_sql.py'

import sys
import sqlalchemy

sys.path.append('sql_database/config')

class DataFrameLoader:
    ''' Load data'''
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def load_dataframe(self, dataframe, table_name):
        'creare engine'
        engine = sqlalchemy.create_engine(self.connection_string)
        dataframe.to_sql(table_name, engine, if_exists='replace', index=False)
