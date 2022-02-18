## A toy project
- Pre-request: 
  - (pyzotero)[https://anaconda.org/conda-forge/pyzotero]
  - 
  
- The [[Zotero.py]] could create a markdown file which can be uploaded to your roam research account.
  - Run the script. Type the name of the reference (make sure your zotero has that reference). In folder output_zotero, you will get a markdown file contains the following information of the reference:  
     - abbreviation (the style is same to google scholar)
     - title 
     - year 
     - author(s)
     - publisher 
     - hyperlink of the path of the local file in zotero (if you have the file)
     - hyperlink of the folder of the local library 
- The [[Roam_to_Latex.py]] can help to convert the the markdown file download from roam research. 
    - Download the file from Roam research into folder [[download]] 
    - In folder [[outout_md]], you will get the converted markdown file. 
    - In folder [[output_latex]], you will get the conveted latex file. 
 
- Future's plan:
    - Add the reference in the bottom of the converted file if there is citation in the file. 
    - When roam-research have open API, I will wrap the download/upload steps into the script. 
  
 
