import streamlit as st
import io
from PIL import Image

import pdfplumber


st.header('OCR for Sparta X')
st.subheader('This is a subheader')


uploaded_files = st.file_uploader("Upload file",type=['pdf'],help="Upload files in pdf", accept_multiple_files=False,)



with pdfplumber.open(uploaded_files) as pdf:
    page = pdf.pages[0]
    final_text = page.extract_text()
     
 

st.text_area(label="Output Data:", value=final_text, height=550)
