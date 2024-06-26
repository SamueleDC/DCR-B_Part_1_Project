#!/usr/bin/env python
# coding: utf-8

# In[54]:


import mysql.connector

def search_word_in_db(word):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="23413",
            database="search_facility"
        )
        cursor = conn.cursor()

        # Prepare the word with wildcards for LIKE and convert to lowercase
        like_word = f"%{word}%"
        lowercase_word = word.lower()

        # Query to find tuples and count occurrences
        query = """
        SELECT 
            FULL_PATH_NAME, FILE_NAME, FILE_TYPE, DEPTH,
            FLOOR((LENGTH(CONTENT) - LENGTH(REPLACE(CONTENT, %s, ''))) / LENGTH(%s)) AS occurrences
        FROM 
            S_FILES
        WHERE 
            LOWER(FILE_NAME) LIKE %s OR LOWER(CONTENT) LIKE %s
        HAVING occurrences > 0 OR occurrences IS NULL;
        """
        cursor.execute(query, (word, word, like_word, like_word))
        results = cursor.fetchall()

        # Print results
        if results:
            print(f"Found {len(results)} tuples containing the word '{word}':")
            for row in results:
                occurrences = row[4]
                if occurrences is None:
                    occurrences_str = "None"
                else:
                    occurrences_str = str(occurrences)
                print(f"Path: {row[0]}, File Name: {row[1]}, File Type: {row[2]}, Depth: {row[3]}, Occurrences: {occurrences_str}")
        else:
            print(f"No tuples found containing the word '{word}'.")

    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

search_word = input("Enter the word to search for: ")
search_word_in_db(search_word)

