# streamlit_app.py
import streamlit as st
from src.pipeline.recommendation_pipeline import Recommendation
import pickle

# Load once
recommendation = Recommendation()
book_list = pickle.load(open(recommendation.recommendation_config.book_name_serialized_object, 'rb')).to_list()

# Set Streamlit page config
st.set_page_config(
    page_title="Book Recommender App",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Recommend", "Importance of Books", "Developer"))

# Home Page
if page == "Home":
    st.markdown("""
        <style>
            .big-font {
                font-size: 38px !important;
                font-weight: bold;
                text-align: center;
                color: #000000;
            }
            .sub-font {
                font-size: 20px !important;
                text-align: center;
                color: #333333;
            }
            .card {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 25px;
                padding: 20px;
                box-shadow: 4px 4px 12px rgba(0,0,0,0.5);
                margin-bottom: 20px;
                color: #000000;
            }
        </style>
    """, unsafe_allow_html=True)


    st.markdown("<p class='big-font'>📖 Welcome to the Book Recommender App: Your Gateway to Book Nirvana</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-font'>Discover personalized book recommendations powered by intelligent AI Alogorithms.</p>", unsafe_allow_html=True)

    st.image("https://undsgn.com/wp-content/uploads/2018/06/xy55bl5mzam-uai-1600x900.jpg", use_container_width=True, caption="✨ Every book is a new universe waiting to be explored.")

    st.markdown("## 🚀 Why Use This App?")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card'>
        <h4>🔍 Personalized Discovery</h4>
        <p>Our AI recommends books tailored to your taste — no fluff, just what you'll love.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
        <h4>📊 Based on Real Reader Ratings</h4>
        <p>We use real-world data and smart filtering techniques to suggest only top-rated titles.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
        <h4>🎯 Focused on You</h4>
        <p>Pick any book you’ve enjoyed, and we'll find 9 others you'll devour next.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
        <h4>⚡ Fast, Simple & Beautiful</h4>
        <p>Minimal UI. Instant results. Because your time is better spent reading.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 🌐 Technologies Behind the Magic")
    st.markdown("""
    <ul>
    <li>🧠 <b>Machine Learning:</b> KNN-based collaborative filtering</li>
    <li>🧰 <b>Tech Stack:</b> Streamlit, Pandas, Scikit-learn</li>
    <li>📦 <b>Model Training:</b> Dynamic pipeline to update recommendations</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("## 📚 Books Change Lives")
    st.image("https://i.fbcd.co/products/original/a-reader-lives-a-thousand-lives-before-he-dies-svg-1625827473046339000-2167a23e2a5bbfc3cacef9aaf02a0e1f5176304ee78d4f2997e06020e24aac72.jpg", use_container_width=True)
    st.markdown("""
    > __<span style='font-size: 20px;'>"A reader lives a thousand lives before he dies. The man who never reads lives only one."</span>__  
    <span style='font-size: 20px;'>– George R. R. Martin</span>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align:center;'>✨ Ready to Find Your Next Favorite Book?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Head over to the <b>Recommend</b> page and dive in!</p>", unsafe_allow_html=True)

    st.markdown("""
        <style>
            .footer {
                text-align: center;
                font-size: 15px;
                color: #000000;
                margin-top: 30px;
            }

            .footer a {
                color: #000000;
                text-decoration: none;
                font-weight: bold;
            }

            .footer a:hover {
                text-decoration: underline;
            }

            .heart {
                animation: pulse 1.5s infinite;
                color: red;
            }

            @keyframes pulse {
                0% { transform: scale(1); opacity: 0.8; }
                50% { transform: scale(1.2); opacity: 1; }
                100% { transform: scale(1); opacity: 0.8; }
            }
        </style>
        <div class='footer'>
            Crafted with <span class='heart'>❤️</span> by <a href='https://arpit-kadam.netlify.app/' target='_blank'>Arpit Kadam</a>
        </div>
    """, unsafe_allow_html=True)

# Recommendation Page
elif page == "Recommend":
    st.markdown("""
        <style>
            .recommend-title {
                font-size: 36px;
                text-align: center;
                color: #000000;
                font-weight: bold;
                margin-bottom: 0.5rem;
            }

            .recommend-subtitle {
                text-align: center;
                font-size: 18px;
                color: #000000;
                margin-bottom: 2rem;
            }

            .recommend-card {
                background-color: #ffffff;
                padding: 1.5rem;
                border-radius: 15px;
                box-shadow: 2px 2px 12px rgba(0,0,0,0.08);
                margin-top: 1rem;
                margin-bottom: 2rem;
            }

            .recommend-footer {
                text-align: center;
                font-size: 14px;
                color: #000000;
                margin-top: 50px;
            }

            .center-button {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }

            .pulse-btn {
                animation: pulse 2s infinite;
            }

            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='recommend-title'>📘 Book Recommendation System</div>", unsafe_allow_html=True)
    st.markdown("<div class='recommend-subtitle'>Find books similar to the ones you already love.</div>", unsafe_allow_html=True)

    st.markdown("### 🔧 Model Control")
    if st.button("🚀 Train Model", help="Click to retrain the recommendation engine with latest data"):
        recommendation.train_engine()
        st.success("✅ Model training completed successfully!")

    st.markdown("### 📚 Choose Your Book")
    book_name = st.selectbox("📖 Select a book to get similar recommendations", book_list)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("🔍 Recommend Books", type="primary", help="Get AI-powered book recommendations!", key="recommend"):
        recommendation.recommend_engine(book_name)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p class='recommend-footer'>✨ Powered by NN + Collaborative Filtering · Optimized by Arpit Kadam</p>", unsafe_allow_html=True)

# Importance of Books Page
elif page == "Importance of Books":
    st.markdown("""
        <style>
            .importance-container {
                background: linear-gradient(145deg, #fdfbfb 10%, #ebedee 100%);
                padding: 25px;
                border-radius: 40px;
                box-shadow: 0 10px 45px rgba(0,0,0,0.40);
                margin-top: 10px;
                font-family: 'Segoe UI', sans-serif;
            }
            .importance-title {
                font-size: 36px;
                font-weight: 700;
                color: #4B0082;
                text-align: center;
                margin-bottom: 20px;
            }
            .importance-text {
                font-size: 18px;
                color: #333;
                text-align: justify;
                line-height: 1.6;
                margin-bottom: 25px;
            }
            .benefits-list {
                font-size: 17px;
                color: #222;
                padding-left: 25px;
                line-height: 1.8;
            }
            .quote-box {
                background-color: #fff;
                border-left: 5px solid #4B0082;
                padding: 15px 25px;
                font-style: italic;
                font-size: 18px;
                margin-top: 30px;
                border-radius: 15px;
                color: #555;
                box-shadow: 6px 6px 16px rgba(0,0,0,0.2);
                text-align: center;
            }
            .quote-author {
                font-size: 16px;
                margin-top: 10px;
                text-align: right;
                color: #444;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="importance-container">
            <div class="importance-title">📚 Why Books Matter</div>
            <div class="importance-text">
                Books are timeless vessels of wisdom and wonder. Whether you're escaping into a fantasy world or learning how to master a skill,
                books unlock worlds within us and around us. Reading not only fuels your intellect, but also deepens your empathy and imagination.
            </div>
            <div class="importance-text"><strong>✨ Benefits of Reading:</strong></div>
            <ul class="benefits-list">
                <li>🧠 Stimulates the brain and enhances mental flexibility</li>
                <li>✍️ Improves vocabulary and writing skills</li>
                <li>🧘 Reduces stress and supports mental well-being</li>
                <li>🤝 Builds empathy by immersing you in other perspectives</li>
                <li>🎓 Encourages lifelong learning and curiosity</li>
            </ul>
            <div class="quote-box">
                “There is more treasure in books than in all the pirate's loot on Treasure Island.”
                <div class="quote-author">– Walt Disney</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.image("https://www.southernliving.com/thmb/yJQb7XBAaQ03_m5cjO0_Yyb_Lj0=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/SL-READING-QUOTES-1_WALTDISNEY1-d66677172fc94117ae0b84c5a1b20350.jpg", 
             use_container_width=True, caption="📖 Read more. Live more.")



# Developer Page
elif page == "Developer":
    st.markdown("""
        <style>
            .dev-title {
                text-align: center;
                font-size: 28px;
                font-weight: bold;
                color: #4B0082;
                margin-top: 20px;
                margin-bottom: 20px;
            }
            .dev-section {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.05);
                color: #000000;
                font-size: 17px;
                line-height: 1.6;
                text-align: center;
            }
            .dev-links a {
                color: #4B0082;
                text-decoration: none;
                margin: 0 10px;
                font-weight: 500;
                text-align: right;
            }
            .footer-dev {
                text-align: center;
                margin-top: 20px;
                font-size: 15px;
                color: #333;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='dev-title'>👨‍💻 Developer Info</div>", unsafe_allow_html=True)

    st.markdown("""
        <div class='dev-section'>
            <p><strong>Arpit Sachin Kadam</strong><br>
            Final Year AIML Student, Shivajrao S. Jondhale College of Engineering<br>
            Passionate about AI, ML, and building intelligent systems that solve real-world problems.</p>
        </div>

        <div class='dev-links'>
            🔗 <a href='https://github.com/arpitkadam' target='_blank' text-align: center >GitHub</a> |
            🔗 <a href='https://arpit-kadam.netlify.app/' target='_blank'>Portfolio</a> |
            🔗 <a href='https://www.linkedin.com/in/arpitkadam/' target='_blank'>LinkedIn</a> |
            🔗 <a href='https://buymeacoffee.com/arpitkadam' target='_blank'>Buy me a Coffee</a> |
            🔗 <a href='https://dev.to/arpitkadam' target='_blank'>Dev.io</a> |
            🔗 <a href='arpitkadam922@gmail.com' target='_blank'>Gmail</a>
        </div>

        <div class='footer-dev'>
            💡 Always Learning · Always Building · Made with ❤️ by Arpit
        </div>
    """, unsafe_allow_html=True)

