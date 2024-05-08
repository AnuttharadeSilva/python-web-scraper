import urllib.request
import csv
import pandas as pd

csv_path = 'datasets/ovp_all_all_video.csv'
df = pd.read_csv(csv_path)
df = df[["Id","MPEG-4"]].dropna() #remove null values
df = df[~df['MPEG-4'].str.startswith('http://nasa')] #remove not downloadable urls

# df.to_csv("datasets/ovp_all_all_downloadable_video.csv", index=False)

df = df.head(50)
df.to_csv("video_dataset/video_dataset.csv", index=False)

for i in range(len(df)):
    id = df.iloc[i, 0]
    url = str(df.iloc[i, 1])

    print(id, url)

    file_path = "video_dataset/"+str(id)+".mp4"

    try:
        urllib.request.urlretrieve(url, file_path)
        print("Video "+str(id)+" successfully downloaded!")
    except Exception as e:
        print(e)