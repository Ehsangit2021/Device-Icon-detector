from PIL import Image 
import pandas as pd
from PDF2IMAGE import MyPdf2Image
import pytesseract
from googletrans import Translator


img = Image.open('IMG/out_0.jpg')

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/Ethan/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
result = pytesseract.image_to_string(img)

matrices = result.split('\n')
counter=0

for i in matrices:
    if 'VB' in i:
        counter += 1


# Get bounding box estimates
BoundingBox = pytesseract.image_to_boxes(img)
BoundingBox = BoundingBox.split('\n')
print(BoundingBox)

# Get verbose data including boxes, confidences, line and page numbers
texts = pytesseract.image_to_data(img)
texts2 = texts.replace('\t', ',')

temp = list(texts.split('\n'))
[temp[i].split('\t') for i,j in enumerate(temp)]
temp2 = pd.DataFrame([temp[i].split('\t') for i,j in enumerate(temp)])
pd.DataFrame(temp2).to_csv('text.csv')

MyPdf2Image('PDF/1.pdf')

print(texts)

# Get information about orientation and script detection
print(pytesseract.image_to_osd(img))



print(result)