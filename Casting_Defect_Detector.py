import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import PIL

model = load_model("models/casting_defect_model.h5")

st.title("📦 Surface Defect Detection")

uploaded_file = st.file_uploader("Upload a casting image...", type=["jpg", "png", "bmp"])

if uploaded_file is not None:
    img = image.load_img(uploaded_file, target_size=(224, 224))
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    label = "Defective" if prediction[0][0] < 0.7 else "Normal"
    confidence = prediction[0][0] if prediction[0][0] > 0.5 else 1 - prediction[0][0]

    st.subheader(f"Prediction: {label}")
    st.write(f"Confidence: {confidence:.2f}")