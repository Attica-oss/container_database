'main file'
from dataschema.excel_schema import ExcelData
import reshape_data.reshape_data as rs
import sql_database.convert_to_sql as sq
from sql_database.config import CONNECTION_STRING


if __name__ == '__main__':

    # Apply the duration_in_days function to the 'date_of_birth' column
    preprocessed_df = rs.apply_function_to_series('test_file',
                                                  'date_of_birth',
                                                  'duration',
                                                  rs.duration_in_days)

    salary_df = ExcelData.get_excel_schema('salary').load_excel()

    # Create an instance of DataFrameLoader with the connection string from the config file
    loader = sq.DataFrameLoader(CONNECTION_STRING)

    # Load a DataFrame into an SQL table
    loader.load_dataframe(preprocessed_df, 'persons')
    loader.load_dataframe(salary_df, 'salary_data')

    # Print the modified DataFrame
    print(salary_df)
