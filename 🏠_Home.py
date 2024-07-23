import os
import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from streamlit_option_menu import option_menu


# Define the base URI of the API
#   - Potential sources are in `.streamlit/secrets.toml` or in the Secrets section
#     on Streamlit Cloud
#   - The source selected is based on the shell variable passend when launching streamlit
#     (shortcuts are included in Makefile). By default it takes the cloud API url
# """ if 'API_URI' in os.environ:
#     BASE_URI = st.secrets[os.environ.get('API_URI')]
# else:
#     BASE_URI = st.secrets['cloud_api_uri']
# # Add a '/' at the end if it's not there
# BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
# # Define the url to be used by requests.get to get a prediction (adapt if needed)
# url = BASE_URI + 'predict'

# # Just displaying the source for the API. Remove this in your final version.
# st.markdown(f"Working with {url}")

# st.markdown("Now, the rest is up to you. Start creating your page.")  """


# TODO: Add some titles, introduction, ...

# TODO: display the prediction in some fancy way to the user


# TODO: [OPTIONAL] maybe you can add some other pages?
#   - some statistical data you collected in graphs
#   - description of your product
#   - a 'Who are we?'-page

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
        color: white;
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


#### Show content dependend on selection in navigation bar

## Defining Button state
# Initialize session state for buttons if not already done
if 'Detect if there is a crack' not in st.session_state:
    st.session_state.button1 = False

## Landing Page (Home)
    col1, col2 = st.columns([2.5, 1.5])
    #Left side of page (Text)
    with col1: #Text
        st.title("Analyze cracks with the cracks detector to prevent accitents and to anticipate climate change")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.link_button("Start Cracks Detector", "https://cracksdetectionui-a8f28peutiafdfxnrmdqzw.streamlit.app/Cracks_Detector", type="primary")
    #Right side of page (Picture)
    with col2: #Image
        image = Image.open("media/Unbenannt.jpg")
        st.image(image, use_column_width=True)
