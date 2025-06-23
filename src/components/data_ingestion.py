import os
import sys
from src.exception import CustomException
from src.logger import logger
from urllib.request import urlretrieve
import zipfile
from src.configuration.configuration import AppConfiguration

class DataIngestion:
    def __init__(self, config = AppConfiguration()):
        try:
            self.config = config
            self.data_ingestion_config = config.get_data_ingestion_config()
        except Exception as e:
            logger.error(f"Error occurred while initializing DataIngestion: {e}")
            raise CustomException(e, sys)
    
    def download_data(self):
        try:
            dataset_url = self.data_ingestion_config.dataset_download_url
            logger.info(f"Downloading data from {dataset_url}")
            zip_download_dir = self.data_ingestion_config.raw_data_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            logger.info(f"Created directory {zip_download_dir}")
            datafile_name = os.path.basename(dataset_url)
            logger.info(f"File name: {datafile_name}")
            zip_file_path = os.path.join(zip_download_dir, datafile_name)
            urlretrieve(dataset_url, zip_file_path)
            logger.info(f"Data downloaded successfully to: {zip_file_path}")
            return zip_file_path
        except Exception as e:
            logger.error(f"Error occurred while downloading data: {e}")
            raise CustomException(e, sys)
    
    def extract_zip_file(self, zip_file_path: str):
        try:
            ingested_dir = self.data_ingestion_config.ingested_data_dir
            os.makedirs(ingested_dir, exist_ok=True)
            logger.info(f"Created directory {ingested_dir}")
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(ingested_dir)
            logger.info(f"Zip file extracted successfully to {ingested_dir}")
        except Exception as e:
            logger.error(f"Error occurred while extracting zip file: {e}")
            raise CustomException(e, sys)
    
    def initiate_data_ingestion(self):
        try:
            logger.info("Initiating data ingestion")
            zip_file_path = self.download_data()
            self.extract_zip_file(zip_file_path)
            logger.info("Data ingestion completed successfully")
        except Exception as e:
            logger.error(f"Error occurred while initiating data ingestion: {e}")
            raise CustomException(e, sys)