import os
import sys
from src.exception import CustomException
from src.logger import logger
from src.configuration.configuration import AppConfiguration
import pickle
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

class ModelTrainer:
    def __init__(self):
        try:
            self.config = AppConfiguration()
            self.model_trainer_config = self.config.get_model_trainer_config()
        except Exception as e:
            logger.error(f"Error occurred while initializing ModelTrainer: {e}")
            raise CustomException(e, sys)
    
    def train(self):
        try:
            logger.info("Loading data...")
            book_pivot_path = self.model_trainer_config.transformed_data_file_path
            book_pivot = pickle.load(open(book_pivot_path, 'rb'))
            logger.info(f"Data loaded successfully from {book_pivot_path}")

            logger.info("Sparsifying data...")
            book_sparse = csr_matrix(book_pivot)
            logger.info("Data sparsified successfully")

            logger.info("Fitting Data to Model...")
            model = NearestNeighbors(algorithm='brute')
            model.fit(book_sparse)
            logger.info("Data fitted to model successfully")

            logger.info("Saving model...")
            
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            logger.info(f"Creating Directory : {self.model_trainer_config.model_trainer_dir}")
            
            model_path = os.path.join(self.model_trainer_config.model_trainer_dir, self.model_trainer_config.trained_model_name)
            pickle.dump(model, open(model_path, 'wb'))
            logger.info(f"Model saved at: {model_path}")

        except Exception as e:
            logger.error(f"Error occurred while training the model: {e}")
            raise CustomException(e, sys)

        except Exception as e:
            logger.error(f"Error occurred while training the model: {e}")
            raise CustomException(e, sys)
    
    def initiate_model_trainer(self):
        try:
            logger.info("Initiating model training")
            self.train()
            logger.info("Model training completed successfully")
        except Exception as e:
            logger.error(f"Error occurred while initiating model training: {e}")
            raise CustomException(e, sys)