import matplotlib.pyplot as plt
import numpy as np


score_tesseract = 0.6310130718954265
score_easyocr = 0.641251167133522

x = ['EasyOCR', 'Tesseract']
y = [score_easyocr, score_tesseract]

# plt.bar(x, y, label='Calculated Jaccard similarity') #Параметр label позволяет задать название величины для легенды
plt.bar(x, y, width=0.7) #Параметр label позволяет задать название величины для легенды
plt.plot(x, y, color='red', marker='o', markersize=7)
plt.yticks(np.arange(0,1,0.1))
plt.xticks(np.arange(0,2,1))
plt.ylabel('Jaccard similarity',)
plt.title('Comparison OCR')
plt.legend()
name = "Test 1"
plt.show()
