import os
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Page configuration and CSS
st.set_page_config(page_title="Streamlit Navigation Example", layout="wide")

st.markdown("""
    <style>
    .css-1d391kg {
        background-color: #f8f9fa;
        color: #000000;
    }
    .css-1d391kg div {
        background-color: #000000;
    }
    .css-1d391kg a {
        color: white;
    }
    .stButton>button {
        background-color: #00878D;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton>button:hover {
        background-color: #00878D;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold !important;
    }
    .centered {
        display: flex;
        justify-content: center;
    }
    .slider-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .slider-label {
        font-size: 20px;
        font-weight: bold;
    }
    .stSlider {
        width: 50% !important;
    }
    </style>
""",
unsafe_allow_html=True)

button_html = """
    <style>
    .button {
        background-color: #00878D;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    </style>
    """
## Page Vision

st.title("Vision")
st.write("**Beta Version:**")
st.write(" The beta version of Cracks Detector represents a significant advance in infrastructure monitoring and maintenance. This innovative solution uses advanced image processing techniques and deep learning approaches to efficiently detect and assess cracks in roads and bridges. The Cracks Detector integrates two powerful models for image classification and segmentation: YOLO and a Convolutional Neural Network. These models provide three main outputs in four steps: classification if there are cracks or not, segmentation of the affected areas and determination of the severity of the cracks. This beta version shows the potential to revolutionize infrastructure maintenance by providing accurate and fast analysis to ensure the safety and longevity of our roads and bridges.")
image = Image.open("media/Beta.jpg")
st.image(image, use_column_width=True)

st.write("**Vision and Next Steps:**")
st.write("Our vision for the Cracks Detector is to enable a comprehensive global perspective on and evaluation of infrastructure. Furthermore, we plan to integrate further data sources like 3D to make the assessment of infrastucture as easy as possible. Besides, reinforcement learning is planed to be integrated to improve analysis accuracy and develop adaptive maintenance strategies. With these steps the Cracks Detector should further contribute to revolutionizing the safety and sustainability of infrastructure worldwide.")
st.write("")
col1, col2 = st.columns([2, 2.3])
with col1:
    image = Image.open("media/Vision.jpg")
    st.image(image, use_column_width=True)
with col2:
    st.write("")
