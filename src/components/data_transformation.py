import os
import sys
from src.exception import CustomException
from src.logger import logger
from src.configuration.configuration import AppConfiguration
import pandas as pd
import pickle

class DataTransformation:
    def __init__(self, config = AppConfiguration()):
        try:
            self.config = config
            self.data_validation_config = config.get_data_validation_config()
            self.data_transformation_config = config.get_data_transformation_config()
        except Exception as e:
            logger.error(f"Error occurred while initializing DataTransformation: {e}")
            raise CustomException(e, sys)
    
    def get_transformed_data(self):
        try:
            logger.info(f"Getting validated data from {self.data_validation_config.clean_data_dir}")
            data_path = os.path.join(self.data_validation_config.clean_data_dir, 'final_ratings.csv')
            df = pd.read_csv(data_path)
            book_pivot = df.pivot_table(columns="user_id", index="title", values="rating")
            logger.info("Got validated data successfully")

            book_pivot.fillna(0, inplace=True)
            logger.info("Filled NaN values with 0")

            logger.info(f"Creating directory {self.data_transformation_config.transformed_data_dir}")
            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            logger.info(f"Saving transformed data to {self.data_transformation_config.transformed_data_dir}")
            transformed_data_path = os.path.join(self.data_transformation_config.transformed_data_dir, 'transformed_data.pkl')
            pickle.dump(book_pivot, open(transformed_data_path, 'wb'))
            logger.info("Saved transformed data successfully")

            book_name = book_pivot.index
            logger.info("Got book names successfully")

            logger.info(f"Saving book names to pickle file to {self.data_transformation_config.transformed_data_dir}")
            book_name_path = os.path.join(self.data_transformation_config.transformed_data_dir, 'book_names.pkl')
            pickle.dump(book_name, open(book_name_path, 'wb'))
            logger.info("Saved book names successfully")

            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            logger.info(f"Saving book_pivot data to {self.data_transformation_config.transformed_data_dir}")
            transformed_data_path = os.path.join(self.data_transformation_config.transformed_data_dir, 'book_pivot.pkl')
            pickle.dump(book_pivot, open(transformed_data_path, 'wb'))
            logger.info("Saved book_pivot data successfully")

            # Save final_ratings DataFrame with 'title', 'image_url', etc.
            final_ratings_path = os.path.join(self.data_transformation_config.transformed_data_dir, 'final_ratings.pkl')
            pickle.dump(df, open(final_ratings_path, 'wb'))
            logger.info("Saved final_ratings DataFrame with titles and metadata successfully")

        except Exception as e:
            logger.error(f"Error occurred while getting transformed data: {e}")
            raise CustomException(e, sys)

    def initiate_data_transformation(self):
        try:
            logger.info("Data Transformation initiated")
            self.get_transformed_data()
            logger.info("Data Transformation completed")
        except Exception as e:
            logger.error(f"Error occurred while initiating data transformation: {e}")
            raise CustomException(e, sys)