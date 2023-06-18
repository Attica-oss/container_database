'ExcelShema: We use this to create Excel objects'

from dataclasses import dataclass
from pathlib import Path
import json

import pandas as pd


@dataclass
class ExcelData:
    """
    Represents Excel data configuration.

    Attributes:
        path (Path): The path to the directory where the Excel file is located.
        file_name (str): The name of the Excel file.
        sheet_name (str): The name of the sheet in the Excel file.
        column_names (list): A list of column names in the sheet.
    """

    path: Path
    file_name: str
    sheet_name: str
    column_details: dict[str,type]

    @staticmethod
    def get_excel_schema(config_name: str) -> 'ExcelData':
        """
        Create an instance of ExcelData using the configuration from the JSON file.

        Args:
            config_name (str): The name of the configuration to use.

        Returns:
            ExcelData: The instantiated ExcelData object.
        """
        # Read the configuration file
        with open('dataschema/excel_data.json', 'r', encoding='utf-8') as config_file:
            config_data = json.load(config_file)

        # Access and process the selected Excel data
        excel_data = config_data["excel_data"]
        selected_data = next((data for data in excel_data if data["name"] == config_name), None)

        if selected_data is None:
            raise ValueError(f"No configuration found for the name '{config_name}'.")

        path = Path(selected_data["path"])
        file_name = selected_data["file_name"]
        sheet_name = selected_data["sheet_name"]
        column_details = selected_data["column_details"]

        return ExcelData(path=path,
                        file_name=file_name,
                        sheet_name=sheet_name,
                        column_details=column_details)

    def load_excel(self) -> pd.DataFrame:
        """
        Load the selected Excel file, select specific columns,
        rename column names, and return the preprocessed DataFrame.

        Returns:
            pd.DataFrame: The preprocessed DataFrame.
        """
        excel_file_path = self.path / self.file_name
        excel_df = pd.read_excel(excel_file_path, sheet_name=self.sheet_name)

        # Select specific columns
        column_names = list(self.column_details.keys())
        excel_df = excel_df[column_names]

        # Convert column values to desired data types

        for column, data_type in self.column_details.items():
            if column in excel_df:
                if isinstance(data_type, dict) and data_type.get("data_type") == "time":
                    format_str = data_type.get("format", "%H:%M:%S")
                    excel_df[column] = pd.to_datetime(excel_df[column],
                                                      format=format_str,
                                                      errors='coerce').apply(
                        lambda x: x.time() if not pd.isnull(x) else None)
                elif data_type == "category":
                    excel_df[column] = excel_df[column].astype("category")


        # Rename column names to remove spaces and make them lowercase
        excel_df = excel_df.rename(columns=lambda x: x.replace(" ", "_").lower())

        return excel_df