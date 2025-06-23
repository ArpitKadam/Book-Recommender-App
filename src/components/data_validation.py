import os
import sys
from src.exception import CustomException
from src.logger import logger
from src.configuration.configuration import AppConfiguration
import pandas as pd
import pickle

class DataValidation:
    def __init__(self, config = AppConfiguration()):
        try:
            self.config = config
            self.data_validation_config = config.get_data_validation_config()
        except Exception as e:
            logger.error(f"Error occurred while initializing DataValidation: {e}")
            raise CustomException(e, sys)
        
    def preprocess(self):
        try:
            ratings = pd.read_csv(self.data_validation_config.ratings_csv_file, sep=';', encoding="latin-1", on_bad_lines='skip')
            books = pd.read_csv(self.data_validation_config.book_csv_file, sep=';', encoding="latin-1", on_bad_lines='skip')

            logger.info(f"Ratings DataFrame Shape {ratings.shape}")
            logger.info(f"Books DataFrame Shape {books.shape}")

            logger.info(f"Ratings DataFrame Columns {ratings.columns}")
            logger.info(f"Books DataFrame Columns {books.columns}")

            logger.info("Dropping Unnecessary Columns from Ratings DataFrame")
            books.drop(['Image-URL-S', 'Image-URL-M'], axis=1, inplace=True)
            
            logger.info("Renaming Columns in Books DataFrame")
            books.rename(columns={
                "Book-Title":"title",
                "Book-Author":"author",
                "Year-Of-Publication":"year",
                "Publisher":"publisher",
                "Image-URL-L":"url"
            }, inplace=True)
            logger.info("Columns Renamed Successfully")
            logger.info(f"New column names: {books.columns}")

            logger.info("Renaming Columns in Ratings DataFrame")
            ratings.rename(columns={
                "User-ID":"user_id",
                "Book-Rating":"rating"
            }, inplace=True)
            logger.info("Columns Renamed Successfully")
            logger.info(f"New column names: {ratings.columns}")

            logger.info("Only keeping users with more than 150 ratings")
            x = ratings['user_id'].value_counts() > 150
            y = x[x].index
            ratings = ratings[ratings['user_id'].isin(y)]
            logger.info(f"Ratings DataFrame Shape after filtering: {ratings.shape}")

            logger.info("Merging Ratings and Books DataFrames")
            ratings_with_books = ratings.merge(books, on='ISBN')
            logger.info("Merged Successfully")
            logger.info(f"New DataFrame Shape {ratings_with_books.shape}")

            logger.info("Getting Ratings Count for Each Book")
            rating_count = ratings_with_books.groupby('title')['rating'].count().reset_index()
            rating_count.rename(columns={'rating':'num_ratings'}, inplace=True)
            final_ratings = ratings_with_books.merge(rating_count, on='title')
            logger.info("Ratings Count Obtained Successfully")

            logger.info("Filtering Books with more than 50 ratings")
            final_ratings = final_ratings[final_ratings['num_ratings'] >= 50]
            logger.info("Filtered Successfully")

            logger.info("Dropping Duplicates")
            final_ratings.drop_duplicates(['user_id', 'title'], inplace=True)
            logger.info("Dropped Successfully")

            logger.info(f"Final DataFrame Shape {final_ratings.shape}")

            os.makedirs(self.data_validation_config.clean_data_dir, exist_ok=True)
            logger.info(f"Clean Data Directory Created: {self.data_validation_config.clean_data_dir}")
            final_ratings.to_csv(os.path.join(self.data_validation_config.clean_data_dir, "final_ratings.csv"), index=False)
            logger.info(f"Clean Data Saved Successfully to {self.data_validation_config.clean_data_dir}")

            os.makedirs(self.data_validation_config.serialized_data_dir, exist_ok=True)
            logger.info(f"Serialized Data Directory Created: {self.data_validation_config.serialized_data_dir}")
            pickle.dump(final_ratings, open(os.path.join(self.data_validation_config.serialized_data_dir, "final_ratings.pkl"), "wb"))
            logger.info(f"Serialized Data Saved Successfully to {self.data_validation_config.serialized_data_dir}")

        except Exception as e:
            logger.error(f"Error occurred while preprocessing data: {e}")
            raise CustomException(e, sys)
    
    def initiate_data_validation(self):
        try:
            logger.info("Initiating data validation")
            self.preprocess()
            logger.info("Data validation completed successfully")
        except Exception as e:
            logger.error(f"Error occurred while initiating data validation: {e}")
            raise CustomException(e, sys)