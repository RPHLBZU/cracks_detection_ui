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
    </style>
""", unsafe_allow_html=True)


#### Navigation bar
with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["Home", "Cracks Detector", "Settings", "Background", "Contact"],
        icons=["house", "cloud-upload", "gear", "book", "telephone"],  # Labels
        menu_icon="cast",
        default_index=0,
    )


#### Show content dependend on selection in navigation bar

## Landing Page (Home)
if selected == "Home":
    col1, col2 = st.columns([2.5, 1.5])
        #Left side of page (Text)
    with col1: #Text
        st.title("Analyze cracks with the cracks detector to prevent accitents and to anticipate climate change")
        st.write("")
        st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text t Text Text Text Text Text Text Text Text Text Text Text Text Text Te")
        st.write("")
        st.write("")
        if st.button("Start Cracks Detector"):
            show_page1()
        st.write("")
        st.write("")

        #Right side of page (Picture)
    with col2: #Image
        image = Image.open("/Users/miraweber/Desktop/Unbenannt.jpg")
        st.image(image, use_column_width=True)

## Cracks Detector Page
if selected == "Cracks Detector":
    st.title("Start to analyze your image for cracks with the Cracks Detector")
    # Step 1:
        # Selection of Option (Bulding, Street etc.)
    st.markdown('<p class="big-font">Step 1: Choose your image(s)</p>', unsafe_allow_html=True) #st.write("**Step 1: Choose your image(s)**")

    option = st.selectbox(
        'Select the kind of image:',
        ('Building', 'Street', 'Bridge', 'Other')
    )
        # Image Upload (old)
    url="https://cracksdetectionapi-5ojt6thguq-ew.a.run.app/predict"

    st.set_option('deprecation.showfileUploaderEncoding', False)

    uploaded_file = st.file_uploader("Choose an Image")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Checkbox
    st.checkbox('Accept terms and conditions')

    # Step 2:
    st.markdown('<p class="big-font">Step 2: Find out if there is a crack (Classification)</p>', unsafe_allow_html=True) #st.write("**Step 2: Find out if there is a crack (Classification)**")
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text ")
    if st.button("Detect if there is a crack"):


        # print is visible in the server output, not in the page
        print('button clicked!')
        st.write('I was clicked 🎉')
        files = {"file":  uploaded_file.getvalue()}
        response=requests.post(url,files=files)
        if response.status_code==200:
            image = Image.open("/Users/miraweber/Desktop/Cracks.jpg")
            st.image(image, use_column_width=True)
            #prediction=response.json()['prediction']
            #st.write(prediction)
        elif response.status_code==204:
            image = Image.open("/Users/miraweber/Desktop/No_Cracks.jpg")
            st.image(image, use_column_width=True)
        else:
            st.write('error')
            st.write(type(uploaded_file))

#        # Result
#        col1, col2 = st.columns([2, 2])
#        with col1: # Result Cracks
#            image = Image.open("/Users/miraweber/Desktop/Cracks.jpg")
#            st.image(image, use_column_width=True)
#        with col2: # Result No Cracks
#                image = Image.open("/Users/miraweber/Desktop/No_Cracks.jpg")
#                st.image(image, use_column_width=True)

    # Step 3:
    st.markdown('<p class="big-font">Step 3: Find out the location of the crack (Segmentation)</p>', unsafe_allow_html=True)  #st.write("**Step 3: Find out the location of the crack (Segmentation)**")
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text ")
    if st.button("Detect location of the crack"):
        if response.status_code==200:
            st.image(response, use_column_width=True)

    # Step 4:
    st.markdown('<p class="big-font">Step 4: Estimate the severity of the cracks</p>', unsafe_allow_html=True)  #st.write("**Step 4: Estimate the severity of the crack**")
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text ")

        # Slider
    percent = st.slider(
        'Severity Setting',
        min_value=0,
        max_value=100,
        value=50  # Default 50%
    )
    st.write(f'You have choosen {percent}%')
    st.button("Calculate crack severity")
    st.write("")
    st.write("")
        # Result
    col1, col2 = st.columns([2, 2])
    with col1: # Result Cracks
        image = Image.open("/Users/miraweber/Desktop/Cracks.jpg")
        st.image(image, use_column_width=True)


## Page Settings
if selected == "Settings":
    st.title("Settings")
    st.write("Settings Info")

## Page Background
if selected == "Background":
    st.title("Background")
    st.write("Background Info")

## Page Contact
if selected == "Contact":
    st.title("Contact")
    st.write("Contact Info")
