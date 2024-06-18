import time
import pytesseract
from PIL import Image
from easyocr import Reader
import os
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
reader = Reader(['en'], gpu=True)


def read_text_tesseract(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
    # print(text)
    return text


def read_text_easyocr(image_path):
    text = ''
    results = reader.readtext(Image.open(image_path))
    for result in results:
        text = text + result[1] + ' '

    text = text[:-1]
    # print(text)
    return text

t_start = time.time()
for image_path_ in os.listdir('test2/'):
    image_path = os.path.join('test2/', image_path_)

    # print("Tesseract")
    # read_text_tesseract(image_path).lower().replace('\n', '').replace('!','').replace('?', '').replace('.', '')

    # print("EasyOCR with GPU")
    read_text_easyocr(image_path).lower().replace('\n', '').replace('!','').replace('?', '').replace('.', '')

print("Training done, dT:", time.time() - t_start)
