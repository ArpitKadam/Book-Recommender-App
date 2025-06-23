from src.components.data_ingestion import DataIngestion
from src.logger import logger
from src.exception import CustomException
import sys

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
    
    def start_training_pipeline(self):
        try:
            logger.info("*"*50)
            self.data_ingestion.initiate_data_ingestion()
            logger.info("*"*50)
        except Exception as e:
            logger.error(f"Error occurred while starting training pipeline: {e}")
            raise CustomException(e, sys)
