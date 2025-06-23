import os
import sys
from src.logger import logger
from src.exception import CustomException
from src.utils import read_yaml
from src.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelRecommendationConfig
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
            
            return response

        except Exception as e:
            logger.error(f"Error occurred while getting data ingestion config: {e}")
            raise CustomException(e, sys)
    
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            data_validation_config = self.config['data_validation_config']
            data_ingestion_config = self.config['data_ingestion_config']
            dataset_dir = data_ingestion_config['data_ingestion_dir']
            artifacts_dir = self.config['artifacts_config']['artifacts_dir']
            data_validation_dir = data_validation_config['data_validation_dir']
            book_csv_file = data_validation_config['book_csv_file']
            ratings_csv_file = data_validation_config['ratings_csv_file']

            clean_data_path = os.path.join(artifacts_dir, data_validation_dir, data_validation_config['clean_data_dir'])
            serialized_object_path = os.path.join(artifacts_dir, data_validation_dir, data_validation_config['serialized_data_dir'])
            book_csv_file_path = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_data_dir'], book_csv_file)
            ratings_csv_file_path = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['ingested_data_dir'], ratings_csv_file)

            response = DataValidationConfig(data_validation_dir=data_validation_dir,
                                             clean_data_dir=clean_data_path,
                                             serialized_data_dir=serialized_object_path,
                                             book_csv_file=book_csv_file_path,
                                             ratings_csv_file=ratings_csv_file_path
                                            )
            
            return response

        except Exception as e:
            logger.error(f"Error occurred while getting data validation config: {e}")
            raise CustomException(e, sys)
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            data_transformation_config = self.config['data_transformation_config']
            data_validation_config = self.config['data_validation_config']
            data_ingestion_config = self.config['data_ingestion_config']
            artifacts_dir = self.config['artifacts_config']['artifacts_dir']
            data_transformation_dir = data_transformation_config['data_transformation_dir']

            data_transformation_dir_path = os.path.join(artifacts_dir, data_transformation_dir)
            cleaned_data_path = os.path.join(artifacts_dir, data_validation_config['data_validation_dir'], data_validation_config['clean_data_dir'], 'final_ratings.csv')
            transformed_data_dir = os.path.join(artifacts_dir, data_transformation_dir, data_transformation_config['transformed_data_dir'])

            response = DataTransformationConfig(data_transformation_dir=data_transformation_dir_path,
                                                clean_data_dir=cleaned_data_path,
                                                transformed_data_dir=transformed_data_dir
                                                )
            
            return response

        except Exception as e:
            logger.error(f"Error occurred while getting data transformation config: {e}")
            raise CustomException(e, sys)
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            model_trainer_config = self.config['model_trainer_config']
            data_transformation_config = self.config['data_transformation_config']
            artifacts_dir = self.config['artifacts_config']['artifacts_dir']
            model_trainer_dir = model_trainer_config['model_trainer_dir']

            transformed_data_file_path = os.path.join(artifacts_dir, data_transformation_config['data_transformation_dir'], data_transformation_config['transformed_data_dir'], 'transformed_data.pkl')
            trained_model_dir = os.path.join(artifacts_dir, model_trainer_dir)
            trained_model_name = model_trainer_config['trained_model_name']

            response = ModelTrainerConfig(model_trainer_dir=trained_model_dir,
                                           trained_model_name=trained_model_name,
                                           transformed_data_file_path=transformed_data_file_path
                                        )
            
            return response

        except Exception as e:
            logger.error(f"Error occurred while getting model trainer config: {e}")
            raise CustomException(e, sys)
    
    def get_model_recommendation_config(self) -> ModelRecommendationConfig:
        try:
            artifacts_dir = self.config['artifacts_config']['artifacts_dir']
            model_trainer_config = self.config['model_trainer_config']
            data_transformation_config = self.config['data_transformation_config']

            book_name_serialized_object = os.path.join(artifacts_dir, data_transformation_config['data_transformation_dir'], data_transformation_config['transformed_data_dir'], 'book_names.pkl')
            book_pivot_serialized_object = os.path.join(artifacts_dir, data_transformation_config['data_transformation_dir'], data_transformation_config['transformed_data_dir'], 'book_pivot.pkl')
            final_ratings_serialized_object = os.path.join(artifacts_dir, data_transformation_config['data_transformation_dir'], data_transformation_config['transformed_data_dir'], 'final_ratings.pkl')
            trained_model_path = os.path.join(artifacts_dir, model_trainer_config['model_trainer_dir'], model_trainer_config['trained_model_name'])

            response = ModelRecommendationConfig(book_name_serialized_object=book_name_serialized_object,
                                                 book_pivot_serialized_object=book_pivot_serialized_object,
                                                 final_ratings_serialized_object=final_ratings_serialized_object,
                                                 trained_model_path=trained_model_path
                                                )
            
            return response
        
        except Exception as e:
            logger.error(f"Error occurred while getting model recommendation config: {e}")
            raise CustomException(e, sys)
