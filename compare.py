import cv2
import pytesseract
from PIL import Image
from easyocr import Reader
import os
import time
import matplotlib as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
reader = Reader(['en'])

def createPlot(score_easyocr, score_tesseract):
    x = ['EasyOCR', 'Tesseract']
    y = [score_easyocr, score_tesseract]

    plt.bar(x, y,label='Calculated Jaccard similarity')  # Параметр label позволяет задать название величины для легенды
    # plt.plot(x, y, color='green', marker='o', markersize=7)

    plt.ylabel('Jaccard similarity ')
    plt.title('Comparison OCR')
    plt.legend()
    name = "fig"
    plt.savefig(f'C:/Users/user/PycharmProjects/comparisonOCR/fig/{name}')


def read_text_tesseract(image_path):
    img = cv2.imread(image_path)

    custom_config = r'--oem 3' #для использования LSTM

    text = pytesseract.image_to_string(img, config=custom_config)
    # print("tesseract's text: ", text)
    return text


def read_text_easyocr(image_path):
    text = ''
    results = reader.readtext(Image.open(image_path))
    for result in results:
        text = text + result[1] + ' '

    text = text[:-1]
    # print("easyOCR's text: ", text)
    return text


def jaccard_similarity(sentence1, sentence2):
    # Tokenize sentences into sets of words
    set1 = set(sentence1.lower().split())
    set2 = set(sentence2.lower().split())

    # Calculate Jaccard similarity
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))

    # Avoid division by zero if both sets are empty
    similarity = intersection_size / union_size if union_size != 0 else 0.0

    return similarity


# score_tesseract = 0
# score_easyocr = 0

def test_tesseract(path):
    t_start = time.time()
    score_tesseract = 0

    for image_path_ in os.listdir(f'TESTS/{path}/'):
        image_path = os.path.join(f'TESTS/{path}/', image_path_)
        gt = image_path[:-4].replace('_', ' ').lower()

        tesText = read_text_tesseract(image_path).lower().replace('\n', ' ').replace('!', '').replace(
            '?', '').replace('.', '')
        print(tesText)
        score_tesseract += jaccard_similarity(gt, tesText)

    print(f"Tesseract done with {path}, dT:", time.time() - t_start)
    return score_tesseract

def test_easyocr(path):
    t_start = time.time()
    score_easyocr = 0

    for image_path_ in os.listdir(f'TESTS/{path}/'):
        image_path = os.path.join(f'TESTS/{path}/', image_path_)
        gt = image_path[:-4].replace('_', ' ').lower()

        easyText = read_text_easyocr(image_path).lower().replace('\n', '').replace('!', '').replace(
            '?', '').replace('.', '')
        # print(easyText)
        score_easyocr += jaccard_similarity(gt, easyText)

    print(f"EasyOCR done with {path}, dT:", time.time() - t_start)
    return score_easyocr


# for image_path_ in os.listdir('TESTS/testROTATE/'):
#     image_path = os.path.join('TESTS/testROTATE/', image_path_)
#
#     gt = image_path[:-4].replace('_', ' ').lower()
#     # print(gt, " ")
#
#     tesText = read_text_tesseract(image_path).lower().replace('\n', ' ').replace('!','').replace(
#         '?', '').replace('.', '')
#
#     easyText = read_text_easyocr(image_path).lower().replace('\n', '').replace('!','').replace(
#         '?', '').replace('.', '')
#
#     print("TESSERACT: ", tesText)
#     print("EASYOCR: ", easyText)
#
#     # score_tesseract += jaccard_similarity(gt, tesText)
#     score_easyocr += jaccard_similarity(gt, easyText)
paths = ['testBLUR', 'testROTATE', 'testROTATEandBLUR', 'testKAGGLE']

total_score_tesseract = 0
total_score_easyocr = 0
all_datasets_size = 0

for path in paths:
    dataset_size = len(os.listdir(f'TESTS/{path}/'))
    all_datasets_size +=dataset_size

    print("\n\n----------------------\nDataset: ", path, f" {dataset_size} files")
    score_tesseract = test_tesseract(path)
    score_easyocr = test_easyocr(path)

    total_score_tesseract += score_tesseract
    total_score_easyocr += score_easyocr

    final_score_tesseract = score_tesseract / dataset_size
    final_score_easyocr = score_easyocr / dataset_size
    dataset_size = 0

    print('score tesseract:', final_score_tesseract)
    print('score_easyocr:', final_score_easyocr)

print(f"\n\n----------------------------\nTotal score: \nTesseract: {total_score_tesseract/all_datasets_size}\nEasyOCR: {total_score_easyocr/all_datasets_size}")


