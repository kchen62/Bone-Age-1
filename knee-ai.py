# importing the modules
import os
import shutil
import pandas as pd

# Providing the folder path
origin = "/Users/kalliechen/Downloads/AI Knee.v14i.yolov5pytorch/images"
target = "/Users/kalliechen/Documents/python/Bone-Age/bone_data"

data = pd.read_excel("/Users/kalliechen/Library/Mobile Documents/com~apple~CloudDocs/Research/Liu - Skeletal Maturity/AI/Data/data-for-bone-age.xlsx")

for row in data.itertuples(index = False):
	if row[7] == "train":
		shutil.copy(origin+'/'+row[0], target+'/train/'+row[0])
	elif row[7] == "test":
		shutil.copy(origin+'/'+row[0], target+'/test/'+row[0])
	else:
		shutil.copy(origin+'/'+row[0], target+'/validation/'+row[0])