import os
import sys
import streamlit as st
import pickle
import numpy as np
from src.logger import logger
from src.exception import CustomException
from src.configuration.configuration import AppConfiguration
from src.pipeline.training_pipeline import TrainingPipeline

class Recommendation:
    def __init__(self):
        self.config = AppConfiguration()
        self.recommendation_config = self.config.get_model_recommendation_config()

    def fetch_poster(self, suggestion):
        try:
            book_name = []
            id_index = []
            poster_url = []
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_object, 'rb'))
            final_ratings = pickle.load(open(self.recommendation_config.final_ratings_serialized_object, 'rb'))
            book_names = pickle.load(open(self.recommendation_config.book_name_serialized_object, 'rb'))

            for book_id in suggestion:
                book_name.append(book_pivot.index[book_id])
                print(book_name)

            for name in book_name[0]:
                print(name)
                array = np.where(final_ratings['title'] == name)[0][0]
                print(array)
                id_index.append(array)

            for index in id_index:
                url = final_ratings.iloc[index]['url']
                poster_url.append(url)
            
            return poster_url

        except Exception as e:
            logger.error(f"Error occurred while fetching poster: {e}")
            raise CustomException(e, sys)
    
    def recommend_book(self, book_name):
        try:
            book_list = []
            model = pickle.load(open(self.recommendation_config.trained_model_path, 'rb'))
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_object, 'rb'))
            book_id = np.where(book_pivot.index == book_name)[0][0]

            distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

            poster_url = self.fetch_poster(suggestion)

            for i in range(len(suggestion)):
                books = book_pivot.index[suggestion[i]]
                for j in books:
                    book_list.append(j)

            return book_list, poster_url
            
        except Exception as e:
            logger.error(f"Error occurred while recommending book: {e}")
            raise CustomException(e, sys)
    
    def train_engine(self):
        try:
            st.text("Training started...")
            training_pipeline = TrainingPipeline()
            training_pipeline.start_training_pipeline()
            st.text("Training completed successfully!")

        except Exception as e:
            logger.error(f"Error occurred while training engine: {e}")
            raise CustomException(e, sys)
    
    def recommend_engine(self, book_name):
        try:
            book_list, poster_url = self.recommend_book(book_name)
            
            col1, col2, col3, col4, col5= st.columns(5)
            with col1:
                st.text(book_list[1])
                st.image(poster_url[1])
            with col2:
                st.text(book_list[2])
                st.image(poster_url[2])
            with col3:
                st.text(book_list[3])
                st.image(poster_url[3])
            with col4:
                st.text(book_list[4])
                st.image(poster_url[4])
            with col5:
                st.text(book_list[5])
                st.image(poster_url[5])

        except Exception as e:
            logger.error(f"Error occurred while recommending engine: {e}")
            raise CustomException(e, sys)
    