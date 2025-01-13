#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Data Cleaning - Zip Module
### Version 1
#### 12/31/24
#### 17:00


# In[7]:


# Zipfile
import zipfile

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


# In[8]:


global raw_data_base_folder_path

global raw_ufo_data_folder_path
global raw_cdc_natality_data_folder_path
global raw_fips_data_folder_path

global doc_folder_path

global cleaned_data_base_folder_path

global cleaned_ufo_data_folder_path
global cleaned_cdc_natality_data_folder_path
global cleaned_fips_data_folder_path

global archived_data_folder_path 

global files_downloads_folder_path

#global archive_dictionary = {}
archive_dictionary = {}

#global matched_files = []
matched_files = []

global search_pattern
global search_folder
global save_folder
global save_file

global archive_file_path

global delete_flag
global filter_extension_flag
global file_extension_filter


# In[9]:


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


# In[10]:


def find_matched_files(path, pattern, filter_extension_flag=False, file_extension_filter=None):

    search_folder_path = path
    
    search_file_name_pattern_base = pattern

    if filter_extension_flag:
        
        if not file_extension_filter:
            raise ValueError("Extension is required when extension flag is set to True")
        

        normalized_file_extension = f".{file_extension_filter.lstrip('.')}"

        
#         if not path.endswith(normalized_extension):
#             raise ValueError(
#                 f"file_path must end with the specified extension: {normalized_extension}"
#             )  

        search_file_name_pattern_full = search_file_name_pattern_base + "*" + normalized_file_extension

    
    else:

        search_file_name_pattern_full = search_file_name_pattern_base + "*"



    matched_files = glob.glob(search_folder_path + "/" + search_file_name_pattern_full)


    if matched_files:
        matched_files.sort()
        #print(matched_files)
        return matched_files

    else:
        print(f"No Files Found That Match the File Name Pattern {search_file_name_pattern_full} in {search_folder_path}")


# In[11]:


def archive_files(matched_files, archive_name, destination_folder):

    global archive_file_path
    
    if destination_folder == "default":
        destination_save_folder = archived_data_folder_path
    else:
        destination_save_folder = destination_folder
    
    archive_file_name = archive_name + ".zip"

    archive_file_path = destination_save_folder + "/" + archive_file_name
    
    try:
        with zipfile.ZipFile(archive_file_path, 'w') as archive_zip:
                
            for file_path in matched_files:
                    
                file = Path(file_path)
                
                if file.exists():
                    archive_zip.write(file_path, arcname=file_path)
                else:
                    print(f"File not found: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error archiving files: {e}")
        return False


   # with zipfile.ZipFile("directory.zip", mode="r") as archive:
        #archive.printdir()
    


# In[12]:


def delete_files(files_to_delete):
    """
    Deletes the given files.

    Args:
        files_to_delete (list): List of file paths to delete.
    """
    for file_path in files_to_delete:
        try:
            file = Path(file_path)
            if file.exists():
                file.unlink()  # Deletes the file
                print(f"Deleted: {file_path}")
            else:
                print(f"File not found, cannot delete: {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


# In[13]:


def get_archive_details(file_path):

    """
    Prints details of the contents of a zip file.

    Args:
        file_path (str): Path to the zip file.
    """
    # Opening the zip file in READ mode
    
    with zipfile.ZipFile(file_path, 'r') as zip:
        for info in zip.infolist(): 
                print(info.filename) 
                print('\tModified:\t' + str(datetime.datetime(*info.date_time))) 
                print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)') 
                print('\tZIP version:\t' + str(info.create_version)) 
                print('\tCompressed:\t' + str(info.compress_size) + ' bytes') 
                print('\tUncompressed:\t' + str(info.file_size) + ' bytes') 
    


# In[14]:


def main():

    # Initializer Commands

    # Initializes Folder Manager Requirements
    fm.initialize_folder_paths()
    
    
    # Initializes The Folders for This Notebook
    setup_working_directories()
    
    global search_pattern
    global search_folder 
    global save_folder
    global save_file

    global delete_flag 
    global filter_extension_flag
    global file_extension_filter 

    if filter_extension_flag:
         
        if not file_extension_filter:
            
            raise ValueError("extension is required when filter_extension_flag is True.")


    get_search_folder_path = fm.get_folder_path(search_folder)
    get_save_folder_path = fm.get_folder_path(save_folder)
    
    matched_files = find_matched_files(get_search_folder_path, search_pattern, filter_extension_flag, file_extension_filter)
    
    if archive_files(matched_files, save_file, get_save_folder_path):
        print("Files archived successfully.")
        # Delete the original files
        if delete_flag:
            delete_files(matched_files)
    else:
        print("Archiving failed. Files not deleted.")

    results = get_archive_details(archive_file_path)


# In[15]:


def create_archive(set_search_pattern, set_search_folder, set_save_folder, set_save_file, filter_extension=False, filter_by_file_extension=None, delete=True):

    # Initializer Commands

    # Initializes Folder Manager Requirements
    fm.initialize_folder_paths()
    
    
    # Initializes The Folders for This Notebook
    setup_working_directories()
    
    global search_pattern
    global search_folder 
    global save_folder
    global save_file
    global delete_flag
    global filter_extension_flag
    global file_extension_filter

    search_pattern = set_search_pattern
    search_folder = set_search_folder
    save_folder = set_save_folder
    save_file = set_save_file
    filter_extension_flag = filter_extension
    file_extension_filter = filter_by_file_extension
    delete_flag = delete

    main()


# In[19]:


#fm.initialize_folder_paths()
#find_matched_files(fm.get_folder_path("raw_CDC_Natality_Birth_Data"), "Raw_CDC_Natality_Birth_Data", filter_extension_flag=True, file_extension_filter=".txt")


# In[104]:


if __name__ == "__main__":
    
    # Initializer Commands

    # Initializes Folder Manager Requirements
    fm.initialize_folder_paths()
    
    # Initializes Database Engine and Session For SQL
    #db_tool.initialize_engine()
    #db_tool.initialize_session()
    
    # Initializes The Folders for This Notebook
    setup_working_directories()
    
    search_pattern = "ufo_data_main_"
    search_folder = raw_ufo_data_folder_path
    save_folder = archived_data_folder_path
    save_file = "ufo_data_main_data_cleaning_backups_test_2"
    filter_extension_flag = False
    file_extension_filter = ".pkl"
    delete_flag = False
    
    main()

