from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.logger import logger
from src.exception import CustomException
import sys

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion  = DataIngestion()
        self.data_validation = DataValidation()
    
    def start_training_pipeline(self):
        try:
            logger.info("*"*50)
            self.data_ingestion.initiate_data_ingestion()
            logger.info("*"*50)
            self.data_validation.initiate_data_validation()
            logger.info("*"*50)
        except Exception as e:
            logger.error(f"Error occurred while starting training pipeline: {e}")
            raise CustomException(e, sys)
