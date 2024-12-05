import streamlit as st
import pandas as pd
import io
import re

# Configure the page
st.set_page_config(
    page_title="AI Agent For Businesses",
    page_icon="🤖",
    layout="wide"
)

# Title and welcome message
st.title('AI Agent For Businesses')
st.write("Hello, 👋 I am your AI Agent and I am here to help you with your project.")

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = None

# File upload section
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type="csv",
    help="Upload a CSV file to analyze"
)

if uploaded_file is not None:
    # Check file size
    file_size = uploaded_file.size
    if file_size > 10 * 1024 * 1024:  # 10 MB limit
        st.error("File size exceeds 10 MB. Please upload a smaller file.")
    else:
        try:
            # Read the CSV file
            try:
                df = pd.read_csv(uploaded_file, encoding='utf-8', low_memory=False)
            except UnicodeDecodeError:
                st.error("File encoding is not UTF-8. Please save your file with UTF-8.")
            else:
                if df.empty:
                    st.error("The file is empty. Please upload a file with data.")
                else:
                    st.session_state.df = df
                    st.success("File successfully uploaded! 🎉")
                    st.write("### Preview of Your Data")
                    st.dataframe(df.head())
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if 'df' in st.session_state and st.session_state.df is not None:
    st.subheader('Data Exploration')
    df = st.session_state.df

    st.write("**Data Overview**")
    st.write("Let's start by taking a quick look at your dataset. We'll examine the first few rows to understand the structure of the data.")
    st.write("The first rows of your dataset look like this:")
    st.dataframe(df.head())

    st.write("Now, let's also look at the last few rows to ensure no surprises at the end.")
    st.write("Last rows of your dataset look like this:")
    st.dataframe(df.tail())

    st.write("Here's a random sample of your data:")
    st.dataframe(df.sample(5))

    st.write("Next, we'll look at a statistical summary of your dataset. This will give us a sense of the dataset's central tendency, dispersion, and shape.")
    st.write("**Statistical Summary:**")
    st.write(df.describe(include='all'))

    st.write("**Data Information:**")
    st.write("This provides information about the data types and non-null values in each column.")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.write(f"**Data Shape:** {df.shape}")

    # Data Cleaning Section
    st.subheader('Data Cleaning')
    st.write("In this step, we'll clean your data to prepare it for analysis.")

    df_clean = df.copy()

    # Handle missing values
    st.write("**Missing Values**")
    st.write("Missing values can significantly impact analysis and model performance. We'll handle them accordingly.")

    missing_values = df_clean.isnull().sum()
    total_missing = missing_values.sum()
    if total_missing > 0:
        st.write(f"Total missing values in the dataset: {total_missing}")
        # Determine dataset size to decide on handling method
        num_rows = df_clean.shape[0]
        if num_rows > 100000:  # Large dataset
            df_clean = df_clean.dropna()
            st.write("Missing values have been dropped from the dataset.")
        elif num_rows > 1000:  # Moderately sized dataset
            # Impute missing values with mean
            numeric_cols = df_clean.select_dtypes(include=['float64', 'int64']).columns
            for col in numeric_cols:
                df_clean[col].fillna(df_clean[col].mean(), inplace=True)
            st.write("Missing values in numerical columns have been imputed with the mean.")
        else:  # Small dataset
            df_clean.fillna(method='ffill', inplace=True)
            st.write("Missing values have been forward-filled in the dataset.")
        st.write("Missing values handled successfully.")
    else:
        st.write("No missing values found in the dataset.")

    # Remove duplicate records
    duplicates = df_clean.duplicated().sum()
    if duplicates > 0:
        st.write(f"Number of duplicate records in the dataset: {duplicates}")
        df_clean.drop_duplicates(inplace=True)
        st.write("Duplicate entries removed from the dataset.")
    else:
        st.write("No duplicate records found in the dataset.")

    # Convert all string values to lowercase and remove special characters
    object_cols = df_clean.select_dtypes(include=['object']).columns
    if len(object_cols) > 0:
        for col in object_cols:
            df_clean[col] = df_clean[col].str.lower().str.replace(r'[^\w\s]', '', regex=True)
        st.write("All string values converted to lowercase.")
        st.write("Special characters removed from the dataset.")
    else:
        st.write("No string columns found to convert to lowercase or remove special characters.")

    # Encode categorical variables
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        df_clean = pd.get_dummies(df_clean, columns=categorical_cols)
        st.write("Categorical data converted to numerical values.")
    else:
        st.write("No categorical variables found for encoding.")

    # Store cleaned data in session state
    st.session_state.cleaned_data = df_clean
    st.write("Data cleaning is complete.")

    st.subheader('Cleaned Data')
    st.write("Here is the cleaned dataset:")
    st.dataframe(df_clean.head())
