#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Checkpoint Module
# Version 1
# 1/3/25
# 17:45


# In[2]:


# Inspect
import inspect

# Pandas 
import pandas as pd

# Numpy
import numpy as np

# RegularExpression for string matching
import re

# GLOB 
import glob 

# Pathlib 
from pathlib import Path

# NB Importer
import nbimporter

# Date Time
import datetime 

# My Modules

## Folder Manager
#import folder_manager as fm
from d497_helpers import folder_manager as fm

## Database Helper
#import database_helper as db_tool
from d497_helpers import database_helper as db_tool

# In[3]:


global base_data_folder_path

global doc_folder_path
global archived_data_folder_path

global raw_data_base_folder_path
global raw_ufo_data_folder_path
global raw_cdc_natality_data_folder_path
global raw_fips_data_folder_path

global cleaned_data_base_folder_path
global cleaned_ufo_data_folder_path
global cleaned_cdc_natality_data_folder_path
global cleaned_fips_data_folder_path


global save_folder_path
global save_file_name
global dataframe_to_save

 


# In[5]:


def setup_working_directories():

    global base_data_folder_path

    global doc_folder_path
    global archived_data_folder_path
    
    global raw_data_base_folder_path
    global raw_ufo_data_folder_path
    global raw_cdc_natality_data_folder_path
    global raw_fips_data_folder_path

    global cleaned_data_base_folder_path
    global cleaned_ufo_data_folder_path
    global cleaned_cdc_natality_data_folder_path
    global cleaned_fips_data_folder_path

    #### #### #### ####
    
    fm.initialize_folder_paths()

    ####

    doc_folder_path = fm.get_folder_path("raw_FIPS_Data")
    
    ####
    
    base_data_folder_path = fm.get_folder_path("data_folder")

    ####

    files_downloads_folder_path = fm.get_folder_path("files_downloads")
    
    #### 
    
    raw_data_base_folder_path = fm.get_folder_path("raw_files")
    
    raw_ufo_data_folder_path = fm.get_folder_path("raw_UFO_Data")
    
    raw_cdc_natality_data_folder_path = fm.get_folder_path("raw_CDC_Natality_Birth_Data")
    
    raw_fips_data_folder_path = fm.get_folder_path("raw_FIPS_Data")

    ####
    
    cleaned_data_base_folder_path = fm.get_folder_path("cleaned_data")
    
    cleaned_ufo_data_folder_path = fm.get_folder_path("cleaned_UFO_Data")

    cleaned_cdc_natality_data_folder_path = fm.get_folder_path("cleaned_CDC_Natality_Birth_Data")

    cleaned_fips_data_folder_path = fm.get_folder_path(" cleaned_FIPS_Data")

    ####

    archived_data_folder_path = fm.get_folder_path("archived_data_folder")


# In[6]:


def write_checkpoints(save_path, save_name, dataframe):

    # Set Save Folder Path 
    #save_folder_path = save_path
    save_folder_path_csv = fm.get_folder_path(save_path)
    #print(save_folder_path_csv)

    save_folder_path_pickle = fm.get_folder_path(save_path)
    #save_folder_path = fm.get_folder_path(save_path)
    #print(save_folder_path_pickle)
    
    # Set Save File Name For CSV Export 
    save_file_name_csv = save_name
    #print(save_file_name_csv)

    save_file_name_pickle = save_name
    #print(save_file_name_pickle)

    # Create Export File Path For CSV
    save_file_path_csv = Path(save_folder_path_csv + "/" + save_file_name_csv + ".csv")
    #print(save_file_path_csv)
    
    # Create Export File Path For Pickle
    save_file_path_pickle = Path(save_folder_path_pickle + "/" + save_file_name_pickle + ".pkl")
    #print(save_file_path_pickle)
    
    try:      
        # Export CSV
        dataframe.to_csv(save_file_path_csv, sep=",", index=False)
        #print(f"Dataframe was successfully exported to CSV, {save_file_path}")
        
        # Export Pickle
        dataframe.to_pickle(save_file_path_pickle)
        #print(f"Dataframe was successfully exported to CSV, {save_file_path_pickle}")
        #print("Check Point Successful")

        
        
    except:
        
        
        print(f"Save Foler Path: {save_folder_path}")
        print(f"Save_File_Name: {save_file_name}")
        print(f"Save_Save_Path_CSV: {save_file_path_csv}")
        print(f"Save_Save_Path_Pickle: {save_file_path_pickle}")
        print("Checkpoint Failed")


# In[7]:


def main():

    global save_folder_path 
    global save_file_name
    global dataframe_to_save
    
    # Initializes Folder Manager Requirements
    fm.initialize_folder_paths()
    
    # Initializes Database Engine and Session For SQL
    db_tool.initialize_engine()
    db_tool.initialize_session()
    
    # Initializes The Folders for This Notebook
    setup_working_directories()
    
    
    write_checkpoints(save_folder_path, save_file_name, dataframe_to_save)

    


# In[8]:


def create_checkpoint(save_path, save_name, dataframe):

    global save_folder_path 
    global save_file_name
    global dataframe_to_save

    save_folder_path = save_path
    save_file_name = save_name
    dataframe_to_save = dataframe

    main()
    


# In[9]:


if __name__ == "main":

    save_folder_path = ""

    #save_folder_path = fm.get_folder_path("")
    
    # Set Save File Name 
    save_file_name = ""

    # DataFrame 
    dataframe_to_save = None
    

    main()

