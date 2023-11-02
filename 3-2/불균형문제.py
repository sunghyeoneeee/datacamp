# 3 - 2 (불균형 문제 확인)
import numpy as np

# 훈련 데이터 클래스 불균형 확인
train_classes, train_counts = np.unique(train_gen.classes, return_counts=True)
for class_name, class_count in zip(train_classes, train_counts):
    print(f'학습 데이터 - 클래스 {class_name}: {class_count}개')

# 검증 데이터 클래스 불균형 확인
val_classes, val_counts = np.unique(val_gen.classes, return_counts=True)
for class_name, class_count in zip(val_classes, val_counts):
    print(f'검증 데이터 - 클래스 {class_name}: {class_count}개')