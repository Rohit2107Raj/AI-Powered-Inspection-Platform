import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

# Load the fault detection model
model = load_model("models/vibration_analysis_of_machine_parts.h5")

st.title("Fault Detection from Time-Series Vibration Data")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the CSV file (skip first row if it's header)
        df = pd.read_csv(uploaded_file, header=1)

        # Extract the first column as signal (e.g., a1)
        signal = df.iloc[:, 0].astype(float).values

        # Truncate or pad signal to 5000 samples
        if len(signal) > 5000:
            signal = signal[:5000]
        elif len(signal) < 5000:
            padding = np.zeros(5000 - len(signal))
            signal = np.concatenate([signal, padding])

        # Reshape for model input
        input_data = signal.reshape(1, 5000, 1)

        # Predict
        prediction = model.predict(input_data)[0][0]
        result = "Fault Detected" if prediction > 0.5 else "No Fault"

        st.subheader("Prediction:")
        st.success(f"{result} (Confidence: {prediction:.2f})")

    except Exception as e:
        st.error(f"Error processing file: {e}")

