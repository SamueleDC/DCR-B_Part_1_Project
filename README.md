# DCR-B_Part_1_Project
The purpose of the project was to build a search facility on a subtree of a local file sysstem.


## Subtree specification
First of all a subtree was built with a depth of at least 6, containing a specific subtree named “DCRB” which has a depth of at least 4. Inside the DCRB subtree 50 files downloaded by wikipedia have been inserted. The distribution can be see from the file [Listing_DCRB_directory](Listing_DCRB_directory)


## Storage engine
As a storage engine, for the files of the subtree Mysql was choosen and the database schema can be visualize from the file [Database_schema.sql](Database_schema.sql) .
Furthermore, to oprimize the search, some indexes were created and can be analyzed from the files [Index_creation.sql](Index_creation.sql) and [Show_index.png](Show_index.png).


## Table load & Search_engine
Then two scripts in python, that are [Database_load.py](Database_load.py) and [Search_engine.py](Search_engine.py) were created, wich respectively load the content of the subtree mentioned above into the database and the other, in base alla parola che viene immessa da tastiera, perform a search wich return:

1. The full path name of the file that matches
2. The type of the file (directory or simple file)
3. If the string is found with a file, the number of occurences in the file of the string
4. The occurences of that string in a searchable file
5. the depth of that file



## Tests
Finally, to assure the effectness of the search_engine executions of different type were performed, resulting in having:
* A snapshot of the search for a “non existing” string [No_string_found.png](No_string_found.png)
* A snapshot of the search for a string matching at least two file names, but not found in any searchable file [Only_file_name.png](Only_file_name.png)
* A snapshot of the search for a string matching at least one file name and contained in at least one searchable file, with the counts of the occurrencies in the file(s) [File_name_and_searchable_file.png](File_name_and_searchable_file.png)
* A snapshot of the search for a string that does not match a file name but is found in at least one searchable file, with the counts of the occurrencies in the file(s) [Only_searchable_file.png](Only_searchable_file.png)

 
