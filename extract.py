import glob
import os
import cv2
import pandas as pd
import os
import cv2
import numpy as np
import glob
import os
import shutil
import pandas as pd


image_name = []
label_name = []
laterality = []

def format_list(list):
    for index, value in enumerate(list):
        if index ==0:
            list[index] = int(value)
        else:
            list[index] = float(value)
            
    return list

for image_path in glob.glob('./images/*.jpg'):
    image_name.append(image_path)

for labelPath in glob.glob('./labels/*.txt'):
    with open(labelPath) as file:
        lines = file.readlines()
        if len(lines) == 1:
            annotation_info = format_list(lines[0].split(' '))
            if annotation_info[0] == 1:
                label_name.append(labelPath)
                laterality.append('right')
            elif annotation_info[0] ==0:
                label_name.append(labelPath)
                laterality.append('left')
        elif len(lines) == 2:
            annotation_info = format_list(lines[0].split(' '))
            if annotation_info[0] == 1:
                label_name.append(labelPath)
                laterality.append('right')
            elif annotation_info[0] == 0:
                label_name.append(labelPath)
                laterality.append('left')  
            annotation_info = format_list(lines[1].split(' '))
            if annotation_info[0] == 1:
                label_name.append(labelPath)
                laterality.append('right')
            elif annotation_info[0] == 0:
                label_name.append(labelPath)
                laterality.append('left')


for i in range(0, len(image_name)):
    print(image_name[i], label_name[i], laterality[i])