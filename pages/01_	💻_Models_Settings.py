# import os
import streamlit as st
# from streamlit_gsheets import GSheetsConnection
# import requests
from PIL import Image
# from io import BytesIO

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

# Models Comparison Section
with st.expander("Models Comparison"):
    st.markdown('<p class="big-font">Models</p>', unsafe_allow_html=True)
    st.write("Two models are used for the predictions, here are described the parameters we used to train them")
    image = Image.open("media/models_settings.png")
    st.image(image, use_column_width=True)


# YOLO Architecture Section
with st.expander("YOLO Architecture"):
    image = Image.open("media/yolo_architecture.png")
    st.image(image, use_column_width=True)


# Severity Section
with st.expander("Severity of Cracks"):
    st.markdown('<p class="big-font">Severity Setting</p>', unsafe_allow_html=True) # st.write('**Severity Setting**')
    st.markdown("""
    **Computation**:
    Crack Density (Cd) is calculated as the total cracked area divided by the total surface area of the concrete element
    being evaluated.
    \[ C_d = \frac{A_{\text{total}}}{S_{\text{total}}} \]

    **Low Severity**:
    - Crack Density less than 0.1%
    - Indicates minor surface cracks that may not significantly affect structural integrity.

    **Moderate Severity**:

    - Crack Density between 0.1% and 0.5%
    - Represents a more considerable number or width of cracks that could affect durability and may require repair.

    **High Severity**:

    - Crack Density greater than 0.5%
    - Indicates a high density of cracks or very wide cracks that could compromise structural integrity and require immediate attention and repair
    ([American Concrete Institute]
    (https://www.concrete.org/publications/internationalconcreteabstractsportal/m/details/id/18555)
    """)
