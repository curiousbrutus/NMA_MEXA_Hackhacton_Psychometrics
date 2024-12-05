import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai

# Google Gemini API setup
GOOGLE_API_KEY = 'AIzaSyAfyh2dwrsP2Iv2WcXEfd6bTnJinnCvDsc'  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Helper function for Gemini analysis
def gemini_analysis(wearable_data, conversational_data, baseline_data, current_data, prompt_template):
    """
    Function to perform analysis using Gemini AI based on provided datasets and prompt.
    """
    prompt = prompt_template.format(
        wearable_data=wearable_data.head(5).to_string(),
        conversational_data=conversational_data.head(5).to_string(),
        baseline_data=baseline_data.head(5).to_string(),
        current_data=current_data.head(5).to_string()
    )

    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text

# Streamlit app UI
st.title('AI-Driven Mental Health Insights')

# File upload for the datasets
wearable_file = st.file_uploader("Upload Wearable Data CSV", type="csv")
conversational_file = st.file_uploader("Upload Conversational Data CSV", type="csv")
baseline_file = st.file_uploader("Upload Baseline Data CSV", type="csv")
current_file = st.file_uploader("Upload Current Data CSV", type="csv")

if wearable_file and conversational_file and baseline_file and current_file:
    # Read datasets
    wearable_data = pd.read_csv(wearable_file)
    conversational_data = pd.read_csv(conversational_file)
    baseline_data = pd.read_csv(baseline_file)
    current_data = pd.read_csv(current_file)

    # Check if datasets are loaded correctly
    if wearable_data.empty or conversational_data.empty or baseline_data.empty or current_data.empty:
        st.error("One of the datasets is empty. Please check your input files.")
    else:
        # Display dataframes
        st.subheader('Wearable Data')
        st.write(wearable_data.head())
        
        st.subheader('Conversational Data')
        st.write(conversational_data.head())
        
        st.subheader('Baseline Data')
        st.write(baseline_data.head())
        
        st.subheader('Current Data')
        st.write(current_data.head())

        # Define the prompt template
        prompt_template = """
        You are an advanced AI specializing in mental health analytics. Your task is to assist therapists by analyzing multimodal data collected from their patients. 
        You will evaluate patterns in wearable device data and conversational inputs to identify trends, provide insights, and suggest areas for further attention.

        Dataset Overview:
        1. Wearable Data: 
        {wearable_data}

        2. Conversational Data:
        {conversational_data}

        3. Baseline Data (e.g., remission phase):
        {baseline_data}

        4. Current Data:
        {current_data}

        Tasks:
        1. Analyze trends in wearable data to identify stress, fatigue, or irregular activity patterns.
        2. Correlate conversational insights (e.g., sentiment analysis) with wearable trends.
        3. Highlight deviations from baseline trends that require therapist attention.
        4. Provide a concise summary of findings and actionable recommendations.

        Output Format:
        1. Summary of trends (patterns and deviations).
        2. Key insights correlating wearable and conversational data.
        3. Recommendations for therapist follow-up or patient care adjustments.
        4. Confidence levels for findings.

        - Avoid diagnosing patients directly but provide clinical advice to therapists. 
        """

        # Run Gemini AI analysis
        with st.spinner('Analyzing data...'):
            generated_insights = gemini_analysis(wearable_data, conversational_data, baseline_data, current_data, prompt_template)
        
        # Display generated insights
        st.subheader('AI Generated Insights')
        st.write(generated_insights)

        # Visualization of data trends using Matplotlib
        st.subheader('Data Visualization')

        fig, axes = plt.subplots(3, 3, figsize=(15, 10))  # Create a 3x3 grid of subplots
        fig.suptitle('Data Analysis', fontsize=16)  # Set main title

        # Plot each variable in a separate subplot
        axes[0, 0].plot(wearable_data['Date'], wearable_data['Sleep Hours'], label='Sleep Hours', marker='o')
        axes[0, 1].plot(wearable_data['Date'], wearable_data['REM Sleep (%)'], label='REM Sleep (%)', marker='o')
        axes[0, 2].plot(wearable_data['Date'], wearable_data['Deep Sleep (%)'], label='Deep Sleep (%)', marker='o')
        axes[1, 0].plot(wearable_data['Date'], wearable_data['Light Sleep (%)'], label='Light Sleep (%)', marker='o')
        axes[1, 1].plot(wearable_data['Date'], wearable_data['Screen Time (hours)'], label='Screen Time (hours)', marker='o')
        axes[1, 2].plot(wearable_data['Date'], wearable_data['Steps'], label='Steps', marker='o')
        axes[2, 0].plot(wearable_data['Date'], wearable_data['Calories Burned'], label='Calories Burned', marker='o')
        axes[2, 1].plot(wearable_data['Date'], wearable_data['Running Distance (km)'], label='Running Distance (km)', marker='o')
        axes[2, 2].plot(wearable_data['Date'], wearable_data['Exercise Time (minutes)'], label='Exercise Time (minutes)', marker='o')

        # Set labels and titles for each subplot
        for ax in axes.flat:
            ax.set_xlabel('Date')
            ax.set_ylabel('Value')
            ax.legend(loc='upper left', fontsize='small')  # Adjust legend position if needed
            ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout for title and subplots
        st.pyplot(fig)
