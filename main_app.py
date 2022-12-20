import streamlit as st
import io
from PIL import Image
import pdfplumber

import fitz
import json
import tabula
from tabula import convert_into
import pandas as pd


uploaded_files = st.file_uploader("Upload file",type=['pdf'],help="Upload files in pdf", accept_multiple_files=False,)


with pdfplumber.open(uploaded_files) as pdf:
    file = pdf.pages[0]
    final_text = file.extract_text()
    result_final=extract_data(final_text, templates=templates)
 



tabula.convert_into(file, "output.csv", output_format="csv", pages='all')
df = pd.read_csv("output.csv")
df['id']=df.index
df.to_csv("output.csv"),

##
import csv, json
csvFilePath='output.csv'
data= {}

with open(csvFilePath) as csvFile:
  csvReader = csv.DictReader(csvFile)
  for rows in csvReader:
    id = rows["id"]
    data[id]= rows
table_output=json.dumps(data,indent=4)

##
with fitz.open(file) as doc:
    for page in doc:
        text = page.get_text("blocks")
  
##
res = [lis[4] for lis in text]
##
total =  {
     "Invoice_Number":res[1], 
     "Invoice_Date":res[6],
     "Issuer":res[3],
     "Bill_to": res[5]
      }
header = json.dumps(total)
##

st.header('OCR for Sparta X')





st.text_area(label="Output Data:", value=final_text, height=550)


st.text_area(label="Header:", value=header, height=550)


st.text_area(label="Table:", value=table_output, height=550)

