import os
import shutil

import requests

update_zipfile = '../data/files/cache/update/update.zip'

url = 'https://github.com/Random-Creation-of-YassiGame/Coran-Converter/archive/refs/heads/main.zip'
r = requests.get(url, allow_redirects=True)

open(update_zipfile, 'wb').write(r.content)

import zipfile
with zipfile.ZipFile(update_zipfile, 'r') as zip_ref:
    zip_ref.extractall('../data/files/cache/update/unzip_update')

path_folder_update = '../data/files/cache/update/unzip_update/Coran-Converter-main'
destination = '../'

file_names = os.listdir(path_folder_update)

for file_name in file_names:
    shutil.move(os.path.join(path_folder_update, file_name), destination)