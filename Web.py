import streamlit as st
from PIL import Image
import pytesseract

im = Image.open("./favicon.ico")
st.set_page_config(
    page_title=" P&ID Icons",
    page_icon=im,
    layout="wide"
)

st.title('This project is to identify all types of devices and instrument in P&ID map.')

st.write('Currently, we support some basic devices!')

pdf_file = st.file_uploader("Select your input file", type=["jpg"])




pytesseract.pytesseract.tesseract_cmd = 'C:/Users/Ethan/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'



texts = pytesseract.image_to_data(img)
texts2 = texts.replace('\t', ',')

temp = list(texts.split('\n'))
[temp[i].split('\t') for i,j in enumerate(temp)]
temp2 = pd.DataFrame([temp[i].split('\t') for i,j in enumerate(temp)])
pd.DataFrame(temp2).to_csv('text.csv')