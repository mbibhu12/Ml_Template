# import pandas as pd
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'mlProject'



list_of_files = [
    f"src/{project_name}/init.py",
    f"src/{project_name}/components/init_.py",
    f"src/{project_name}/utils/init_.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/init.py",
    f"src/{project_name}/entity/init_.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/init_.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]



for filepath in list_of_files:
    filepath = Path (filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs (filedir, exist_ok=True)
        # logging.info(f"Creating directory; {filedir) for the file: {filename}")
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f'Creating empty file: {filepath}')


    else:
        logging.info(f"{filename} is already exist")