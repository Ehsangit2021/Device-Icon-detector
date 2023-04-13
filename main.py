from PIL import Image 
import pytesseract 
from googletrans import Translator


img = Image.open('test2.jpg')

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
print(pytesseract.image_to_data(img))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(img))



print(result)