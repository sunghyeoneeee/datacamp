# 3 - 3
# 성능향상 - 6번
import os
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization  # BatchNormalization import
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras import backend as K

train_directory = '/content/drive/MyDrive/데이터 분석 대회/undersampled_train'
val_directory = '/content/drive/MyDrive/데이터 분석 대회/undersampled_valid'
image_size = (64, 64)
channels = 3

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(image_size[0], image_size[1], channels)))
model.add(MaxPooling2D((2, 2)))
model.add(BatchNormalization())  # BatchNormalization layer added
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(BatchNormalization())  # BatchNormalization layer added
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(BatchNormalization())  # BatchNormalization layer added
model.add(Flatten())
model.add(Dropout(0.7))
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())  # BatchNormalization layer added
model.add(Dense(1, activation='sigmoid'))

def f1_score(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', f1_score])

datagen = ImageDataGenerator(rescale=1./255)

train_gen = datagen.flow_from_directory(
    directory=train_directory,
    target_size=image_size,
    class_mode='binary',
    batch_size=64
)

val_gen = datagen.flow_from_directory(
    directory=val_directory,
    target_size=image_size,
    class_mode='binary',
    batch_size=64
)

early_stopping = EarlyStopping(monitor='val_loss', patience=3, verbose=1)
callbacks = [early_stopping]

history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=20,
    callbacks=callbacks,
    workers=4
)