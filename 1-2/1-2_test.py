import os
import shutil

def test(test_data):
    three = []
    two = []
    one = []

    for dirpath, dirname, filename in os.walk(test_data):
        for file in filename:
            file_test_result = file.split("_")
            if '03' in file_test_result[-1]:
                three.append(os.path.join(dirpath, file))
            elif '02' in file_test_result[-1]:
                two.append(os.path.join(dirpath, file))
            elif '01' in file_test_result[-1]:
                one.append(os.path.join(dirpath, file))

    return three, two, one

test_data = "Test"

three, two, one = test(test_data)

print(len(three))
print(len(two))
print(len(one))