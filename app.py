import os
import streamlit as st
import requests
from PIL import Image
from io import BytesIO


# Define the base URI of the API
#   - Potential sources are in `.streamlit/secrets.toml` or in the Secrets section
#     on Streamlit Cloud
#   - The source selected is based on the shell variable passend when launching streamlit
#     (shortcuts are included in Makefile). By default it takes the cloud API url
""" if 'API_URI' in os.environ:
    BASE_URI = st.secrets[os.environ.get('API_URI')]
else:
    BASE_URI = st.secrets['cloud_api_uri']
# Add a '/' at the end if it's not there
BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
# Define the url to be used by requests.get to get a prediction (adapt if needed)
url = BASE_URI + 'predict'

# Just displaying the source for the API. Remove this in your final version.
st.markdown(f"Working with {url}")

st.markdown("Now, the rest is up to you. Start creating your page.")  """


# TODO: Add some titles, introduction, ...

url="https://cracksdetectionapi-5ojt6thguq-ew.a.run.app/predict"

st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose an Image", type="jpeg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)



if st.button('click me'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
    files = {"file":  uploaded_file.getvalue()}
    response=requests.post(url,files=files)
    if response.status_code==200:
        prediction=response.json()['prediction']
        st.write(prediction)
    else:
        st.write('error')
        st.write(type(uploaded_file))

else:
    st.write('I was not clicked 😞')





# TODO: display the prediction in some fancy way to the user


# TODO: [OPTIONAL] maybe you can add some other pages?
#   - some statistical data you collected in graphs
#   - description of your product
#   - a 'Who are we?'-page
