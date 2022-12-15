import streamlit as st
import io
from PIL import Image

import pdfplumber
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates



st.header('OCR for Sparta X')



uploaded_files = st.file_uploader("Upload file",type=['pdf'],help="Upload files in pdf", accept_multiple_files=False,)


templates= read_templates('Template/')
result_final= extract_data('AmazonWebServices.pdf', templates=templates)


with pdfplumber.open(uploaded_files) as pdf:
    page = pdf.pages[0]
    final_text = page.extract_text()
     
 

# st.text_area(label="Output Data:", value=final_text, height=550)

st.text_area(label="Extracted Data:", value=result_final, height=250)

