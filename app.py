import streamlit as st
import pandas as pd
from dotenv import load_dotenv

# Import all your modules
from modules import (
    data_loader,
    processing,
    visualization,
    nlp,
    ai_integration,
    machine_learning
)

# Load environment variables from .env file
load_dotenv()

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Intelligent Data Analysis Assistant",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- 2. LOAD CUSTOM CSS ---
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Custom CSS file not found. Using default styles.")

load_css("assets/custom_style.css")

# --- 3. INITIALIZE SESSION STATE ---
if 'df' not in st.session_state:
    st.session_state.df = None

# --- 4. SIDEBAR - DATA INPUT ---
st.sidebar.title("Data Input")
input_method = st.sidebar.radio("Choose your data source", ["Upload a File", "Connect to API"])

# Conditional UI based on user's choice
if input_method == "Upload a File":
    uploaded_file = st.sidebar.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file:
        df_loaded = data_loader.load_data(uploaded_file)
        if df_loaded is not None:
            st.session_state.df = df_loaded
else: # Connect to API
    api_url = st.sidebar.text_input(
        "Enter API URL",
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    )
    if st.sidebar.button("Fetch Data"):
        df_loaded = data_loader.load_data_from_api(api_url)
        if df_loaded is not None:
            st.session_state.df = df_loaded

# --- 5. MAIN APPLICATION BODY ---
st.title("Intelligent Data Analysis Assistant")

if st.session_state.df is not None:
    df = st.session_state.df
    st.header("Data Preview")
    st.dataframe(df.head())

    # --- Create Tabs for Different Analyses ---
    tab1, tab2, tab3, tab4 = st.tabs(["Data Overview", "Visualization", "Natural Language Query", "Machine Learning"])

    # --- TAB 1: Data Overview ---
    with tab1:
        st.subheader("Data Summary")
        summary = processing.get_data_summary(df)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Rows", summary['rows'])
        col2.metric("Columns", summary['columns'])
        col3.metric("Missing Values", summary['missing_values'])
        col4.metric("Duplicate Rows", summary['duplicate_rows'])

        st.subheader("Column Profiles")
        column_profiles = processing.get_column_profiles(df)
        st.json(column_profiles)

    # --- TAB 2: Visualization ---
    with tab2:
        st.subheader("Create a Visualization")

        column_profiles = processing.get_column_profiles(df)
        numeric_cols = [col for col, type in column_profiles.items() if type == 'Numerical']
        categorical_cols = [col for col, type in column_profiles.items() if type == 'Categorical']

        plot_type = st.selectbox(
            "Select Plot Type",
            ["Histogram", "Bar Chart", "Scatter Plot", "Heatmap", "Geographic Map"]
        )

        if plot_type == "Histogram" and numeric_cols:
            hist_col = st.selectbox("Select a numerical column", numeric_cols)
            fig = visualization.plot_histogram(df, hist_col)
            st.plotly_chart(fig, use_container_width=True)

        elif plot_type == "Bar Chart" and categorical_cols:
            bar_col = st.selectbox("Select a categorical column", categorical_cols)
            fig = visualization.plot_bar(df, bar_col)
            st.plotly_chart(fig, use_container_width=True)

        elif plot_type == "Scatter Plot" and len(numeric_cols) >= 2:
            x_axis = st.selectbox("Select X-axis", numeric_cols, index=0)
            y_axis = st.selectbox("Select Y-axis", numeric_cols, index=1)
            fig = visualization.plot_scatterplot(df, x_axis, y_axis)
            st.plotly_chart(fig, use_container_width=True)

        elif plot_type == "Heatmap":
            fig = visualization.plot_heatmap(df)
            if fig: st.pyplot(fig)
            else: st.warning("You need at least two numerical columns for a correlation heatmap.")

        elif plot_type == "Geographic Map" and len(numeric_cols) >= 2:
            st.write("Select columns for Latitude and Longitude.")
            lat_col = st.selectbox("Select Latitude column", numeric_cols, index=0)
            lon_col = st.selectbox("Select Longitude column", numeric_cols, index=1)
            color_col = st.selectbox("Color by (optional)", [None] + numeric_cols + categorical_cols)
            fig = visualization.plot_geo_map(df, lat_col, lon_col, color_col)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Please select a plot type. Some plots may require specific column types (e.g., numerical or categorical).")

    # --- TAB 3: Natural Language Query ---
    with tab3:
        st.subheader("Ask a Question About Your Data")
        natural_query = st.text_input("e.g., 'What is the average price?'", key="natural_query_input")

        if natural_query:
            with st.spinner("The AI is thinking... this may take a moment."):
                explanation_prompt = f"The user asked: '{natural_query}'. Explain what kind of data analysis this question implies in simple terms."
                explanation = ai_integration.get_ai_explanation(explanation_prompt)
                
                # --- THE FIX IS HERE ---
                st.info(f"**AI Assistant's Plan:** {explanation}", icon="💡") # Replaced brain with lightbulb

                answer = ai_integration.ask_question_on_data(st.session_state.df, natural_query)
                st.success(f"**Answer:** {answer}", icon="✅")

    # --- TAB 4: Machine Learning ---
    # --- TEMPORARY DEBUGGING VERSION for Tab 4 ---
# --- FINAL, ROBUST VERSION for Tab 4 ---
with tab4:
    st.subheader("Automated Machine Learning")
    
    df_for_ml = df.copy() 
    target_column = st.selectbox(
        "Select the Target Column to Predict", 
        df_for_ml.columns, 
        key="ml_target_column"
    )
    
    if st.button("Run AutoML to Predict '" + target_column + "'"):
        # This function call is the source of the potential error
        task, performance, model = machine_learning.auto_ml(df_for_ml, target_column)
        
        # THE CRUCIAL CHECK: We check if 'task' is valid (not None).
        # This is the gatekeeper that prevents the crash.
        if task is not None:
            # If we are inside this block, 'performance' is guaranteed to be a dictionary.
            st.success(f"Successfully ran AutoML for a **{task}** task.")
            
            explanation_prompt = (
                f"The user ran an ML model to predict '{target_column}'. The task was {task}. "
                f"The performance is {performance}. Explain what these results mean in simple terms."
            )
            
            with st.spinner("AI is generating an explanation of the results..."):
                explanation = ai_integration.get_ai_explanation(explanation_prompt)
                st.info("AI-Powered Explanation:", icon="💡")
                st.write(explanation)

            st.subheader("Model Performance")
            # This loop is now 100% safe.
            for metric, value in performance.items():
                st.metric(label=metric, value=f"{value:.4f}")
        
        else:
            # If 'task' is None, we know the function failed.
            # In this case, 'performance' holds the error string, which we display.
            st.error(f"Could not run AutoML. The function returned this error: {performance}")
            st.info("This often happens if the target column contains too many empty values (NaNs), which are removed during data cleaning.")
    else:
        st.info("Please provide a data source using the sidebar to begin analysis.")