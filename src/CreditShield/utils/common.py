import os
import sys
import yaml
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations


from src.CreditShield.exception import CustomException
from src.CreditShield.logger import logging


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns ConfigBox type object

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox typ
    """
    try:
        logging.info(f"> Reading yaml file: {path_to_yaml}")

        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            logging.info(f"Yaml file read successfully: {path_to_yaml}!")

            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logging.error(f"Error reading yaml file: {path_to_yaml}!")
        raise CustomException(e, sys)


@ensure_annotations
def create_directories(path_to_directories: list):
    """
    Create list of directories

    Args:
        path_to_directories (list): list of path of directories

    Returns:
        None
    """
    try:
        for path in path_to_directories:
            if not os.path.exists(path):
                logging.info(f"> Creating directory: {path}")

                os.makedirs(path)

                logging.info(f"Directory created successfully: {path}!")

            else:
                logging.info(f"Directory already exists: {path}. Skipping creating directory!")

    except Exception as e:
        logging.error(f"Error creating directories: {path_to_directories}")
        raise CustomException(e, sys)


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    try:
        logging.info(f"> Getting size of file: {path}")

        size_in_kb = round(os.path.getsize(path) / 1024)

        return f"~ {size_in_kb} KB"

    except Exception as e:
        logging.error(f"Error getting size of file: {path}!")
        raise CustomException(e, sys)