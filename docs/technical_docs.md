# Technical Documentation: Intelligent Data Analysis Assistant

## 1. Architecture Overview
This application follows a modular design pattern, separating concerns into distinct Python modules managed by a central Streamlit frontend (`app.py`).

- **Frontend:** Streamlit
- **Backend Logic:** Python
- **Data Layer:** Pandas/NumPy
- **AI Integration:** REST APIs for Hugging Face (TAPAS) and OpenAI (GPT-3.5).
- **Visualization:** Plotly (interactive) and Matplotlib/Seaborn.
- **NLP:** NLTK library.

## 2. API Integration Details
- **OpenAI:** Uses the `openai` Python library. Requires `OPENAI_API_KEY` environment variable. Handles errors with try-except blocks.
- **Hugging Face:** Uses `requests` to call the Inference API. Requires `HUGGINGFACE_API_TOKEN`.

## 3. Performance & Caching
Streamlit's caching (`@st.cache_data`) is used for functions that are computationally expensive and have deterministic outputs, such as data loading and initial processing. This prevents re-computation on every UI interaction.