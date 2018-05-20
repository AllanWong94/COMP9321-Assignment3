import os
import urllib.request
import zipfile
print("Downloading Dataset: Billboard-Lyrics to current directory...")
url = "https://www.kaggle.com/rakannimer/billboard-lyrics/downloads/billboard-1964-2015-songs-lyrics.zip/1"
# The Download URL for dataset: billboard-lyrics, format as zip file

path = "."
# Download to current file directory

urllib.request.urlretrieve(url,path)

try:
    zip_file = zipfile.ZipFile("billboard-1964-2015-songs-lyrics.zip")
    for names in zip_file.namelist():
        dest_dir = "./" + names
        zip_file.extract(names, dest_dir)
    zip_file.close()
except Exception as e:
    print("Downloaded data corrupted, please download again.")