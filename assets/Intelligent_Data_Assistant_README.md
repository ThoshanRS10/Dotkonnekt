# Intelligent Data Analysis Assistant  
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)  
<!--- TODO: Replace with your deployed app's URL --->

An **AI-powered web application** that automates the entire data analysis pipeline.  
This tool allows users to upload data, perform complex analyses, generate visualizations, and even build machine learning models using a simple, intuitive, and conversational interface.  

---

## Demo  
<img width="2721" height="1498" alt="image" src="https://github.com/user-attachments/assets/0a9c93cd-7f5b-499b-91e2-4542e63254f1" />

<img width="2716" height="1500" alt="image" src="https://github.com/user-attachments/assets/73414838-856c-47df-ac0e-bd36629d2d4f" />

<img width="2721" height="1504" alt="image" src="https://github.com/user-attachments/assets/2cf610a9-74f9-4d26-821c-b73cd68aa99d" />

<img width="2723" height="1502" alt="image" src="https://github.com/user-attachments/assets/86de57bb-3847-43bf-9828-951879681eba" />



*(A short GIF showcasing the app's features, like uploading a file and asking a question, would be highly effective here.)*  

---

## 🚀 Key Features  

This assistant combines a powerful data science backend with a user-friendly frontend, augmented by AI from the Hugging Face ecosystem.  

- **Intuitive Web Interface**: Built with Streamlit for a clean, professional, and responsive user experience.  
- **Flexible Data Input**:  
  - Upload local files (`.csv`, `.xlsx`).  
  - Connect directly to live data sources via API URLs.  
- **Automated Data Profiling**: Instant dataset summary including row/column counts, missing values, and automatic data type detection.  
- **Advanced Interactive Visualizations**:  
  - Histograms, Bar Charts, Scatter Plots, Heatmaps.  
  - Custom Geographic Maps with interactive world mapping using latitude/longitude columns.  
- **Natural Language Queries**:  
  - Ask plain-English questions (e.g., *"What is the average price?"*).  
  - Powered by Hugging Face Table-QA models.  
- **AI Explanation System**: Interprets analysis results, explains steps, and simplifies ML model performance metrics.  
- **Automated Machine Learning (AutoML)**:  
  - Detects task type (Classification or Regression).  
  - Builds predictive models with performance metrics (Accuracy, R², etc.).  

---

## 🛠 Tech Stack & Architecture  

- **Frontend**: Streamlit  
- **Backend**: Python  
- **Data Manipulation**: Pandas, NumPy  
- **Data Visualization**: Plotly, Matplotlib, Seaborn  
- **Machine Learning**: Scikit-learn  
- **AI Integration**: Hugging Face Inference API (Table-QA + Text Generation)  
- **Architecture**: Modular design separating data loading, processing, visualization, AI, and ML.  

---

## ⚡ Getting Started  

### Prerequisites  
- Python **3.9+**  
- Git  
- Hugging Face account (for free API token).  

---

### Installation & Setup  

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/intelligent-data-assistant.git
cd intelligent-data-assistant


2. Create & activate a virtual environment

# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


4. Configure Environment Variables

Create a .env file in the root directory.

Add your Hugging Face API token:
HUGGINGFACE_API_TOKEN="hf_YourSecretTokenGoesHere"

Running the Application

streamlit run app.py

The app will open in your browser automatically.

📖 How to Use

Provide Data

Upload .csv or .xlsx files, or

Paste an API URL (default provided).

Data Overview

Get instant dataset summary & profiling.

Visualization

Choose chart type & columns → Generate interactive plots.

Natural Language Query

Ask a question about your data.

AI explains its reasoning & answers.

Machine Learning

Select a target column → Run AutoML.

Get trained model with performance metrics & AI explanation.

Project Structure

/intelligent-data-assistant/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Dependencies
├── .env                    # API keys (ignored in Git)
├── .gitignore              # Git ignore rules
├── README.md               # Documentation
│
├── modules/                # Core backend logic
│   ├── __init__.py
│   ├── data_loader.py
│   ├── processing.py
│   ├── visualization.py
│   ├── nlp.py
│   ├── ai_integration.py
│   └── machine_learning.py
│
├── assets/                 # CSS, images, etc.
│   ├── custom_style.css
│   └── screenshot.png
│
└── .streamlit/
    └── config.toml         # Streamlit theme configuration

