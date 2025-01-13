#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Version 5
## 12/25/24
## 22:24


# In[2]:


# Pandas
import pandas as pd

# Numpy
import numpy as np

# RegularExpression for string matching
import re

# SQL Alchemy for SQL DB Creation and Storage
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# GLOB 
import glob 

# Pathlib 
from pathlib import Path

# NB Importer
import nbimporter

# My Modules
#import folder_manager as fm

from d497_helpers import folder_manager as fm
# In[3]:


#global database_folder_path
#global database_file_path

engine = None
session = None


# In[5]:


def initialize_engine():

    global engine

    fm.initialize_folder_paths()
    
    db_path = fm.get_folder_path("db")

    full_path = "sqlite:///" + db_path + "/database.db"

    engine = create_engine(full_path, echo=True)

    return engine 

def db_session(engine):

    global session 
    
    Session = sessionmaker(bind=engine)
    session = Session()

    return session
    
def initialize_session():
    """
    Initialize the global session using the global engine.
    """
    global session
    if engine is None:
        raise RuntimeError("Engine is not initialized.")
    session = db_session(engine)
    
initialize_engine()
initialize_session()

def get_engine():
    """Retrieve the initialized database engine."""
    if engine is None:
        raise RuntimeError("Engine is not initialized.")
    return engine

def get_session():
    """Retrieve the initialized session."""
    if session is None:
        raise RuntimeError("Session is not initialized.")
    return session

def execute_query(query):
    """Execute a raw SQL query and return the result."""

    try:
    # Start a transaction
        with session.begin():
            # Get the raw connection
            connection = session.connection()

            result = connection.execute(text(query))
            
            # Read SQL to Pandas dataframe
            #dataframe_name = pd.read_sql(sql_query, con=connection)

            # Return dataframe
            return result.fetchall()
        
        #print("Data inserted successfully!")
        
    except Exception as e:
        # Rollback transaction on error
        session.rollback()
        print("Transaction failed! Rolling back...")
        print(f"Error: {e}")
        
    finally:
        # Close the session
        session.close()


def export_to_sql(dataframe, tablename):

    #self.session = session
    
    try:
        # Start a transaction
        with session.begin():
            # Get the raw connection
            connection = session.connection()
            
            # Write DataFrame to database
            dataframe.to_sql(tablename, con=connection, if_exists='replace', index=False)
            #FIPS_df.to_sql('FIPS', con=connection, if_exists='replace', index=False)
            
        
        #print("Data inserted successfully!")
        
    except Exception as e:
        # Rollback transaction on error
        session.rollback()
        print("Transaction failed! Rolling back...")
        print(f"Error: {e}")
        
    finally:
        # Close the session
        session.close()


def export_df_from_sql(sql_query, dataframe_name):


    #self.session = session
    
    try:
    # Start a transaction
        with session.begin():
            # Get the raw connection
            connection = session.connection()
        
            # Read SQL to Pandas dataframe
            dataframe_name = pd.read_sql(sql_query, con=connection)

            # Return dataframe
            return dataframe_name
        
        #print("Data inserted successfully!")
        
    except Exception as e:
        # Rollback transaction on error
        session.rollback()
        print("Transaction failed! Rolling back...")
        print(f"Error: {e}")
        
    finally:
        # Close the session
        session.close()


def say_hello_db():
    # Creating Database
    
    fm.initialize_folder_paths()

    db_folder_path = fm.get_folder_path("db")
    
    db_file_path = Path(db_folder_path) / 'database.db'
    
    engine = create_engine(f'sqlite:///{db_file_path}')
    
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())

    conn.close()


# In[ ]:


if __name__ == "__main__":
    say_hello_db()

