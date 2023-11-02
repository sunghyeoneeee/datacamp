# 3 - 2 (불균형 문제 해결)
import os
import shutil
import numpy as np

# 원본 학습 데이터와 검증 데이터 디렉토리
original_train_directory = '/content/drive/MyDrive/데이터 분석 대회/new_train_resized'
original_val_directory = '/content/drive/MyDrive/데이터 분석 대회/new_valid_resized'

# 언더샘플링된 데이터를 저장할 디렉토리
undersampled_train_directory = '/content/drive/MyDrive/데이터 분석 대회/undersampled_train'
undersampled_val_directory = '/content/drive/MyDrive/데이터 분석 대회/undersampled_valid'

os.makedirs(undersampled_train_directory, exist_ok=True)
os.makedirs(undersampled_val_directory, exist_ok=True)

# 학습 데이터 언더샘플링
class_directories = [os.path.join(original_train_directory, d) for d in os.listdir(original_train_directory)]
image_files_per_class = [os.listdir(d) for d in class_directories]
min_count = min(len(image_files) for image_files in image_files_per_class)

for directory, image_files in zip(class_directories, image_files_per_class):
    sampled_image_files = np.random.choice(image_files, min_count, replace=False)
    sampled_train_directory = os.path.join(undersampled_train_directory, os.path.basename(directory))
    os.makedirs(sampled_train_directory, exist_ok=True)
    for file in sampled_image_files:
        src = os.path.join(directory, file)
        dst = os.path.join(sampled_train_directory, file)
        shutil.copyfile(src, dst)

# 검증 데이터 언더샘플링
class_directories = [os.path.join(original_val_directory, d) for d in os.listdir(original_val_directory)]
image_files_per_class = [os.listdir(d) for d in class_directories]
min_count = min(len(image_files) for image_files in image_files_per_class)

for directory, image_files in zip(class_directories, image_files_per_class):
    sampled_image_files = np.random.choice(image_files, min_count, replace=False)
    sampled_val_directory = os.path.join(undersampled_val_directory, os.path.basename(directory))
    os.makedirs(sampled_val_directory, exist_ok=True)
    for file in sampled_image_files:
        src = os.path.join(directory, file)
        dst = os.path.join(sampled_val_directory, file)
        shutil.copyfile(src, dst)