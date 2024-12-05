### GigaGrams @ NMA_MEXA_Hackhacton_Psychometrics
## Symptom Tracking & Assistance for Mental Health Workers

This repo contains the code generated as part of the MEXA Hackathon by team GigaGrams. 

Our project aimed to leverage the power of data that can be passively collected through wearable devices and LLMs in assisting mental health professionals in tracking symptoms of their patients.

## Project overview
When working with patients, mental health practicioners rely mostly on self-report data gathered during therapy sessions, which are often sporadic. As a result, the insight into the fluctuations in symptom type and intensity in between sessions is limited, possibly affecting the progress of treatment, as well as the level of understanding of the condition of each individual patient. A solution we propose is tracking the fluctuations of symptoms across time using a variety of methods and generating reports on the relevant symptoms to the clinician using LLMs.  Our project integrates data collected in real-time from wearable devices (such as heart rate variability, sleep patterns, and activity) with AI-driven insights.
**This solution aims to assist individuals and clinicians by providing continuous symptom tracking, helping detect deviations and offering timely interventions to improve treatment outcomes.
**
Multimodal Data Integration:

Wearable Data: Sleep patterns, HRV, activity levels, heart rate, and electrodermal activity (EDA).

Self-Reported Data: Mood logs, symptom checklists, and daily journaling.

Voice Input: Daily sentiment analysis based on spoken input, providing additional insights. Speech cadence analysis.
AI for Mental Health:

Utilizes Google Gemini AI for mental health diagnostics, leveraging the AI model for personalized feedback and intervention suggestions.

Voice Sentiment Analysis: Sentiment and mood analysis through the user’s spoken words, analyzed with advanced NLP techniques.

Technologies that could be integrated at later stages:
Google Gemini AI: Used for generating insights and analyzing multimodal mental health data.
Google Cloud Speech-to-Text: For transcribing voice data into text for analysis.
Google Dialogflow: Used to create voice-based conversational agents.
Python: Main programming language for data analysis, model integration, and API interaction.
Pandas, NumPy, Matplotlib: Data handling and visualization tools.
Google Cloud APIs: Integration with Google Health Connect (formerly Google Fit) for wearable data.


* To run:

pip install streamlit pandas matplotlib google-generativeai

streamlit run app.py


*Code overview

1.33Wearable_MEXA_Hackathon_Gemini_Example.ipynb - main code base 

app.py - interface for uploading datafiles and visualising data

Smooth_data_generation.ipynb - script used for generating artificial data simulating symptoms  associated with manic/depressive/euthymic episodes in bipolar disorder

*.csv files - sample data sets generated/used during development

