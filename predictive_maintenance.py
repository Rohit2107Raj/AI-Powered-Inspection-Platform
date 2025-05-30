# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Predictive Maintenance")
# st.title("Predictive Maintenance - RUL Prediction")

# uploaded_file = st.file_uploader("Upload your sensor data CSV", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.subheader("Uploaded Data")
#     st.write(df.head())

#     # Reshape or pad data to (5000, 1) if required
#     data = df.values.flatten()
#     if len(data) < 5000:
#         padded = np.pad(data, (0, 5000 - len(data)), mode='constant')
#     else:
#         padded = data[:5000]

#     input_data = padded.reshape(1, 5000, 1)

#     # Load model
#     try:
#         model = joblib.load("models/random_forest_model.pkl")
#         prediction = model.predict(input_data)[0]

#         st.subheader("Predicted Remaining Useful Life (RUL):")
#         st.success(f"{prediction:.2f} cycles")

#         # Visual trend
#         st.subheader("Degradation Trend (Simulated)")
#         cycles = np.arange(len(data))
#         plt.figure(figsize=(10, 4))
#         plt.plot(cycles, data[:len(cycles)], label='Sensor Signal')
#         plt.axvline(prediction, color='r', linestyle='--', label='Predicted RUL')
#         plt.xlabel("Cycle")
#         plt.ylabel("Sensor Reading")
#         plt.title("Sensor Signal Over Time")
#         plt.legend()
#         st.pyplot(plt)

#     except Exception as e:
#         st.error(f"Failed to load model or make prediction: {e}")
# else:
#     st.info("Awaiting CSV upload.")

import pandas as pd
import numpy as np
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import joblib

st.title("🔧 Predictive Maintenance - RUL Estimation")

uploaded_file = st.file_uploader("Upload a CSV file with sensor readings", type=["csv"])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        # Ensure correct format
        st.write("Input data preview:")
        st.dataframe(df.head())

        # Drop non-numeric columns (if any)
        numeric_df = df.select_dtypes(include=[np.number])

        # Ensure data is 2D
        X = numeric_df.to_numpy()

        # Load model
        # with open("models/random_forest_model.pkl", "rb") as f:
        #     model = pickle.load(f)
        model = joblib.load("models/random_forest_model.pkl")


        predictions = model.predict(X)

        # Output
        st.success("RUL Prediction Completed!")
        st.write(f"📉 Final Estimated RUL: **{predictions[-1]:.2f} cycles**")

        # Plot
        st.subheader("Predicted RUL Trend")
        plt.figure(figsize=(10, 4))
        plt.plot(predictions, label="RUL")
        plt.xlabel("Time Step")
        plt.ylabel("RUL")
        plt.legend()
        st.pyplot(plt.gcf())

    except Exception as e:
        st.error(f"Failed to load model or make prediction: {e}")
