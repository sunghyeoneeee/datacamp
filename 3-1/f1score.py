# 3 - 1 (F1 Score)
# 검증 데이터에 대한 f1_score
print("검증 데이터에 대한 f1_score:")
print(history.history['val_f1_score'])

# f1_score 보기
from tensorflow.keras.metrics import Precision, Recall

# 정밀도와 재현율 메트릭 객체 생성
precision = Precision()
recall = Recall()

# 검증 데이터에서 예측
val_gen.reset()  # 제네레이터 상태 초기화
predictions = model.predict(val_gen)

# 이진 분류 문제이므로 예측값을 0.5를 기준으로 0 또는 1로 변환
predictions = [1 if pred > 0.5 else 0 for pred in predictions]

# 실제 라벨 값을 문자열에서 정수로 변환
true_labels = [int(label) for label in val_gen.classes]

# 정밀도와 재현율 업데이트
precision.update_state(true_labels, predictions)
recall.update_state(true_labels, predictions)

# F1 점수 계산
f1_score = 2 * (precision.result().numpy() * recall.result().numpy()) / \
            (precision.result().numpy() + recall.result().numpy())

print(f"F1 Score: {f1_score}")