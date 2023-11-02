# 3 - 2 (Accuracy, Precision, Recall, F1 Score)
from tensorflow.keras.metrics import Precision, Recall, Accuracy

# Accuracy, 정밀도, 재현율 메트릭 객체 생성
accuracy = Accuracy()
precision = Precision()
recall = Recall()

# 검증 데이터에서 예측
val_gen.reset()  # 제네레이터 상태 초기화
predictions = model.predict(val_gen)

# 이진 분류 문제이므로 예측값을 0.5를 기준으로 0 또는 1로 변환
predictions = [1 if pred > 0.5 else 0 for pred in predictions]

# 실제 라벨 값을 문자열에서 정수로 변환
true_labels = [int(label) for label in val_gen.classes]

# Accuracy, 정밀도, 재현율 업데이트
accuracy.update_state(true_labels, predictions)
precision.update_state(true_labels, predictions)
recall.update_state(true_labels, predictions)

# F1 점수 계산
f1_score = 2 * (precision.result().numpy() * recall.result().numpy()) / \
            (precision.result().numpy() + recall.result().numpy())

print(f"Accuracy: {accuracy.result().numpy()}")
print(f"Precision: {precision.result().numpy()}")
print(f"Recall: {recall.result().numpy()}")
print(f"F1 Score: {f1_score}")