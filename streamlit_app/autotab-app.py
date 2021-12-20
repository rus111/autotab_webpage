import os
import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image
import requests
from streamlit_app import params
import sys
import google_cloud as gc


st.set_page_config(
    page_title="AutoTab tab generator",
    layout="centered", # centered
    initial_sidebar_state="auto") # collapsed

uploaded_file = None
base_url = 'https://autotab-cloud-image-xsu5gc7nxq-ew.a.run.app'

def resp(endpoint, filename):
    url = base_url +'/'+ endpoint
    
    params = {
        'uploaded_file': filename
    }
    print(url, params)
    response = requests.get(url, params=params)
    sys.stdout.write('resonse' +  str(response)+"\n")
    response = response.json()
    sys.stdout.write('resonse' +  str(response)+"\n")
    return response
    # st.text(response['simple_text'])


image_path = "https://images.unsplash.com/photo-1535587566541-97121a128dc5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
st.write(f'<div class="banner" style="background-image: linear-gradient(rgba(0,0,0,0.4),rgba(0,0,0,0.4)), url({image_path});"><h1>Autotab</h1><p>Learning to play the guitar the easy way</p></div>', unsafe_allow_html=True)
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

# choose an existing music file or your own
if st.checkbox('check if you want to upload your mono-wave file!'):
    # upload music file to ram 
    uploaded_file = st.file_uploader("please choose a (mono) wave music file:", type="wav")
    filename = ''
else:
    # download file from cloud and allow user to play it.  
    filename = 'experimentmono.wav'
    st.write('you chose: ' + filename + ' file')
    joined_path = os.path.join(params.LOCAL_PATH, filename)
    print(joined_path)
    if not os.path.isfile(joined_path): # Only create locally, if it is not there yet.
        print('file:', filename, 'in dir', params.LOCAL_PATH, 'does not exists')
        gc.get_gcloud_file(params.BUCKET_NAME, filename, filename)
    audio_file = open(filename,'rb')
    audio_bytes = audio_file.read() 
    st.audio(audio_bytes, format='audio/wav')
    
# execute if wave file is chosen to write it in file.     
if uploaded_file is not None:
    filename = uploaded_file.name
    audio_bytes = uploaded_file.read()
    st.audio(audio_bytes, format='audio/wav')
    joined_path = os.path.join(params.LOCAL_PATH, filename)
    print(joined_path)
    if not os.path.isfile(joined_path): # Only create locally, if it is not there yet.
        print('file:', uploaded_file, 'in dir', params.LOCAL_PATH, 'does not exists')
        with open(filename, mode="bx") as f:
            f.write(audio_bytes)
    gc.upload_gcloud_file(params.BUCKET_NAME, filename, filename)


mode = st.radio('Choose Mode of Tab production:', ('Ergonomic Simple', 'Ergonomic Rhythm', 'All Frames'))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


def output_style_request(mode, filename):
    if filename != '':
        if mode == 'Ergonomic Simple': 
            st.title("""
                    Ergonomic Simple predicted Tabs: 
            """)

            # response of ergonomic_simple endpoint, also give filename
            simple_text = resp('ergonomic_simple', filename) 
            st.text(simple_text['simple_text'])
            
        if mode == 'Ergonomic Rhythm': 
            st.title("""
                    Ergonomic Rhythm predicted Tabs:
            """)

            simple_text = resp('ergonomic_rhythm', filename)
            st.text(simple_text['simple_text'])
            
        if mode == 'All Frames': 
            st.title("""
                    All Frames predicted Tabs:
            """)

            simple_text = resp('all_frames', filename)
            st.text(simple_text['simple_text'])

output_style_request(mode, filename) 
#######################################################################
# The developers:

developers_html =  """<div class="footer">
<div class="footer-copyright">
    Autotab is brought to you by:
</div>
<img class="avatar-large" alt="avatar-large" src="https://avatars.githubusercontent.com/u/75431042?v=4" />
<img class="avatar-large" alt="avatar-large" src="https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1632725013/gu7bxeeyzt4tvxidmxsu.jpg" />
<img class="avatar-large" alt="avatar-large" src="https://avatars.githubusercontent.com/u/91727688?v=4" />
<img class="avatar-large" alt="avatar-large" src="https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1632729260/u7j3wesevs1hwbtfahem.jpg" />
</div>
"""


developers_css = """
.footer {
  position: fixed;
  bottom:0;
  background: #F4F4F4;
  display: bottom;
  align-items: center;
  justify-content: space-between;
  height: 100px;
  padding: 0px 50px;
  color: rgba(0,0,0,0.3);
}

.avatar {
  width: 40px;
  border-radius: 50%;
}

.avatar-large {
  width: 56px;
  border-radius: 50%;
}

.avatar-bordered {
  width: 40px;
  border-radius: 50%;
  box-shadow: 0 1px 2px rgba(0,0,0,0.2);
  border: white 1px solid;
}

.avatar-square {
  width: 40px;
  border-radius: 0px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.2);
  border: white 1px solid;
}
"""
st.write(developers_html, unsafe_allow_html=True)
st.write(f'<style>{developers_css}</style>', unsafe_allow_html=True)
