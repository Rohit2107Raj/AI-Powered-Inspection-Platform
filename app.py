# import streamlit as st

# st.set_page_config(page_title="Defect Detection System", layout="centered")

# st.title("Welcome to Defect Detection System")
# st.write("Choose a detector from the sidebar to begin:")
# st.markdown("- 📦 **Casting Defect Detection**")
# st.markdown("- ⚙️ **Fault Detection**")

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Surface Inspection Suite", layout="centered")

st.title("Inspection and Maintenance Prediction App")
st.markdown("""
Welcome to the **Inspection and Maintenance Suite**.

This application offers three main functionalities:

1. 🔍 **Surface Defect Detection**  
2. ⚙️ **Fault Detection in Machine Parts**  
3. 🔧 **Predictive Maintenance using RUL Estimation**

Use the navigation menu on the left sidebar to explore each section.
""")