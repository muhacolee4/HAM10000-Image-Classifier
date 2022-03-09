import os
import shutil
import pandas as pd
dataDir=r"D:\Users\Engr M2J\Downloads\Compressed\Dataset\All Images"
desDir=r"D:\Users\Engr M2J\Downloads\Compressed\Dataset\reorganized"
readLable=pd.read_csv(r'D:\Users\Engr M2J\Downloads\Compressed\Dataset/HAM10000_metadata.csv')

#print(readLable['dx'].value_counts())
label=readLable['dx'].unique().tolist()
#print (label)
lable_images=[]

for i in label:
    print(i)
    os.mkdir(desDir + str(i) + "/")
    sample=readLable[readLable["dx"]==i]['image_id']
    lable_images.extend(sample)
    shutil.copyfile((dataDir + "/" + id + ".jpg"),(desDir + i + "/" + id + ".jpg"))
    lable_images=[]



