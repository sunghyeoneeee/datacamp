# 3 - 1 (이진분류)
import os
import shutil
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping # 콜백 추가
from tensorflow.keras import backend as K

# 이미지 파일이 저장된 최상위 디렉토리 경로
root_directory = '/content/drive/MyDrive/데이터 분석 대회/new_train_resized'

# 클래스별 디렉토리 이름
class1_directory = '마스크 미착용'  # 마스크 미착용
class2_directory = '마스크 착용'  # 마스크 착용

# 이미지 파일 이름에 따라 클래스를 결정하고 해당 클래스의 디렉토리로 파일을 이동
for root, directories, files in os.walk(root_directory):
    for filename in files:
        if filename.endswith((".jpg", ".JPG")):
            # 파일 이름에 따라 클래스 결정
            if filename[12:14] == '01':  # 마스크 미착용
                class_name = class1_directory
            elif filename[12:14] in ['02', '03']:  # 마스크 착용
                class_name = class2_directory
            else:
                continue  # '01', '02', '03'이 아닌 경우는 무시

            # 클래스 이름으로 디렉토리 생성 (이미 디렉토리가 존재하면 생성하지 않음)
            class_directory = os.path.join(root_directory, class_name)
            os.makedirs(class_directory, exist_ok=True)

            # 이미지 파일을 클래스 디렉토리로 이동
            src_file = os.path.join(root, filename)
            dst_file = os.path.join(class_directory, filename)
            shutil.move(src_file, dst_file)

# 학습 데이터와 검증 데이터가 저장된 디렉토리 경로
train_directory = '/content/drive/MyDrive/데이터 분석 대회/new_train_resized'  # 실제 학습 데이터 디렉토리 경로로 변경
val_directory = '/content/drive/MyDrive/데이터 분석 대회/new_valid_resized'  # 실제 검증 데이터 디렉토리 경로로 변경

# 이미지 크기와 채널 수
image_size = (64, 64)
channels = 3

# 모델 구성
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(image_size[0], image_size[1], channels)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

def f1_score(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val

# 모델 컴파일
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', f1_score])

# 이미지 데이터 제네레이터 생성
datagen = ImageDataGenerator(rescale=1./255)

train_gen = datagen.flow_from_directory(
    directory=train_directory,  # 학습 데이터가 있는 디렉토리 경로
    target_size=image_size,
    class_mode='binary',
    batch_size=32
)

val_gen = datagen.flow_from_directory(
    directory=val_directory,  # 검증 데이터가 있는 디렉토리 경로
    target_size=image_size,
    class_mode='binary',
    batch_size=32
)


# EarlyStopping 콜백 설정
early_stopping = EarlyStopping(monitor='val_loss', patience=3, verbose=1)

# 콜백 리스트
callbacks = [early_stopping]

# 모델 훈련
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=20,
    callbacks=callbacks,
    workers=4
)