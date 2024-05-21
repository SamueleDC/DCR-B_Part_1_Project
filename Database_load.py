#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import mysql.connector
from bs4 import BeautifulSoup

# Get the type of file
def get_file_type(file_name):
    return "file" if '.' in file_name else "dir"

# Get the HTML content
def get_file_content(file_path):
    if file_path.endswith('.html'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                return soup.get_text()
        except Exception as e:
            print(f"Errore nella lettura del file {file_path}: {e}")
            return None
    return None

# get the dimension of the file
def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        print(f"Errore nell'ottenere la dimensione del file {file_path}: {e}")
        return None

# Insert values in the table
def insert_into_mysql(cursor, full_path, file_name, file_type, content, depth, size):
    query = "INSERT INTO S_FILES (FULL_PATH_NAME, FILE_NAME, FILE_TYPE, CONTENT, DEPTH, SIZE) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (full_path, file_name, file_type, content, depth, size)
    cursor.execute(query, values)

# Directory to pass
directory = "C:/Users/dicug/Desktop"

try:
# Connection to DB
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="23413",
        database="search_facility",
        autocommit=False 
    )
    cursor = conn.cursor()
    conn.start_transaction()

# scan files and directories
    for root, dirs, files in os.walk(directory):
        depth = root.count(os.sep) - directory.count(os.sep)
        for dir_name in dirs:
            full_path = os.path.join(root, dir_name)
            file_name = os.path.basename(full_path)
            file_type = get_file_type(file_name)
            insert_into_mysql(cursor, full_path, file_name, file_type, None, depth, None)

        for file_name in files:
            full_path = os.path.join(root, file_name)
            file_type = get_file_type(file_name)
            content = get_file_content(full_path)
            size = get_file_size(full_path)
            insert_into_mysql(cursor, full_path, file_name, file_type, content if content else None, depth, size)

    conn.commit() # One single transaction for all operations
    print("Dati inseriti con successo nella tabella MySQL.")

except Exception as e:
    print("Si è verificato un errore:", e)
    conn.rollback()

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()

