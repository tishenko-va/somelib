from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
with Image.open("коза.jpg") as im:
     print(im.format, im.size, im.mode)
     im.show()
     enh = ImageEnhance.Contrast(im)
     enh.enhance(1.3).show("30% more contrast")
     out = im.filter(ImageFilter.DETAIL)

import requests
#
r = requests.get('https://vk.com/tishenkovalery')
print(r.status_code)
# получили разрешение на наботу со стр.(200)
print(r.text)
# получили доступ к контенту
# дальше можем работать с контентом, получать списки постов, фильтровать, узнать самые популярные,
# делать статистику

import numpy as np
a = np.array([[1,2,3],[6,7,8]])
print(a)
"""проверяем, что все работает"""
print(a.ndim)
"""узнаем количество измерений"""
print(a.shape)
"""считаем кол-во строк и столбцов"""
print(a ** 2)
'''возводим каждое число во 2 степень'''


