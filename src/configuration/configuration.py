import os
import sys
from src.logger import logger
from src.exception import CustomException
from src.utils import read_yaml
from src.entity.config_entity import DataIngestionConfig
from src.constants import CONFIG_FILE_PATH
import logging

class AppConfiguration:
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH):
        try:
            self.config = read_yaml(config_file_path)
        except Exception as e:
            logger.error(f"Error occurred while initializing AppConfiguration: {e}")
            raise CustomException(e, sys)
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.config['data_ingestion_config']
            artifacts_dir = self.config['artifacts_config']['artifacts_dir']
            dataset_url = data_ingestion_config['dataset_download_url']

            dataset_dir = data_ingestion_config['data_ingestion_dir']
            dataset_dir_path = os.path.join(artifacts_dir, dataset_dir)

            raw_dir = data_ingestion_config['raw_data_dir']
            raw_dir_path = os.path.join(dataset_dir_path, raw_dir)

            ingested_dir = data_ingestion_config['ingested_data_dir']
            ingested_dir_path = os.path.join(dataset_dir_path, ingested_dir)

            response = DataIngestionConfig(dataset_download_url=dataset_url,
                                            data_ingestion_dir=dataset_dir_path,
                                            raw_data_dir=raw_dir_path,
                                            ingested_data_dir=ingested_dir_path
                                            )
            
            logging.info(f"Data Ingestion Config: {response}")
            return response

        except Exception as e:
            logger.error(f"Error occurred while getting data ingestion config: {e}")
            raise CustomException(e, sys)


if __name__ == "__main__":
    app_config = AppConfiguration()
    data_ingestion_config = app_config.get_data_ingestion_config()
    print(data_ingestion_config)
