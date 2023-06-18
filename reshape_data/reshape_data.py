
'reshape_data.py'
import sys
from datetime import datetime
import pandas as pd
from date_functions.date_functions import CustomDate
from dataschema.excel_schema import ExcelData

sys.path.append('/home/garry/container_database/dataschema')
sys.path.append('/home/garry/container_database/date_functions')


# Date Functions

def duration_in_days(date: datetime) -> int:
    """
    Process a date and returns the duration in days.

    Args:
        date (datetime): The date to process.

    Returns:
        int: the duration from the supplied date to today's date.
    """
    custom_date = CustomDate(date.year, date.month, date.day)
    duration = custom_date.duration()
    return duration


def format_date(date: datetime) -> str:
    """
    Process a date and returns the formatted date as Day_name with date/month.

    Args:
        date (datetime): The date to process.

    Returns:
        str: A string containing the formatted date.
    """
    custom_date = CustomDate(date.year, date.month, date.day)
    formatted_date = custom_date.formatted_date()
    return formatted_date





def apply_function_to_series(file_name: str,
                             column_name: str,
                             new_column_name: str,
                             function: callable) -> pd.DataFrame:
    """
    Apply a function to a specific column in a DataFrame.

    Args:
        file_name (str): The name of the Excel file.
        column_name (str): The name of the column to apply the function to.
        function (callable): The function to apply to the column.

    Returns:
        pd.DataFrame: The modified DataFrame.
    """

    excel_data = ExcelData.get_excel_schema(file_name)
    preprocessed_df = excel_data.load_excel()  # Load the Excel data into the object

    # Apply the function to the specified column
    preprocessed_df[new_column_name] = preprocessed_df[column_name].apply(function)

    return preprocessed_df  # Return the modified DataFrame
