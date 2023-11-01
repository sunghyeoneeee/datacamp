import os
import pandas as pd
from PIL import Image
data = []
columns = ["Image", "Label"]

test = "/Users/bagseonghyeon/Desktop/datacamp/Test"

for dirpath, dirname, filenames in os.walk(test):
    for file in filenames:
      img_path = os.path.join(dirpath, file)
      if file[-7:-4].endswith("_02") or file[-7:-4].endswith("_03"):
          label = "마스크 착용"
      elif file[-7:-4].endswith("_01"):
          label = "마스크 미착용"

      data.append([img_path, label])

df = pd.DataFrame(data, columns=columns)
print(df)