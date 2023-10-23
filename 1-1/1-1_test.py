import os

folder_path = "Test"
file_count = sum([len(files) for r, d, files in os.walk(folder_path)])
print(file_count)