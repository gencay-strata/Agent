import streamlit as st
import pandas as pd

# Configure the page
st.set_page_config(
    page_title="AI Agent For Businesses",
    page_icon="🤖",
    layout="wide"
)

# Title and welcome message
st.title('AI Agent For Businesses')
st.write("Hello, 👋 I am your AI Agent and I am here to help you with your project.")

# File upload section
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type="csv",
    help="Upload a CSV file to analyze"
)

if uploaded_file is not None:
    try:
        # Read the CSV file
        df = pd.read_csv(uploaded_file, low_memory=False)
        
        # Show success message and preview
        st.success("File successfully uploaded! 🎉")
        st.write("### Preview of Your Data")
        st.dataframe(df.head())
        
    except Exception as e:
        st.error(f"Error reading the file: {str(e)}")
