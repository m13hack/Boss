import streamlit as st
from src.capture.mailhog_client import fetch_emails
from src.features.extract_features import extract_features
from src.ml.predict import load_model, predict

st.title("Live Email Spoofing Detector")

model = load_model()

emails = fetch_emails()
for email in emails:
    features = extract_features(email)
    result = predict(model, features)
    st.write(f"Subject: {email['Content']['Headers'].get('Subject', [''])[0]}")
    st.write(f"Prediction: {'⚠️ Spoofed' if result == 1 else '✅ Legitimate'}")
    st.write("---")
