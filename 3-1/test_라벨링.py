import os

test = "/content/test/valid_resized"
file_count = 0

for dirpath, dirname, filenames in os.walk(test):
    for file in filenames:
        if file[-7:-4].endswith("_02") or file[-7:-4].endswith("_03"):
            label = "마스크 착용"
        elif file[-7:-4].endswith("_01"):
            label = "마스크 미착용"
        print("파일명: %s, 라벨명: %s" % (file, label))
        file_count += 1

print("총 파일 수: %d개" % file_count)