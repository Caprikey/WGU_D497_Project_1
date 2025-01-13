#!/usr/bin/env python
# coding: utf-8

# In[92]:


# Helper Module - Folder Manager
# Version 14
## 1/12/25
## 16:30


# In[93]:


# Import Json
import json

# Import PathLib
from pathlib import Path


# In[94]:


def initialize_folder_paths():
    
    # Defining the global variable inside the function
    global folder_path_file
    global folder_path_subdirectory
    global base_folder_path
    
    current_folder = Path.cwd()

    # If running from the base folder. 
    if (current_folder / "scripts").exists() and (current_folder / "data").exists() and (current_folder / "notebooks").exists():
        folder_path_subdirectory = "data"
        base_folder_path = "."
    # If running from the scripts folder
    elif (current_folder / "../data").exists() and (current_folder / "../notebooks").exists():
        folder_path_subdirectory = "../data"
        base_folder_path = ".."
    # If running from the notebooks folder
    elif (current_folder / "../data").exists() and (current_folder / "../scripts").exists():
        folder_path_subdirectory = "../data"
        base_folder_path = ".."
    else:
        print("The 'data' folder does not exist. Assuming first-time initialization.")
        folder_path_subdirectory = "data"
        base_folder_path = "."
        
        # Create the data folder in the base path
        Path(base_folder_path).mkdir(parents=True, exist_ok=True)
        Path(base_folder_path, "data").mkdir(parents=True, exist_ok=True)
        Path(base_folder_path, "notebooks").mkdir(parents=True, exist_ok=True)
        Path(base_folder_path, "scripts").mkdir(parents=True, exist_ok=True)
        print(f"Created 'data' folder at {Path(base_folder_path).resolve()}")
        
    folder_path_file = "folder_paths.json"


# In[95]:


def create_base_folder(base_folder_path: str, base_folder_name: str) -> Path:
    
    """Creates the base downloads folder."""
    
    base_folder_path = Path(base_folder_path) / base_folder_name
    base_folder_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Base Data Folder '{base_folder_path.name}' created successfully at '{base_folder_path}'")
    
    return base_folder_path.resolve()


# In[96]:


def create_subfolder(parent_path: Path, subfolder_name: str) -> Path:
    
    """Creates a subfolder inside the given parent path."""
    
    subfolder_path = parent_path / subfolder_name
    subfolder_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Subfolder '{subfolder_path.name}' created successfully inside '{parent_path}'")
    
    return subfolder_path.resolve()


# In[97]:


def get_all_folder_paths(base_folder_path: str,
                         data_folder_name: str,
                         archived_data_folder_name: str,
                         scripts_folder_name: str,
                         notebooks_folder_name: str, 
                         bin_folder_name: str,
                         doc_folder_name: str,
                         cdc_footer_folder_name: str,
                         readme_folder_name: str,
                         results_folder_name: str,
                         raw_data_folder_name:str,
                         processed_data_folder_name:str,
                         cleaned_data_folder_name:str,
                         database_folder_name:str,
                         ufo_data_folder_name: str, 
                         cdc_data_folder_name: str, 
                         fips_data_folder_name: str) -> dict:
    """
    Creates all required folders and returns a dictionary with their absolute paths.
    """
    #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
    
    doc_folder_path = create_base_folder(base_folder_path, doc_folder_name)
    
    #### #### 

    cdc_footer_folder_path = create_subfolder(doc_folder_path, cdc_footer_folder_name)

    #### #### 

    readme_folder_path = create_subfolder(doc_folder_path, readme_folder_name)
    
    #### #### #### #### 

    scripts_folder_path = create_base_folder(base_folder_path, scripts_folder_name)

    #### #### 
    
    notebooks_folder_path = create_base_folder(base_folder_path, notebooks_folder_name)

    #### #### 

    bin_folder_path = create_base_folder(base_folder_path, bin_folder_name)

    #### ####   
    
    results_folder_path = create_base_folder(base_folder_path, results_folder_name)

    #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
    
    data_folder_path = create_base_folder(base_folder_path, data_folder_name)
    
    #### #### #### #### #### #### #### #### 

    archived_data_folder_path = create_subfolder(data_folder_path, archived_data_folder_name)

    #### #### #### #### 

    raw_data_folder_path = create_subfolder(data_folder_path, raw_data_folder_name)

    #### #### 
    
    raw_ufo_data_folder_path = create_subfolder(raw_data_folder_path, ufo_data_folder_name)
    raw_cdc_data_folder_path = create_subfolder(raw_data_folder_path, cdc_data_folder_name)
    raw_fips_data_folder_path = create_subfolder(raw_data_folder_path, fips_data_folder_name)

    #### #### #### #### 

    processed_data_folder_path = create_subfolder(data_folder_path, processed_data_folder_name)
    
    #### #### 
    
    processed_ufo_data_folder_path = create_subfolder(processed_data_folder_path, ufo_data_folder_name)
    processed_cdc_data_folder_path = create_subfolder(processed_data_folder_path, cdc_data_folder_name)
    processed_fips_data_folder_path = create_subfolder(processed_data_folder_path, fips_data_folder_name)

    #### #### #### #### 
    
    cleaned_data_folder_path = create_subfolder(data_folder_path, cleaned_data_folder_name)

    #### #### 
    
    cleaned_ufo_data_folder_path = create_subfolder(cleaned_data_folder_path, ufo_data_folder_name)
    cleaned_cdc_data_folder_path = create_subfolder(cleaned_data_folder_path, cdc_data_folder_name)
    cleaned_fips_data_folder_path = create_subfolder(cleaned_data_folder_path, fips_data_folder_name)

    #### #### #### #### 

    archived_data_folder_path = create_subfolder(data_folder_path, archived_data_folder_name)

    #### #### 
    
    archived_ufo_data_folder_path = create_subfolder(archived_data_folder_path, ufo_data_folder_name)
    archived_cdc_data_folder_path = create_subfolder(archived_data_folder_path, cdc_data_folder_name)
    archived_fips_data_folder_path = create_subfolder(archived_data_folder_path, fips_data_folder_name)
    
    #### #### #### ####       
    
    database_folder_path = create_subfolder(data_folder_path, database_folder_name)
    
    #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
    
    file_directories = {
        "doc": str(doc_folder_path),
        "cdc_footer" : str(cdc_footer_folder_path),
        "readme": str(readme_folder_path),
        "scripts": str(scripts_folder_path),
        "notebooks": str(notebooks_folder_path),
        "bin_folder": str(bin_folder_path),
        "results": str(results_folder_path),
        "data": str(data_folder_path),
        "archived_data":str(archived_data_folder_path),
        "processed_data": str(processed_data_folder_path),
        "raw_data":str(raw_data_folder_path),
        "cleaned_data":str(cleaned_data_folder_path),
        "db":str(database_folder_path),
        "raw_ufo_data": str(raw_ufo_data_folder_path),
        "raw_cdc_data": str(raw_cdc_data_folder_path),
        "raw_fips_data":str(raw_fips_data_folder_path),
        "processed_ufo_data": str(processed_ufo_data_folder_path),
        "processed_cdc_data": str(processed_cdc_data_folder_path),
        "processed_fips_data":str(processed_fips_data_folder_path),       
        "cleaned_ufo_data": str(cleaned_ufo_data_folder_path),
        "cleaned_cdc_data": str(cleaned_cdc_data_folder_path),
        "cleaned_fips_data": str(cleaned_fips_data_folder_path),
        "archived_ufo_data": str(archived_ufo_data_folder_path),
        "archived_cdc_data": str(archived_cdc_data_folder_path),
        "archived_fips_data": str(archived_fips_data_folder_path)
        
    }

    print("\nSummary of Created Folder Paths:")
    
    for folder_name, path in file_directories.items():
        print(f"  {folder_name}: {path}")
    
    # Save the paths to a JSON file for later access
    save_folder_paths(folder_path_subdirectory, file_directories)

    return file_directories


# In[98]:


def save_folder_paths(location: str, folder_paths: dict):

    """Saves the folder paths to a JSON file."""
    #folder_path_subdirectory = location
    
    file_save_path = Path(folder_path_subdirectory) / folder_path_file

    with open(file_save_path, 'w') as file:
        json.dump(folder_paths, file, indent=4)
        
    print(f"\nFolder paths have been saved to '{folder_path_file}' at '{file_save_path.parent}'.")


# In[99]:


def load_folder_paths() -> dict:
    
    """Loads the folder paths from the JSON file."""
    
    try:
        file_save_path = Path(folder_path_subdirectory) / folder_path_file
        
        with open(file_save_path, 'r') as file:
            folder_paths = json.load(file)
            
            return folder_paths
            
    except FileNotFoundError:
        
        print(f"Error: '{folder_path_file}' not found. Please run this script to create the paths.")
        
        return {}


# In[100]:


def get_folder_path(folder_name: str) -> str:
    
    """Retrieves a specific folder path from the saved folder paths."""
    
    folder_paths = load_folder_paths()
    
    return folder_paths.get(folder_name, f"Error: '{folder_name}' folder path not found.")


# In[101]:


# Only run this if the script is executed directly
if __name__ == "__main__":
     
    # Initialize On Running
    initialize_folder_paths()
    
    #base_folder_path = "."
    #base_folder_path = ".."
    data_folder_name = "data"
    archived_data_folder_name = "archived_data"
    scripts_folder_name = "scripts"
    notebooks_folder_name = "notebooks"
    bin_folder_name = "bin"
    doc_folder_name = "doc"
    cdc_footer_folder_name = "cdc_data_footers"
    readme_folder_name = "read_me"
    results_folder_name = "results"
    raw_data_folder_name = "raw_data"
    processed_data_folder_name = "processed_data"
    cleaned_data_folder_name = "cleaned_data"
    database_folder_name = "db"
    ufo_data_folder_name = "ufo_data"
    cdc_data_folder_name = "cdc_data"
    fips_data_folder_name = "fips_data"

    
    # Create all folders and store their paths
    get_all_folder_paths(
        base_folder_path,
        data_folder_name,
        archived_data_folder_name,
        scripts_folder_name,
        notebooks_folder_name,
        bin_folder_name,
        doc_folder_name,
        cdc_footer_folder_name,
        readme_folder_name,
        results_folder_name,
        raw_data_folder_name,
        processed_data_folder_name,
        cleaned_data_folder_name,
        database_folder_name,
        ufo_data_folder_name, 
        cdc_data_folder_name, 
        fips_data_folder_name
    )

