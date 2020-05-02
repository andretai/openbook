# openbook
 Generates list of open access books' details (count, title, author and link) from https://link.springer.com/ based on categories in csv file format.
 
# Prerequisites
 - Python 3
 - bs4
 - requests
 
# How to use
 1. At line 6, change file name to your desired one. (E.g. file_name = 'myfile.csv').
 2. On line 47, change 'discipline' to your desired category (E.g. discipline = 'Economics').
 3. On line 48, change 'pages' to the number of pages of said category (IMPORTANT: untick 'Include Preview-Only content' and click 'Books' under 'Content Type') (E.g. pages = 4)
 4. Run the application with the command 'python springBooks.py' and a csv file will be created in the same folder.
 
# Screenshot
 ![ss](/ss/ss.jpg)
