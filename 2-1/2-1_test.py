from PIL import Image
import os

def new_img(input_folder, output_folder, new_size):
    for dirpath, dirname, filename in os.walk(input_folder):
        for filename2 in filename:

            input_path = os.path.join(dirpath, filename2)            
            output_path = os.path.join(output_folder, filename2)

            with Image.open(input_path) as image:
                new_img = image.resize(new_size)
                new_img.save(output_path)
                print("완료! {}".format(filename2))

input_folder = '/Users/bagseonghyeon/Desktop/datacamp/Test' 
output_folder = '/Users/bagseonghyeon/Desktop/datacamp/new_test' 
new_size = (512, 512)  

new_img(input_folder, output_folder, new_size)