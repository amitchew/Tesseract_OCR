import streamlit as st
import io
from PIL import Image


uploaded_files = st.file_uploader("Upload file",type=['pdf','jpg','jpeg','png'],help="Upload files in 'pdf','jpg','jpeg','png' format")

for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     image = Image.open(io.BytesIO(bytes_data))
     st.write("filename:", uploaded_file.name)
     st.image(image)
