import yaml
import sys
from src.exception import CustomException
from src.logger import logger

def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise CustomException(e, sys)