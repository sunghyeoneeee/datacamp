# test 안 폴더 수
import os

test_path = 'Test'
test_list = os.listdir(test_path)
test_count = len(test_list)
print(test_count)