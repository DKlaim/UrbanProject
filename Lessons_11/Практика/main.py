# 1) Создать изображение, на котором будет сгенерирована надпись с помощью Python.
# 2) Найти подходящие методы обработки изображений на Python, изучить библиотеки, такие как PIL или OpenCV.
# 3) Найти учебные материалы (туториалы) по обработке изображений в Python.
# 4) Изучить документацию по библиотекам для обработки изображений, чтобы лучше понять их возможности.
# 5) Разработать код с использованием интроспекции, позволяющий исследовать атрибуты объектов и их методы.
# 6) Инкапсулировать все в один класс и протестировать запуск кода.
from PIL import Image, ImageFont, ImageDraw


# im = Image.open('photo.jpg')
# print(im.format, im.size, im.mode)

# # Пропорциональное изменение размера изображения до указанного предела
# im = Image.open('photo.jpg')
# im.thumbnail((400, 400))
# im.show()

# # Вариант изменения размера через изменение параметров size
# im = Image.open('photo.jpg')
# w, h = im.size
# out = im.resize((w//2, h//2))
# out.show()

# Изменение изображения в n раз
def new_photo(name, n=1):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // n, h // n))


im_1 = new_photo('photo1.jpg')
im_2 = new_photo('moon.png', 4)
im_1.paste(im_2, (253, 12), mask=im_2)

draw = ImageDraw.Draw(im_1)
font = ImageFont.truetype('PalatinoBoldItalic.ttf', 30)
draw.text((300, 620), 'New story', font=font, fill='blue')

im_1.show()
