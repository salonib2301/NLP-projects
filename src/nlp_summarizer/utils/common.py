# this file basically contains all the functions that are used frequently 
import os
from box.exceptions import BoxValueError # to add exceptions 
import yaml #to read yaml file
from nlp_summarizer.logging as logger #custom logger
from ensure import ensure_annotations #
from box import ConfigBox #in order to access  values just using keys we use ConfigBox
from pathlib import Path 
from typing import Any

#implementing function which reads YAML file
@ensure_annotations #decorator when a desired type of data input is give and you need it in same type so we use ensure eg pass int get int
def read_yaml(path_to_yaml: Path) -> ConfigBox: # Here -> indicates towards the return data type here it is ConfigBox
    """Read a YAML file and return

    Args:
        path_to_yaml (Path): Path like input

    Raises:
        ValueError: If the YAML file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_files:
            content = yaml.safe_load(yaml_files)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True): # creating directory
    """Create list of directories

    Args:
        path_to_directories (list): list of directories
        ignore_log (bool,optional): ignore if multiple dirs is to be created. Defaults to False

    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory at : {path}")

@ensure_annotation
def get_size(path: Path) -> str:
    """Returns the size in KB
    
    Args:
        path (Path): Path of file
    
    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path/1024)
    return f" ~{size_in_kb} KB"
