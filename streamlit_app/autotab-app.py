import os
import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image
import requests
from streamlit_app import params
from google.cloud import storage
import sys


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
    print(url, params)
    response = requests.get(url, params=params)
    sys.stdout.write('resonse' +  str(response)+"\n")
    response = response.json()
    sys.stdout.write('resonse' +  str(response)+"\n")
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

# @st.cache(suppress_st_warning=True)
# def upload_to_gcloud(uploaded_file):
#     if uploaded_file is not None:
#         st.write('filename', uploaded_file.name)
#         st.write('current dir', os.getcwd())
        
#         audio_bytes = uploaded_file.read()
#         with open(uploaded_file.name, mode="bx") as f:
#             f.write(audio_bytes)
#         st.audio(audio_bytes, format='audio/wav')
        
#         gcloud_path = f'gsutil cp -n {params.LOCAL_PATH + uploaded_file.name} gs://{params.BUCKET_NAME}'
#         time.sleep(5)
#         st.write(gcloud_path)
#         os.popen(gcloud_path)

# call the upload to upload_to_gcloud function once
# upload_to_gcloud(uploaded_file)

# @st.cache(suppress_st_warning=True)
def upload_gcloud_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"
    
    storage_client = storage.Client()
    print(storage_client)

    bucket = storage_client.bucket(bucket_name)
    # sys.stdout.write(bucket)
    print("bucket", bucket)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    sys.stdout.write("blob"+ str(blob)+"\n")
    file_exists = storage.Blob(bucket=bucket, name=uploaded_file.name).exists(storage_client)
    if not file_exists:
        blob.upload_from_filename(destination_file_name)
        print(
            "Uploaded storage object {} from local file {} to bucket {}.".format(
                destination_file_name, source_blob_name, bucket_name
            )
        )
        print(f'uploaded {destination_file_name}')
        
# import ipdb; ipdb.set_trace() # TODO:
if uploaded_file is not None:
    audio_bytes = uploaded_file.read()
    st.audio(audio_bytes, format='audio/wav')
    joined_path = os.path.join(params.LOCAL_PATH, uploaded_file.name)
    print(joined_path)
    if not os.path.isfile(joined_path): # Only create locally, if it is not there yet.
        print('file:', uploaded_file, 'in dir', params.LOCAL_PATH, 'does not exists')
        with open(uploaded_file.name, mode="bx") as f:
            f.write(audio_bytes)
    upload_gcloud_file(params.BUCKET_NAME, uploaded_file.name, uploaded_file.name)

    


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
    



