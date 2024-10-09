import os 
from pathlib import Path
import sys
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

projectname= 'Bot' # Main bot application folder

list_of_files=[
    ".github/workflows/.gitkeep",
    ".venv/" # Virtual environment folder to be ignored by git
    f"src/{projectname}/__init__.py", # Makes the folder a python package
    f"src/{projectname}/main.py", # Entry point for the bot
    f"src/{projectname}/config.py", # Configuration settings (e.g., API Keys, bot settings)
    f"src/{projectname}/logger.py", # Custom logger setup
    f"src/{projectname}/handlers/__init__.py", # For Bot Handler logic
    f"src/{projectname}/services/__init__.py", # Folder for external service intergration such as SAP, Serivce Now etc.
    f"tests/{projectname}/tests_main.py", # Unit test folder for main
    ".env" #Environment variables(API-Key and Endpoint URL)
    ]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filepath=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info("Directory created at {filedir} for dile {filename}")

    if(not os.path.exists(filepath))or(os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"File created at {filepath}")
    

    else:
        logging.info(f"File already exists at {filepath}")
