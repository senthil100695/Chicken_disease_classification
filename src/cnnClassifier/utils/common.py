import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """
    reads the yaml file and returns

    Args:
    Path_to_yaml(str) : path like input

    Raises:
    ValueError ; if yaml file empty
    e : empty file

    Returns:

    ConfigBox : ConfigBoxtype
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file : {path_to_yaml} loaded successfully')
            return ConfigBox(content)      
    except BoxValueError:
        raise ValueError('yaml file is empty') 
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories : list,verbose = True):
    '''
    create the list of directories

    args:
        path_to_directories (list) : list of path to create directories
        ignore_log (bool,optional ) : ignore if multiple directories is created. defaults is be False. 
    
    '''
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'created directory at : {path}')
        
@ensure_annotations
def save_json(path: Path,data : dict ):
    '''
    save the data into json format 

    with the particular path

    '''
    with open(path,'w') as f:
        json.dump(data, f, indent= 4)
    logger.info(f'json file saved at : {path}')


@ensure_annotations
def get_size(path: Path) -> str:
    '''
    get size in kb

    args(Path) : path to the file

    returns str : size in kb
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'



