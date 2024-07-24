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
        background-color: #FFFFFF;
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
scroll_to_top_script = """
    <script>
    function scrollToTop() {
        window.scrollTo({top: 0, behavior: 'smooth'});
    }
    </script>
"""


## Button setup


if 'button1' not in st.session_state:
    st.session_state.button1 = False
if 'button2' not in st.session_state:
    st.session_state.button2 = False
if 'button3' not in st.session_state:
    st.session_state.button3 = False



## Cracks Detector Page


st.title("Start to analyze your image for cracks with the Cracks Detector")

# Step 1:
    # Selection of Option (Bulding, Street etc.)
st.markdown('<p class="big-font">Step 1: Choose your image(s)</p>', unsafe_allow_html=True) #st.write("**Step 1: Choose your image(s)**")
st.write('⚠️ - Warning - the models have been trained on "zoomed images" - For better results, please zoom in your image before uploading it')
col1, col2 = st.columns([1, 3])
with col1:
        image = Image.open("media/Image_zoom.jpg")
        st.image(image, use_column_width=True)

option = st.selectbox(
    'Select the kind of image:',
    ('Building', 'Street', 'Bridge', 'Other')
)

    # Image Upload (old)
url="https://cracksdetectionapi-5ojt6thguq-ew.a.run.app/yolo_predict"
url_CNN="https://cracksdetectionapi-5ojt6thguq-ew.a.run.app/predict"
url_severity="https://cracksdetectionapi-5ojt6thguq-ew.a.run.app/predict_severity"
#url_severity="http://127.0.0.1:8000/predict_severity"

st.set_option('deprecation.showfileUploaderEncoding', False)


uploaded_file = st.file_uploader("Choose an Image")

if uploaded_file is not None:
    col1, col2 = st.columns([1, 5])
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        # Checkbox
st.checkbox('Accept terms and conditions')

# Step 2:
st.markdown('<p class="big-font">Step 2: Find out if there is a crack (Classification)</p>', unsafe_allow_html=True) #st.write("**Step 2: Find out if there is a crack (Classification)**")
st.write('Two models will be running YOLO & CNN')
st.write('For the "CNN" one you have access to the probability of having cracks returned by the model - NOTA to enable a good recall and alert engineer even when there is doubt - the threshod has been put to 34%, "if probability is higher than 34% an alerte will be display"')

if st.button("Detect if there is a crack"):
    st.session_state.button1 = not st.session_state.button1
    # print is visible in the server output, not in the page

if st.session_state.button1:
    files = {"file":  uploaded_file.getvalue()}
    response=requests.post(url,files=files)
    col1, col2, col3 = st.columns([2, 2, 2])
    if response.status_code==200:

        with col1:

            st.markdown('<p class="slider-label">Prediction from YOLO model</p>', unsafe_allow_html=True)
            image = Image.open("media/Cracks.jpg")
            st.image(image, use_column_width=True)
        #prediction=response.json()['prediction']
        #st.write(prediction)

    elif response.status_code==204:

        with col1:
            st.markdown('<p class="slider-label">Prediction from YOLO model</p>', unsafe_allow_html=True)
            image = Image.open("media/No_cracks.jpg")
            st.image(image, use_column_width=True)
    else:
        st.write('error')
        st.write(type(uploaded_file))

    response_CNN=requests.post(url_CNN,files=files).json()
    results=response_CNN["prediction"]*100

    if results <34:

        with col2:
            st.markdown('<p class="slider-label">Prediction from CNN model</p>', unsafe_allow_html=True)
            image = Image.open("media/No_cracks.jpg")
            st.image(image, use_column_width=True)
            results_UI=f'The probability of having cracks, returned by the CNN model, is {round(results)} %'
            st.write(results_UI)
    else :

        with col2:
            st.markdown('<p class="slider-label">Prediction from CNN model</p>', unsafe_allow_html=True)
            image = Image.open("media/Cracks.jpg")
            st.image(image, use_column_width=True)
            results_UI=f'The probability of having cracks, returned by the CNN model, is {round(results)} %'
            st.write(results_UI)
else :
    st.write('Click on Me 👆')

# Step 3:
st.markdown('<p class="big-font">Step 3: Find out the location of the crack (Segmentation)</p>', unsafe_allow_html=True)  #st.write("**Step 3: Find out the location of the crack (Segmentation)**")
st.write('⚠️ - Warning - only the "YOLO" model displays the location of the cracks if there are any')

if st.button("Detect location of the crack"):
    st.session_state.button2 = not st.session_state.button2

if st.session_state.button2:
    files = {"file":  uploaded_file.getvalue()}
    response=requests.post(url,files=files)
    if response.status_code==200:
        col1, col2 = st.columns([2, 1])
        with col1:
            image_stream = BytesIO(response.content)
            image = Image.open(image_stream)
            st.write("")
            st.image(image, use_column_width=True, )
    else :
        col1, col2, col3 = st.columns([2, 2, 2])
        with col1:
            image = Image.open("media/No_cracks.jpg")
            st.image(image, use_column_width=True)
else :
    st.write('Click on Me 👆')

#        # Result
#        col1, col2 = st.columns([2, 2])
#        with col1: # Result Cracks
#            image = Image.open("/Users/miraweber/Desktop/Cracks.jpg")
#            st.image(image, use_column_width=True)
#        with col2: # Result No Cracks
#                image = Image.open("/Users/miraweber/Desktop/No_Cracks.jpg")
#                st.image(image, use_column_width=True)


# Step 4:
st.markdown('<p class="big-font">Step 4: Estimate the severity of the cracks</p>', unsafe_allow_html=True)  #st.write("**Step 4: Estimate the severity of the crack**")
st.write('⚠️ - Warning - Only the YOLO model gives us the severity - The calculation of this parameter is still in process. See Seetings and Vision for more information' )
st.write("")

if st.button("Calculate crack severity"):
    st.session_state.button3 = not st.session_state.button3

if st.session_state.button3:
    files = {"file":  uploaded_file.getvalue()}
    response=requests.post(url_severity,files=files)
    results=response.json()["severity"]


    if response.status_code==200:

            if results <0.005:
                delta ="Low Severity"
            elif results <0.025 :
                delta='-Moderate Severity'
            else :
                delta="-High Severity"

            st.metric(label="Severity", value=f"{results*100:.2f} %", delta=delta)

    else :
        col1, col2 = st.columns([2, 2])
        with col1:
            image = Image.open("media/No_cracks.jpg")
            st.image(image, use_column_width=True)
else :
    st.write('Click on Me 👆')

# st.write("")

# st.markdown(scroll_to_top_script, unsafe_allow_html=True)
# if st.button("Load another picture", on_click="scrollToTop()"):
#     st.session_state.button1 = False
#     st.session_state.button2 = False
#     st.session_state.button3 = False
