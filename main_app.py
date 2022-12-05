import streamlit as st
import io
from PIL import Image

import pdfplumber




uploaded_files = st.file_uploader("Veuillez charger une image",type=['pdf','jpg','jpeg','png'],help="Charger une image au format jpg,jpeg,png", accept_multiple_files=False,)



with pdfplumber.open(uploaded_files) as pdf:
    page = pdf.pages[0]
    final_text = page.extract_text()
     
 

st.text_area(label="Output Data:", value=final_text, height=550)
