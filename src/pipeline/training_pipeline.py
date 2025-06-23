from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logger
from src.exception import CustomException
import sys

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion  = DataIngestion()
        self.data_validation = DataValidation()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()
    
    def start_training_pipeline(self):
        try:
            logger.info("*"*100)
            self.data_ingestion.initiate_data_ingestion()
            logger.info("*"*100)
            self.data_validation.initiate_data_validation()
            logger.info("*"*100)
            self.data_transformation.initiate_data_transformation()
            logger.info("*"*100)
            self.model_trainer.initiate_model_trainer()
            logger.info("*"*100)
        except Exception as e:
            logger.error(f"Error occurred while starting training pipeline: {e}")
            raise CustomException(e, sys)
