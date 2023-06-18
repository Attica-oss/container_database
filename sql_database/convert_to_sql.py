import sys
import pandas as pd
import sqlalchemy
from sql_database.config import CONNECTION_STRING

sys.path.append('sql_database/config')

class DataFrameLoader:
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    def load_dataframe(self, dataframe, table_name):
        engine = sqlalchemy.create_engine(self.connection_string)
        dataframe.to_sql(table_name, engine, if_exists='replace', index=False)

# Usage example
if __name__ == '__main__':
    # Create an instance of DataFrameLoader with the connection string from the config file
    loader = DataFrameLoader(CONNECTION_STRING)
  
    # Load a DataFrame into an SQL table
    df = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']})
    loader.load_dataframe(df, 'your_table_name')
