import streamlit as st
from PIL import Image
import pytesseract
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

im = Image.open("./favicon.ico")
st.set_page_config(
    page_title=" P&ID Quest",
    page_icon=im,
    layout="wide"
)

st.title('This project is to identify all types of devices and instrument in P&ID map.')

st.write('Currently, we support some basic devices!')

img1 = st.file_uploader("Select your input file", type=["jpg"])


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

with st.spinner('Wait for it...'): 
    if img1:

        img = Image.open(img1)

        result = pytesseract.image_to_string(img)
        matrices = result.split('\n')
        counter=0
        vocab_dict = []
        for i in matrices:
            if 'VB' in i:
                vocab_dict.append(i)
                counter += 1

        st.success(f'Count for devices including VB in their name is: {counter}')

        if vocab_dict is not None:
            st.header('Found Devices:')
            for key, FoundString in enumerate(vocab_dict):
                with st.expander(str(key+1)):
                    with st.container():
                        st.info(FoundString)
                        # st.button(f'go to page {int(values[2])+1}', key='btn'+str(key), on_click=change_page, args=(int(values[2])+1,))
                        # st.write('----------------------------------')
                        # st.selectbox('Please select the type!', type_list, key='sb'+str(key), on_change=update_diagram, args=(key,))

        texts = pytesseract.image_to_data(img)
        texts2 = texts.replace('\t', ',')

        temp = list(texts.split('\n'))
        temp2 = pd.DataFrame([temp[i].split('\t') for i,j in enumerate(temp)])
        final_data = temp2[(temp2.iloc[:,11]!='')]

        st.write(pd.DataFrame(final_data))

        img2 = img

        for i in range(len(final_data)):
            if final_data.iloc[i,11] == None:
                continue
            if 'VB' in final_data.iloc[i,11]:
                img2 = cv2.rectangle(np.array(img2), (int(final_data.iloc[i,6]),int(final_data.iloc[i,7])), ( int(final_data.iloc[i,6]) + int(final_data.iloc[i,8]), int(final_data.iloc[i,7]) + int(final_data.iloc[i,9])), color=(255,0,0), thickness=2)

        image_path = './static/img2.jpg'

        cv2.imwrite(image_path, img2)

        pd.DataFrame(final_data).to_csv('text.csv')

        st.image(img)
        st.image(img2)



        # Define the HTML hyperlink with the image
        html_string = f'<a href="{image_path}" target="_blank"><img src="{image_path}" width="200" caption="legend"></a>'

        # Display the image using `st.markdown`
        st.markdown(html_string, unsafe_allow_html=True)