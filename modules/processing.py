
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data # Use Streamlit's caching for performance
def get_data_summary(df):
    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().sum(),
        "duplicate_rows": df.duplicated().sum()
    }
    return summary

@st.cache_data
def get_column_profiles(df):
    profiles = {}
    for col in df.columns:
        dtype = df[col].dtype
        if pd.api.types.is_numeric_dtype(dtype):
            col_type = 'Numerical'
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            col_type = 'Datetime'
        elif pd.api.types.is_categorical_dtype(dtype) or df[col].nunique() < 20:
            col_type = 'Categorical'
        else:
            col_type = 'Text'
        profiles[col] = col_type
    return profiles

def handle_missing_values(df, strategy='mean', columns=None):
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.columns

    for col in columns:
        if df_copy[col].isnull().any():
            if pd.api.types.is_numeric_dtype(df_copy[col]):
                if strategy == 'mean':
                    fill_value = df_copy[col].mean()
                elif strategy == 'median':
                    fill_value = df_copy[col].median()
                else: # mode
                    fill_value = df_copy[col].mode()[0]
                df_copy[col].fillna(fill_value, inplace=True)
            else: # Categorical/Text
                df_copy[col].fillna(df_copy[col].mode()[0], inplace=True)
    return df_copy

