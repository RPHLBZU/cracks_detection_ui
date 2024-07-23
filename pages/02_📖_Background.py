import os
import streamlit as st
import requests
from PIL import Image
from io import BytesIO
#import bibtexparser

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

## Page Background

st.title("Background")

    #Data and Models
st.markdown('<p class="big-font">Data and Models</p>', unsafe_allow_html=True)
with st.expander("**Data used for training**"):
    st.markdown("""
        Data Set for Classification:
        - KAGGLE Surface Crack Detection:
        40k images 20k with crack and 20 k without cracks. At the end a sample of 6k images was enough to train the model.
        - SDNET2018:
        Around 13.5k images of this data set were used for testing

        Data Set for Segmentation:
        - Roboflow Crack-Detection:
        These more than 100 images were used for training, validation and test.
        """)

with st.expander("**Pre-Trained Model use**"):
    st.markdown("""- YOLOv8m-seg:
                """)
    image = Image.open("media/yolo_architecture.png")
    st.image(image, use_column_width=True)

    #Ethics
st.markdown('<p class="big-font">Ethics</p>', unsafe_allow_html=True)
with st.expander("**Responsible Use**"):
    st.markdown("""This application is designed to detect cracks in images to assist with structural health monitoring and maintenance. It should be used responsibly and ethically, with the goal of enhancing safety and infrastructure integrity. Users should ensure that the application is used in a manner that respects privacy and data security.""")
with st.expander("**Proper Attribution**"):
    st.markdown("""We acknowledge the use of the Ultralytics YOLOv8 model in this application. Proper credit is given to the authors of this model, as detailed below.""")

    st.write("""The following model was used in this application:""")
    st.write("""- **Authors**: Glenn Jocher, Ayush Chaurasia, and Jing Qiu""")
    st.write("""- **Title**: Ultralytics YOLOv8""")
    st.write("""- **Version**: 8.0.0""")
    st.write("""- **Year**: 2023""")
    st.write("""- **URL**: [Ultralytics YOLOv8 GitHub Repository](https://github.com/ultralytics/ultralytics)""")
    st.write("""- **License**: AGPL-3.0""")
