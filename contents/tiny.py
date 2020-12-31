import tinify
import os

tinify.key = 'c8vDqJZFDBcF9hfFmBC6sFGc3kqL5My0'
path = './galley/candidate/'

for dirpath, dirs, files in os.walk(path):
    for file in files:
        imgpath = os.path.join(dirpath, file)
        print("compressing ..."+ imgpath)
        tinify.from_file(imgpath).resize(method = 'fit', width = 3840, height = 2160).to_file(imgpath)
