import os
from pathlib import Path
import logging #to log all info during run time as well

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]:%(message)s:')

project_name = "Text_Summarizer"

file_list = [
    ".github/workflows/.gitkeep",#used for CI/CD deployment a yaml file is used
    f"src/(project_name)/__init__.py", # constructor file is required to import the local pacakage
    f"src/(project_name)/components/__init__.py", # another folder componests with constructor file
    f"src/(project_name)/utils/__init__.py",
    f"src/(project_name)/utils/common.py",
    f"src/(project_name)/logging/__init__.py",
    f"src/(project_name)/config/__init__.py",
    f"src/(project_name)/config/configuration.py",
    f"src/(project_name)/pipeline/__init__.py",
    f"src/(project_name)/entity/__init__.py",
    f"src/(project_name)/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in file_list:
    filepath = Path(filepath)# here it will detect the type of OS in order to detect the "/","\" in the path
    filedir, filename = os.path.split(filepath)# this function will give the folder and filename
    if filedir != "":#checking if the filedirectory is empty or not
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")# here you are using f string to return twwo variables in a string hence curly braces

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):#checking if file exists or file size is zero only then the file will be created
        with open(filepath,'w') as f: # opening file in writing mode
            pass #just creating file hence pass
            logging.info(f"Creating empty file:{filepath}")


    else:
        logging.info(f"{filename} is already exists")#this will be printed if the file exists
        
