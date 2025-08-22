# In modules/machine_learning.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import streamlit as st

@st.cache_data(show_spinner="Training Machine Learning model...")
def auto_ml(df, target_column):
    """
    Runs an automated machine learning pipeline.
    Detects task type, preprocesses data, trains a model, and evaluates it.
    """
    df_clean = df.copy()
    
    # --- Basic Preprocessing ---
    for col in df_clean.select_dtypes(include=['object']).columns:
        if col != target_column:
            le = LabelEncoder()
            # Ensure we only transform non-missing values if any
            if df_clean[col].notna().any():
                df_clean[col] = df_clean[col].astype(str) # Convert all to string before encoding
                df_clean[col] = le.fit_transform(df_clean[col])
    
    df_clean.dropna(inplace=True)

    if target_column not in df_clean.columns or df_clean.empty:
        return None, "Target column not found after cleaning or dataframe is empty. This often happens if the target column has too many missing values.", None

    X = df_clean.drop(target_column, axis=1)
    y = df_clean[target_column]
    
    if len(X) < 10: # Not enough data to train
        return None, "Not enough data to train a model after cleaning (less than 10 rows).", None

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # --- Task Detection and Model Training ---
    if y.nunique() < 20 and y.dtype != 'float':
        task = "Classification"
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        performance = {"Accuracy": accuracy_score(y_test, preds)}
    else:
        task = "Regression"
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        performance = {
            "R-squared (R2)": r2_score(y_test, preds),
            "Mean Squared Error (MSE)": mean_squared_error(y_test, preds)
        }
        
    # --- THE CRUCIAL FIX IS HERE ---
    return task, performance, model