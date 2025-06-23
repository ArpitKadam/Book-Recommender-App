import os 
import sys
import streamlit as st
import pickle
import numpy as np
import pandas as pd
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
            book_metadata = []

            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_object, 'rb'))
            final_ratings = pickle.load(open(self.recommendation_config.final_ratings_serialized_object, 'rb'))
            book_names = pickle.load(open(self.recommendation_config.book_name_serialized_object, 'rb'))

            for book_id in suggestion:
                book_name.append(book_pivot.index[book_id])

            for name in book_name[0]:
                array = np.where(final_ratings['title'] == name)[0][0]
                id_index.append(array)

            for index in id_index:
                row = final_ratings.iloc[index]
                poster_url.append(row['url'])
                metadata = {
                    'ISBN': row['ISBN'],
                    'title': row['title'],
                    'author': row['author'],
                    'year': row['year'],
                    'publisher': row['publisher'],
                    'avg_rating': round(final_ratings[final_ratings['title'] == row['title']]['rating'].mean(), 2)
                }
                book_metadata.append(metadata)

            return poster_url, book_metadata

        except Exception as e:
            logger.error(f"Error occurred while fetching poster: {e}")
            raise CustomException(e, sys)

    def recommend_book(self, book_name):
        try:
            book_list = []
            model = pickle.load(open(self.recommendation_config.trained_model_path, 'rb'))
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_object, 'rb'))
            book_id = np.where(book_pivot.index == book_name)[0][0]

            distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=10)

            poster_url, book_metadata = self.fetch_poster(suggestion)

            for i in range(len(suggestion)):
                books = book_pivot.index[suggestion[i]]
                for j in books:
                    book_list.append(j)

            return book_list, poster_url, book_metadata

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
            book_list, poster_url, book_metadata = self.recommend_book(book_name)

            st.subheader("📚 Recommended Books")

            # Row 1: 3 books
            col1, col2, col3 = st.columns(3)
            for i, col in zip(range(1, 4), [col1, col2, col3]):
                with col:
                    html_card = f"""
                    <div style="text-align: center; padding: 10px;" title="More about '{book_metadata[i]['title']}'">
                        <img src="{poster_url[i]}" style="width: 100%; height: auto; border-radius: 10px;" />
                        <div style="margin-top: 10px;">
                            <strong>Title:</strong> {book_metadata[i]['title']}<br>
                            <strong>Author:</strong> {book_metadata[i]['author']}<br>
                            <strong>Year:</strong> {book_metadata[i]['year']}<br>
                            <strong>Publisher:</strong> {book_metadata[i]['publisher']}<br>
                            <strong>Avg Rating:</strong> {book_metadata[i]['avg_rating']}
                        </div>
                    </div>
                    """
                    st.markdown(html_card, unsafe_allow_html=True)

            st.markdown("---")

            # Row 2: 2 books
            col4, col5, col6 = st.columns(3)
            for i, col in zip(range(4, 7), [col4, col5, col6]):
                with col:
                    html_card = f"""
                    <div style="text-align: center; padding: 10px;" title="More about '{book_metadata[i]['title']}'">
                        <img src="{poster_url[i]}" style="width: 100%; height: auto; border-radius: 10px;" />
                        <div style="margin-top: 10px;">
                            <strong>Title:</strong> {book_metadata[i]['title']}<br>
                            <strong>Author:</strong> {book_metadata[i]['author']}<br>
                            <strong>Year:</strong> {book_metadata[i]['year']}<br>
                            <strong>Publisher:</strong> {book_metadata[i]['publisher']}<br>
                            <strong>Avg Rating:</strong> {book_metadata[i]['avg_rating']}
                        </div>
                    </div>
                    """
                    st.markdown(html_card, unsafe_allow_html=True)
            
            st.markdown("---")

            col7, col8, col9 = st.columns(3)
            for i, col in zip(range(7, 10), [col7, col8, col9]):
                with col:
                    html_card = f"""
                    <div style="text-align: center; padding: 10px;" title="More about '{book_metadata[i]['title']}'">
                        <img src="{poster_url[i]}" style="width: 100%; height: auto; border-radius: 10px;" />
                        <div style="margin-top: 10px;">
                            <strong>Title:</strong> {book_metadata[i]['title']}<br>
                            <strong>Author:</strong> {book_metadata[i]['author']}<br>
                            <strong>Year:</strong> {book_metadata[i]['year']}<br>
                            <strong>Publisher:</strong> {book_metadata[i]['publisher']}<br>
                            <strong>Avg Rating:</strong> {book_metadata[i]['avg_rating']}
                        </div>
                    </div>
                    """
                    st.markdown(html_card, unsafe_allow_html=True)
                
            st.markdown("---")

        except Exception as e:
            logger.error(f"Error occurred while recommending engine: {e}")
            raise CustomException(e, sys)
