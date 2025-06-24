# 📘 Book Recommender App

![Book Universe](https://undsgn.com/wp-content/uploads/2018/06/xy55bl5mzam-uai-1600x900.jpg)

---

## 🌟 Overview

The **Book Recommender App** suggests books similar to your interests based on user ratings and book metadata. Leveraging collaborative filtering and machine learning, it provides high-quality recommendations in real time through an elegant web interface. It is an intelligent and personalized book recommendation system that helps you discover your next favorite read. Built using collaborative filtering techniques and deployed with a modern, interactive Streamlit interface.

---

## ✅ Features

- 🔍 **AI-based Book Recommendations**  
  Powered by a K-Nearest Neighbors (KNN) model trained on real-world user ratings.

- 🎨 **Interactive UI with Streamlit**  
  Clean, responsive, and visually appealing front-end for easy interaction.

- 📊 **Live Model Training**  
  Ability to retrain the model with updated data from the UI.

- 🐳 **Dockerized Setup**  
  Fully containerized for consistent deployment and scalability.

- 📁 **DVC Integration**  
  For version-controlled dataset and model tracking (compatible with DagsHub).

---

<details>
<summary>Click to expand/collapse project tree</summary>
  
```
Directory structure:
└── arpitkadam-book-recommender-app/
    ├── README.md
    ├── __init__.py
    ├── app.py
    ├── demo.py
    ├── Dockerfile
    ├── dvc.yaml
    ├── LICENSE
    ├── main.py
    ├── requirements.txt
    ├── setup.py
    ├── template.py
    ├── .dockerignore
    ├── .dvcignore
    ├── artifacts/
    │   ├── data_ingestion/
    │   │   ├── ingested_data/
    │   │   │   ├── BX-Book-Ratings.csv
    │   │   │   ├── BX-Books.csv
    │   │   │   └── BX-Users.csv
    │   │   └── raw_data/
    │   │       └── archive.zip
    │   ├── data_transformation/
    │   │   └── transformed_data/
    │   │       ├── book_names.pkl
    │   │       ├── book_pivot.pkl
    │   │       ├── final_ratings.pkl
    │   │       └── transformed_data.pkl
    │   ├── data_validation/
    │   │   ├── clean_data/
    │   │   │   └── final_ratings.csv
    │   │   └── serialized_data/
    │   │       └── final_ratings.pkl
    │   └── model_trainer/
    │       └── model.pkl
    ├── config/
    │   └── config.yaml
    ├── research/
    │   ├── archive.zip
    │   ├── BX-Book-Ratings.csv
    │   ├── BX-Books.csv
    │   ├── BX-Users.csv
    │   ├── notebook.ipynb
    │   └── artifacts/
    │       ├── book_names.pkl
    │       ├── book_pivot.pkl
    │       ├── final_ratings.pkl
    │       └── model.pkl
    ├── src/
    │   ├── __init__.py
    │   ├── components/
    │   │   ├── __init__.py
    │   │   ├── data_ingestion.py
    │   │   ├── data_transformation.py
    │   │   ├── data_validation.py
    │   │   └── model_trainer.py
    │   ├── configuration/
    │   │   ├── __init__.py
    │   │   └── configuration.py
    │   ├── constants/
    │   │   └── __init__.py
    │   ├── entity/
    │   │   ├── __init__.py
    │   │   ├── artifact_entity.py
    │   │   └── config_entity.py
    │   ├── exception/
    │   │   └── __init__.py
    │   ├── logger/
    │   │   └── __init__.py
    │   ├── pipeline/
    │   │   ├── __init__.py
    │   │   ├── recommendation_pipeline.py
    │   │   └── training_pipeline.py
    │   └── utils/
    │       └── __init__.py
    └── .dvc/
        ├── config
        └── .gitignore

```
</details>

---

## ⚙️ Technologies Used

- 🐍 Python 3.10+
- 📚 Pandas, NumPy, Scikit-learn
- 📈 Streamlit
- 🧠 Machine Learning (KNN-based Collaborative Filtering)
- 📦 Docker & DVC
- ☁️ DagsHub (for remote data storage)

---

## 🐳 Docker Setup

### 1. Build the Docker image

```bash
docker build -t arpitkadam/book-recommender-app .
```

### 2. Run the container locally
```bash
docker run -p 8501:8501 arpitkadam/book-recommender-app
```

The app will be accessible at:
📍 http://localhost:8501

---

## 📦 Installation & Setup (For Local Use Without Docker)

### 1. Clone the repository
```bash
git clone https://github.com/ArpitKadam/Book-Recommender-App.git
cd Book-Recommender-App
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit app
```bash
streamlit run main.py
```

---

## 🚀 How to Use
- Go to the Recommend page.
- Select a book you’ve read or liked from the dropdown.
- Click on Recommend Books to get AI-powered suggestions.
- (Optional) Use the Train Model button to retrain the model on latest data.

---

## 🤝 Contributions

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request

---

## 📄 License

This project is licensed under the [GNU General Public License v3.0](https://github.com/ArpitKadam/Book-Recommender-App/blob/main/LICENSE).

---

## 📬 Contact

- Email: [arpitkadam922@gmail.com](mailto:arpitkadam922@gmail.com)
- GitHub: [ArpitKadam](https://github.com/ArpitKadam)
- Personal: [ArpitKadam](https://arpit-kadam.netlify.app/)





