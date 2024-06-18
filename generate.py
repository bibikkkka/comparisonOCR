import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

# Список слов на английском
words = ["apple", "banana", "cherry", "date", "elderberry",
         "fig", "grape",
         "honeydew", "orange",
         "pear", "peach",
         "plum", "apricot",
         "avocado", "broccoli",
         "carrot", "celery",
         "chicken",
         "coffee",
         "donut",
         "egg",
         "flapjack",
         "grapefruit",
         "hamburger",
         "ice cream",
         "jellyfish",
         "kale",
         "lemon",
         "mango",
         "nectarine",
         "oatmeal",
         "paprika",
         "quinoa",
         "raspberry"]

def generator(count):
    for i in range(0,count):
        # Генерация рандомного набора слов
        random_words = random.sample(words, 5)

        # Создание изображения
        img = Image.new("RGB", (800, 600), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        # Создание шрифта
        font = ImageFont.truetype("arial.ttf", size=24)
        y = 150
        # Наполнение изображения рандомными словами
        for i, word in enumerate(random_words):
            # x = random.randint(0, 800 - len(word) * 24)
            # y = random.randint(0, 600 - 24)
            # draw.text((x, y), word, font=font, fill=(0, 0, 0))

            # функция для генерации повернутых изображений
            x = random.randint(150, 650 - len(word) * 24)
            draw.text((x, y), word, font=font, fill=(0, 0, 0))
            y = y + 40



        # Называние файла изображения рандомным набором слов
        file_name = "_".join(random_words) + ".jpg"

        # Простые изображения
        # img.save(f"C:/Users/user/PycharmProjects/comparisonOCR/TESTS/testBLUR/{file_name}")

        # Заблюренные изображения
        # blur_img = img.filter(ImageFilter.BoxBlur(2))
        # blur_img.save(f"C:/Users/user/PycharmProjects/comparisonOCR/TESTS/testBLUR/{file_name}")

        # Повернутые изображения
        retoated_img = img.rotate(10)
        retoated_img = retoated_img.crop((100, 100, 600, 500))
        retoated_img.save(f"C:/Users/user/PycharmProjects/comparisonOCR/TESTS/testROTATE/{file_name}")

        # Повернутые и заблюренные изображения
        blur_img = img.filter(ImageFilter.BoxBlur(2))
        retoated_img = blur_img.rotate(10)
        retoated_img = retoated_img.crop((100, 100, 600, 500))
        retoated_img.save(f"C:/Users/user/PycharmProjects/comparisonOCR/TESTS/testROTATEandBLUR/{file_name}")

        print(f"Generated image: {file_name}")

generator(500)






