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


#### Navigation bar
with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["Home", "Cracks Detector", "Settings", "Background", "Vision", "Team"],
        icons=["house", "cloud-upload", "gear", "book", "eye", "person"],  # Labels
        menu_icon="cast",
        default_index=0,
    )

#### Show content dependend on selection in navigation bar

## Defining Button state
# Initialize session state for buttons if not already done
if 'Detect if there is a crack' not in st.session_state:
    st.session_state.button1 = False


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
        #st.link_button("Start Cracks Detector", "http://localhost:8501/#analyze-cracks-with-the-cracks-detector-to-prevent-accitents-and-to-anticipate-climate-change")
    #Right side of page (Picture)
    with col2: #Image
        image = Image.open("media/Unbenannt.jpg")
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
    url="https://cracksdetectionapi-5ojt6thguq-ew.a.run.app/yolo_predict"
    #url="http://127.0.0.1:8000/yolo_predict"

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
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text ")

    if st.button("Detect if there is a crack"):
        st.session_state.button1 = not st.session_state.button1
        # print is visible in the server output, not in the page
        files = {"file":  uploaded_file.getvalue()}
        response=requests.post(url,files=files)
        if response.status_code==200:
            col1, col2 = st.columns([2, 2])
            with col1:
                image = Image.open("media/Cracks.jpg")
                st.image(image, use_column_width=True)
            #prediction=response.json()['prediction']
            #st.write(prediction)

        elif response.status_code==204:
            col1, col2 = st.columns([2, 2])
            with col1:
                image = Image.open("media/No_cracks.jpg")
                st.image(image, use_column_width=True)
        else:
            st.write('error')
            st.write(type(uploaded_file))

    # Step 3:
    st.markdown('<p class="big-font">Step 3: Find out the location of the crack (Segmentation)</p>', unsafe_allow_html=True)  #st.write("**Step 3: Find out the location of the crack (Segmentation)**")
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text ")
    if st.button("Detect location of the crack"):
        files = {"file":  uploaded_file.getvalue()}
        response=requests.post(url,files=files)
        if response.status_code==200:
            col1, col2 = st.columns([3, 1])
            with col1:
                image_stream = BytesIO(response.content)
                image = Image.open(image_stream)

                st.image(image, use_column_width=True)
        else :
            col1, col2 = st.columns([2, 2])
            with col1:
                image = Image.open("media/No_cracks.jpg")
                st.image(image, use_column_width=True)


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
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text ")
    st.write("")
    st.button("Calculate crack severity")
    st.write("")
    st.write("")
        # Result
    #col1, col2 = st.columns([2, 2])
    #with col1: # Result Cracks
    #    image = Image.open("/Users/miraweber/Desktop/Cracks.jpg")
    #    st.image(image, use_column_width=True)


## Page Settings
if selected == "Settings":
    st.title("Settings")
    st.markdown('<p class="big-font">Models</p>', unsafe_allow_html=True)
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text")
    # Table of Models
    #col1, col2 = st.columns([4, 1])
   # with col1:
    image = Image.open("media/Table_Model.jpg")
    st.image(image, use_column_width=True)

    # Selection of Model
    option = st.selectbox(
        'Choose a Model   ---  (Warning: the segmentation task (Step 3) is works with the YOLO mode)',
        ('Base Model', 'Inception_v32', 'YOLO')
    )
    st.write('')
    st.write('')

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

## Page Background
if selected == "Background":
    st.title("Background")
    st.markdown('<p class="big-font">Ethics</p>', unsafe_allow_html=True) # st.write('**Severity Setting**')
    st.write("**Data used for training:**")
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text")
    st.write("")
    st.write("**Pre-Trained Model use:**")
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text")

## Page Vision
if selected == "Vision":
    st.title("Vision")
    st.write("**Beta Version:**")
    #st.markdown('<p class="big-font">Beta Version</p>', unsafe_allow_html=True) # st.write('**Severity Setting**')
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text")
    st.write("**Next Steps:**")
    #st.markdown('<p class="big-font">Next Steps</p>', unsafe_allow_html=True) # st.write('**Severity Setting**')
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text")


## Page Team
if selected == "Team":
    st.title("Team")
    st.write('')
    st.write("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text")
    st.write('')
    col1, col2 = st.columns([5, 2])
    with col1:
#        st.write('Team member1')
#        image = Image.open("media/Team.jpg")
#        st.image(image, use_column_width=True)
#        st.write('Team member2')
#        image = Image.open("media/Team.jpg")
#        st.image(image, use_column_width=True)
#        st.write('Team member3')
#        image = Image.open("media/Team.jpg")
#        st.image(image, use_column_width=True)
#        st.write('Team member4')
#        image = Image.open("media/Team.jpg")
#        st.image(image, use_column_width=True)
        image = Image.open("media/Team_all.jpg")
        st.image(image, use_column_width=True)
