import os
import shutil
import zipfile

import requests

update_zipfile = '../data/files/cache/update/update.zip'

url = 'https://github.com/Random-Creation-of-YassiGame/Coran-Converter/archive/refs/heads/main.zip'

try:
    global r
    r = requests.get(url, allow_redirects=True)

except requests.exceptions.ConnectionError:
    print("Download Error: We think, you have no connection or you are banned ip from GitHub")


open(update_zipfile, 'wb').write(r.content)


with zipfile.ZipFile(update_zipfile, 'r') as zip_ref:
    zip_ref.extractall('../data/files/cache/update/unzip_update')


root_src_dir = '../data/files/cache/update/unzip_update/Coran-Converter-main'
root_dst_dir = '../'

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.move(src_file, dst_dir)