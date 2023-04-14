import streamlit as st
from PIL import Image
import pytesseract
import pandas as pd
import numpy as np

im = Image.open("./favicon.ico")
st.set_page_config(
    page_title=" P&ID Quest",
    page_icon=im,
    layout="wide"
)

st.title('This project is to identify all types of devices and instrument in P&ID map.')

st.write('Currently, we support some basic devices!')

img1 = st.file_uploader("Select your input file", type=["jpg"])


pytesseract.pytesseract.tesseract_cmd = 'C:/Users/Ethan/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

with st.spinner('Wait for it...'): 
    if img1:

        img = Image.open(img1)

        result = pytesseract.image_to_string(img)
        matrices = result.split('\n')
        counter=0
        for i in matrices:
            if 'VB' in i:
                counter += 1
        st.success(f'Counter of device including VB in their name is: {counter}')

        texts = pytesseract.image_to_data(img)
        texts2 = texts.replace('\t', ',')

        temp = list(texts.split('\n'))
        temp2 = pd.DataFrame([temp[i].split('\t') for i,j in enumerate(temp)])
        temp2.iloc[:,11].replace('', np.nan, inplace=True)
        temp2.dropna(inplace=True)

        st.write(pd.DataFrame(temp2))
        pd.DataFrame(temp2).to_csv('text.csv')


