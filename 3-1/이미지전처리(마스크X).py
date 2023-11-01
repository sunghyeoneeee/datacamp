# 이미지 전처리(마스크 착용 X)
import os
from PIL import Image

img_folder = '/content/0'

img_files = os.listdir(img_folder)

img_list = []

for img_file in img_files:
    img_path = os.path.join(img_folder, img_file)
    img = Image.open(img_path)
    img = img.resize((224, 224))
    img = img.convert('L')
    img_list.append(img)

    save_path = os.path.join('/content/마스크 착용 X', img_file)
    img.save(save_path)