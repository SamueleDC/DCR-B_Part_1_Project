# DCR-B_Part_1_Project
The purpose of the project was to build a search facility on a subtree of a local file sysstem.


## Subtree specification
First, a subtree with a depth of at least 6 was constructed, which included a special subtree designated "DCRB" with a depth of at least 4. Inside the DCRB subtree, 50 files retrieved from Wikipedia have been added. The distribution can be seen in [Listing_DCRB_directory](Listing_DCRB_directory).


## Storage engine
Mysql was chosen as the storage engine for the subtree's files, and the database schema can be viewed in [Database_schema.sql](Database_schema.sql). Furthermore, to optimize the search, various indexes were generated, which may be examined in [Index_creation.sql](Index_creation.sql) and [Show_index.png](Show_index.png).

## Table load & Search_engine
Then two Python scripts, [Database_load.py](Database_load.py) and [Search_engine.py](Search_engine.py), were written, one to load the content of the previously mentioned subtree into the database and the other to perform a search based on the text entered by the user, which returns:

1. The full path name of the file that matches
2. The type of the file (directory or simple file)
3. If the string is found with a file, the number of occurences in the file of the string
4. The occurences of that string in a searchable file
5. the depth of that file


## Tests
Finally, to test the effectiveness of the search engine, various types of executions were done, resulting in having: 
* A snapshot of a search for a "non-existing" string [No_string_found.png](No_string_found.png)
* A snapshot of the search for a “non existing” string [No_string_found.png](No_string_found.png)
* A snapshot of the search for a string matching at least two file names, but not found in any searchable file [Only_file_name.png](Only_file_name.png)
* A snapshot of the search for a string matching at least one file name and contained in at least one searchable file, with the counts of the occurrencies in the file(s) [File_name_and_searchable_file.png](File_name_and_searchable_file.png)
* A snapshot of the search for a string that does not match a file name but is found in at least one searchable file, with the counts of the occurrencies in the file(s) [Only_searchable_file.png](Only_searchable_file.png)

 
