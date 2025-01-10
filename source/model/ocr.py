import easyocr
import numpy as np
import ctparse
import pandas as pd

reader = easyocr.Reader(['en'])
result=reader.readtext('images/spring2025.png')
strings=[]
for (bbox, text, prob) in result:
    strings.append([text,int(bbox[0][0]),int(bbox[1][0]),int(bbox[0][1]),int(bbox[2][1])])
columnNames=["Text","Xmin","Xmax","Ymin","Ymax"]
df=pd.DataFrame(strings,columns=columnNames)
df["AvX"]=(df["Xmin"]+df["Xmax"])/2
df["AvY"]=(df["Ymin"]+df["Ymax"])/2
print(df)


