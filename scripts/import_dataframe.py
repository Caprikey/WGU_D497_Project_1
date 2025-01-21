# Importing Modules
import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath(".."))

# Now you can use absolute imports
from d497_helpers import folder_manager as fm, archive_module, checkpoint_helper as CheckPoint, database_helper as db_tool, config


# Pandas
import pandas as pd

# Numpy
import numpy as np

def import_dataframe(data_source, data_status, file_name, dtypes=None):
    """
    Reads and cleans data from a specified source, returning two DataFrames (CSV and Pickle).
    
    Args:
        data_source (str): The source of the data ("ufo_data", "cdc_data", or "fips_data").
        data_status (str): The current status of the data ("raw", "processed", "cleaned").
        file_name (str): The base name of the file (without extension).
        dtypes (dict, optional): Dictionary specifying the data types for the columns. Defaults are provided based on the data source.
        
    Returns:
        tuple: A tuple containing the CSV DataFrame and the Pickle DataFrame.
    """
    # Define default dtype dictionaries
    default_dtypes = {
        "ufo_data": {
            "report_id": "object",
            "year_code": "object",
            "month_code": "object",
            "state_fipcode": "object",
            "county_fipcode": "object",
            "city_fipcode": "object",
            "fips_five": "object",
            "fips_nine": "object",
        },
        "cdc_data": {
            "year_code": "object",
            "month_code": "object",
            "state_code": "object",
            "county_code": "object",
            "births": "int",
        },
        "fips_data": {
            "state_fipcode": "object",
            "county_fipcode": "object",
            "city_fipcode": "object",
            "fips_five": "object",
            "fips_nine": "object",
        },
    }

    # Dynamically determine folder path using getattr
    folder_path_attr = f"global_{data_status}_{data_source}_folder_path"
    
    try:
        folder_path = getattr(config, folder_path_attr)
    except AttributeError:
        raise ValueError(f"Invalid combination of data_status and data_source: {folder_path_attr} not found in config.")

    # Determine dtype dictionary
    csv_dtypes = dtypes or default_dtypes.get(data_source)
    if not csv_dtypes:
        raise ValueError(f"Invalid data_source: {data_source}")

    # Construct file paths
    file_path_csv = f"{folder_path}/{file_name}.csv"
    file_path_pickle = f"{folder_path}/{file_name}.pkl"

    # Read CSV and Pickle files
    import_main_df_csv = pd.read_csv(file_path_csv, sep=",", dtype=csv_dtypes)
    import_main_df_pickle = pd.read_pickle(file_path_pickle)

    return import_main_df_csv, import_main_df_pickle