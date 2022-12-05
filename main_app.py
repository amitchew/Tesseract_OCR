import streamlit as st
import io
from PIL import Image

import pdfplumber




uploaded_files = st.file_uploader("Veuillez charger une image",type=['pdf','jpg','jpeg','png'],help="Charger une image au format jpg,jpeg,png", accept_multiple_files=True,)



with pdfplumber.open(uploaded_files) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
     

for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     image = Image.open(io.BytesIO(bytes_data))
     st.write("filename:", uploaded_file.name)
     st.image(image)
st.text(text)
