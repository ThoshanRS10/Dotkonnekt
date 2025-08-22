# modules/data_loader.py

import pandas as pd
import streamlit as st
import openpyxl  # This import is necessary for pandas to read .xlsx files

@st.cache_data(show_spinner="Loading and caching data...")
def load_data(uploaded_file):
    """
    Loads data from an uploaded file (CSV or Excel) into a pandas DataFrame.
    Uses Streamlit's caching to improve performance by not reloading the same file.

    Args:
        uploaded_file: The file object from st.file_uploader.

    Returns:
        A pandas DataFrame with the loaded data, or None if loading fails.
    """
    if uploaded_file is None:
        return None

    try:
        # Check the file extension to use the correct pandas function
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xls', '.xlsx')):
            # The 'openpyxl' engine is required for modern Excel files
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        else:
            # Show an error message in the app for unsupported formats
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            return None
        
        return df

    except Exception as e:
        # Show a generic error message if pandas fails to parse the file
        st.error(f"Error reading the file: {e}")
        return None