# training 안 폴더 수
import os

training_path = 'Training'
training_list = os.listdir(training_path)
training_count = len(training_list)
print(training_count)