import os
import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image
import requests
from streamlit_app import params
import time


st.set_page_config(
    page_title="AutoTab tab generator",
    layout="centered", # centered
    initial_sidebar_state="auto") # collapsed

st.write(params.LOCAL_PATH)

base_url = 'https://autotab-cloud-image-xsu5gc7nxq-ew.a.run.app'

def resp(endpoint, filename):
    url = base_url +'/'+ endpoint
    
    params = {
        'uploaded_file': filename
    }
    response = requests.get(url, params=params)
    response = response.json()
    print('resonse', response)
    return response
    # st.text(response['simple_text'])


image_path = "https://images.unsplash.com/photo-1535587566541-97121a128dc5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
st.write(f'<div class="banner" style="background-image: linear-gradient(rgba(0,0,0,0.4),rgba(0,0,0,0.4)), url({image_path});"><h1>Autotab</h1><p>Learning the guitar the easy way</p></div>', unsafe_allow_html=True)
CSS = """
.banner {
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;
    height: 300px;
    text-align: center;
    margin-top: -100px;
    margin-left: -480px;
    margin-right: -480px;
}
.banner h1 {
    padding-top: 120px;
    margin: 0;
    color: white;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    font-size: 56px;
    font-weight: bold;
}
.banner p {
    font-size: 32px;
    color: white;
    opacity: .7;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


st.set_option('deprecation.showfileUploaderEncoding', False)

# os.popen('explorer.exe "C:\\Users\\rus\\Downloads"')
uploaded_file = st.file_uploader("choose a music file:", type="wav")
# st.write('uploaded file:', uploaded_file)

@st.cache(suppress_st_warning=True)
def upload_to_gcloud(uploaded_file):
    if uploaded_file is not None:
        st.write('filename', uploaded_file.name)
        st.write('current dir', os.getcwd())
        
        audio_bytes = uploaded_file.read()
        with open(uploaded_file.name, mode="bx") as f:
            f.write(audio_bytes)
        st.audio(audio_bytes, format='audio/wav')
        
        gcloud_path = f'gsutil cp -n {params.LOCAL_PATH + uploaded_file.name} gs://{params.BUCKET_NAME}'
        time.sleep(5)
        st.write(gcloud_path)
        os.popen(gcloud_path)

# call the upload to upload_to_gcloud function once
upload_to_gcloud(uploaded_file)
    


mode = st.radio('Choose Mode of Tab production:', ('Ergonomic Simple', 'Ergonomic Rhythm', 'All Frames'))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


    
if uploaded_file is not None and mode == 'Ergonomic Simple': 
    st.title("""
            Ergonomic Simple predicted Tabs: 
    """)

    # response of ergonomic_simple endpoint, also give filename
    simple_text = resp('ergonomic_simple', uploaded_file.name) 
    st.text(simple_text['simple_text'])
    
if uploaded_file is not None and mode == 'Ergonomic Rhythm': 
    st.title("""
            Ergonomic Rhythm predicted Tabs:
    """)

    simple_text = resp('ergonomic_rhythm', uploaded_file.name)
    st.text(simple_text['simple_text'])
    
if uploaded_file is not None and mode == 'All Frames': 
    st.title("""
            All Frames predicted Tabs:
    """)

    simple_text = resp('all_frames', uploaded_file.name)
    st.text(simple_text['simple_text'])


