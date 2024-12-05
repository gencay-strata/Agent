# AI Agent for Businesses

Welcome to the **AI Agent for Businesses** project repository! This project provides a step-by-step guide to building a modular and interactive AI system tailored for simplifying data analysis and machine learning workflows for businesses.

---

## 🌟 Project Flow and Components

### **1. User Input**
The project begins with a simple interface where users can:
- Upload datasets for analysis.
- Provide input on models, metrics, and visualizations they'd like to use.

### **2. Data Loading**
This stage involves:
- Loading the uploaded data into a Pandas DataFrame.
- Ensuring compatibility by handling common file-related issues (e.g., encoding and empty files).

### **3. Data Exploration**
Here, we implement basic exploratory data analysis (EDA) to:
- Display key summary statistics and visualizations.
- Provide users with a better understanding of their dataset.

### **4. Data Cleaning**
Data cleaning includes:
- Handling duplicate records.
- Removing special characters.
- Encoding categorical variables.
- Preparing the dataset for downstream processes.

*Note: The first four sections focus solely on data processing and do not involve any AI components.*

---

### **5. Model Testing**
The Model Testing stage automates the following processes:
- **Model Selection**: Tests multiple machine learning models.
- **Preprocessing**: Includes train-test splitting, normalization, dimensionality reduction, and target column selection.
- **Output**: Results of this stage serve as input for validation.

### **6. Model Validation**
This section evaluates the validity of machine learning models by:
- Checking dataset assumptions specific to each model (e.g., linearity, independence, distribution).
- Returning "Passed" or "Failed" status for every assumption.
- Filtering out models that fail to meet the required criteria.

---

### **7. Model Visualization**
Users can visualize the performance of models that passed the validation stage. This includes:
- Selecting metrics (e.g., accuracy, precision, recall).
- Choosing chart types (e.g., bar charts, line graphs).
- Interactive outputs that showcase model performance insights.

### **8. Model Performance**
The Model Performance Agent is the final stage, where:
- **Performance Metrics**: Key statistics (e.g., accuracy, precision, recall, F1-score, mean squared error) are presented.
- **Text Explanations & Insights**: User-friendly interpretations highlight strengths, weaknesses, and suitability of each model.
- **Preparation for Downstream Systems**: The results are packaged for use in other workflows, such as:
  - Sending insights via email.
  - Creating dashboards.
  - Integrating results into API workflows.

## 🚀 Getting Started

1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
