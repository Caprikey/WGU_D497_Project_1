#from pathlib import Path

from d497_helpers import folder_manager

import json



try:
    with open(".json", "r") as file:
        config_data = json.load(file)

        global_doc_folder_path = config_data.get("doc")
        global_cdc_footer_folder_path = config_data.get("cdc_footer")
        global_readme_folder_path = config_data.get("read_me")
        global_scripts_folder_path = config_data.get("scripts")
        global_notebooks_folder_path = config_data.get("notebooks")
        global_bin_folder_path = config_data.get("bin_folder")
        global_results_folder_path = config_data.get("results")
        global_data_folder_path = config_data.get("data")
        global_archived_data_folder_path = config_data.get("archived_data")
        global_processed_data_folder_path = config_data.get("processed_data")
        global_raw_data_folder_path = config_data.get("raw_data")
        global_cleaned_data_folder_path = config_data.get("cleaned_data")
        global_database_folder_path = config_data.get("db")
        global_raw_ufo_data_folder_path = config_data.get("raw_ufo_data")
        global_raw_cdc_data_folder_path = config_data.get("raw_cdc_data")
        global_raw_fips_data_folder_path = config_data.get("raw_fips_data")
        global_processed_ufo_data_folder_path = config_data.get("processed_ufo_data")
        global_processed_cdc_data_folder_path = config_data.get("processed_cdc_data")
        global_processed_fips_data_folder_path = config_data.get("processed_fips_data")
        global_cleaned_ufo_data_folder_path = config_data.get("cleaned_ufo_data")
        global_cleaned_cdc_data_folder_path = config_data.get("cleaned_cdc_data")
        global_cleaned_fips_data_folder_path = config_data.get("cleaned_fips_data")
        global_archived_ufo_data_folder_path = config_data.get("archived_ufo_data")
        global_archived_cdc_data_folder_path = config_data.get("archived_cdc_data")
        global_archived_fips_data_folder_path = config_data.get("archived_fips_data")
        
except FileNotFoundError:
    global_doc_folder_path = folder_manager.get_folder_path("doc")
    global_cdc_footer_folder_path = folder_manager.get_folder_path("cdc_footer")
    global_readme_folder_path = folder_manager.get_folder_path("read_me")
    global_scripts_folder_path = folder_manager.get_folder_path("scripts")
    global_notebooks_folder_path = folder_manager.get_folder_path("notebooks")
    global_bin_folder_path = folder_manager.get_folder_path("bin")
    global_results_folder_path = folder_manager.get_folder_path("results")
    global_data_folder_path = folder_manager.get_folder_path("data")
    global_archived_data_folder_path = folder_manager.get_folder_path("archived_data")
    global_processed_data_folder_path = folder_manager.get_folder_path("processed_dataa")
    global_raw_data_folder_path = folder_manager.get_folder_path("raw_data")
    global_cleaned_data_folder_path = folder_manager.get_folder_path("cleaned_data")
    global_database_folder_path = folder_manager.get_folder_path("db")
    global_raw_ufo_data_folder_path = folder_manager.get_folder_path("raw_ufo_data")
    global_raw_cdc_data_folder_path = folder_manager.get_folder_path("raw_cdc_data")
    global_raw_fips_data_folder_path = folder_manager.get_folder_path("raw_fips_data")
    global_processed_ufo_data_folder_path = folder_manager.get_folder_path("processed_ufo_data")
    global_processed_cdc_data_folder_path = folder_manager.get_folder_path("processed_cdc_data")
    global_processed_fips_data_folder_path = folder_manager.get_folder_path("processed_fips_data")
    global_cleaned_ufo_data_folder_path = folder_manager.get_folder_path("cleaned_ufo_data")
    global_cleaned_cdc_data_folder_path = folder_manager.get_folder_path("cleaned_cdc_data")
    global_cleaned_fips_data_folder_path = folder_manager.get_folder_path("cleaned_fips_data")
    global_archived_ufo_data_folder_path = folder_manager.get_folder_path("archived_ufo_data")
    global_archived_cdc_data_folder_path = folder_manager.get_folder_path("archived_cdc_data")
    global_archived_fips_data_folder_path = folder_manager.get_folder_path("archived_fips_data")


global_dot_api_key = "G9y46iRQiv4jix5v8fCATdd2B"
