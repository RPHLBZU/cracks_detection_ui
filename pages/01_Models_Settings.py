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

## Page Settings

st.title("Settings")
st.markdown('<p class="big-font">Models</p>', unsafe_allow_html=True)
st.write("Two models are used for the predictions, here is described the parameters we used to train them")
# Table of Models
#col1, col2 = st.columns([4, 1])
# with col1:
image = Image.open("media/Table_Model.jpg")
st.image(image, use_column_width=True)



# Severity Setting/ Slider
st.markdown('<p class="big-font">Severity Setting</p>', unsafe_allow_html=True) # st.write('**Severity Setting**')
st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text")
with st.container():
    st.markdown('<div class="slider-container">', unsafe_allow_html=True)
    percent = st.slider(
        '',
        min_value=0,
        max_value=100,
        value=50  # Default 50%
    )
st.markdown('</div>', unsafe_allow_html=True)

st.write(f'You have choosen {percent}%')
