from ocr import OCR

import os
ocr=OCR(image_folder='test/')

if __name__ == "__main__":
    # path = 'test/'
    # rez = sorted(os.listdir(path))
    # for n, item in enumerate(rez):
    #     print(n+1 , item)
    # print("\n############\n" + "KERAS" + "\n############\n")
    # ocr.keras_ocr_works()
    print("\n############\n" + "EasyOCR" + "\n############\n")
    ocr.easyocr_model_works()
    print("\n############\n" + "PYTESSERACT" + "\n############\n")
    ocr.pytesseract_model_works()

